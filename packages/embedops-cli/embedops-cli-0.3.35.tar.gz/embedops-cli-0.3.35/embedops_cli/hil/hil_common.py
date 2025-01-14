"""Common functions used by the HIL commands"""
import sys
import json
import os.path
import tempfile
import traceback
import subprocess
from datetime import datetime
from os import getcwd
import click
from dynaconf import Dynaconf
from embedops_cli.hil.hil_types import get_hil_config_path
from embedops_cli.sse import eo_sse
from embedops_cli import config
from embedops_cli.api.rest import ApiException
from embedops_cli.eo_types import (
    EmbedOpsException,
    NoAvailableHilDevice,
    NoRepoIdException,
    NoCIRunIdException,
    NetworkException,
    UnauthorizedUserException,
)
from embedops_cli.hil.hil_types import (
    NoHILSDKPathException,
    HILSDKPathDoesNotExistException,
    HILPackageCreationException,
)
from embedops_cli.hil.hil_package import create_hil_package
from embedops_cli import embedops_authorization
from embedops_cli.sse.sse_api import SSEApi
from embedops_cli.utilities import (
    echo_error_and_fix,
    get_client as util_get_client,
)
from embedops_cli.utilities import logging_setup
from embedops_cli.hil import hil_package
from embedops_cli.api.models import HilRunCreateProps

_logger = logging_setup(__name__)


def get_hil_root_path():
    """get hil_root_path from .embedops/hil/config.yml

    Returns:
        str: the value stored in <repo_root>/.embedops/hil/config.yml:hil_root_path or None
    """
    dot_eo = Dynaconf(
        load_dotenv=False,
        settings_files=[get_hil_config_path()],
        silent_errors=True,
    )
    dot_eo.configure(
        LOADERS_FOR_DYNACONF=[
            "dynaconf.loaders.yaml_loader",
        ]
    )
    return dot_eo.get("hil_root_path")


def hil_echo_run_banner(ex_pkg_id: str, sdk_path: str) -> None:
    """print the embedops job banner to the console (local and pipeline)

    Args:
        ex_pkg_id (str): repo_id or ci_run_id
        sdk_path (str): path to hil sdk from the repo root.
                        set in .embedops/hil/config.yml:hil_root_path
    """
    git_hash_run = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    if git_hash_run.returncode != 0:
        git_hash = "Not Available"
    else:
        git_hash = git_hash_run.stdout.strip()

    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    click.secho("-" * 80, fg="magenta")
    click.secho("Running job      'hil'", err=False, fg="magenta")
    click.secho(f"-> repo id       '{ex_pkg_id}'", err=False, fg="white")
    click.secho(f"-> directory     '{getcwd()}'", err=False, fg="white")
    click.secho(f"-> hil sdk path  '{sdk_path}'", err=False, fg="white")
    click.secho(f"-> git sha       '{git_hash}'", err=False, fg="white")
    click.secho(f"-> timestamp     '{current_time}'", err=False, fg="white")
    click.secho("-" * 80, fg="magenta")
    click.secho("\n")


def hil_run(local: bool = False) -> int:  # pylint: disable=R0912,R0914,R0915
    """
    Run hil in either local or CI mode,
    using the current repository as a source.
    """

    try:
        ex_pkg_id = config.settings.run_id
        if not ex_pkg_id and not local:
            raise NoCIRunIdException()
        if local:
            ex_pkg_id = config.get_repo_id()
            if not ex_pkg_id:
                raise NoRepoIdException()

        hil_root_path = get_hil_root_path()
        if not hil_root_path:
            raise NoHILSDKPathException()

        hil_sdk_full_path = os.path.join(os.path.curdir, hil_root_path)
        if not os.path.isdir(hil_sdk_full_path):
            raise HILSDKPathDoesNotExistException()

        _logger.debug(f"using host: {config.settings.host}")
        hil_echo_run_banner(ex_pkg_id, hil_sdk_full_path)

        # Compile the package in a temporary folder that is deleted after uploading
        with tempfile.TemporaryDirectory() as tmp_dir:
            hil_ep_file = os.path.join(tmp_dir, "hil_ep.zip")
            # TODO: Build artifacts and manifest data are being left blank intentionally
            if not create_hil_package([], hil_root_path, {}, hil_ep_file):
                raise HILPackageCreationException()

            # Get the upload URL
            _logger.debug(
                f"[local={local}] getting presigned url for hil execution package upload"
            )
            if local:
                api_client = embedops_authorization.get_user_client()
                upload_url_response = api_client.get_pre_signed_url_for_upload(
                    ex_pkg_id
                )
            else:
                api_client = util_get_client()
                upload_url_response = api_client.get_pre_signed_url_for_upload_0(
                    ex_pkg_id
                )
            upload_url = upload_url_response.url
            try:
                upload_status = hil_package.upload_hil_package(hil_ep_file, upload_url)
                if upload_status != 200:
                    raise NetworkException(
                        upload_status,
                        message="network exception during execution package upload",
                    )
            except ApiException as exc:
                raise EmbedOpsException(
                    fix_message=f"Uploading HIL execution package failed: {exc.body.decode()}"
                ) from exc

        if local:
            # After package is uploaded, call into SSE and print any further events
            sse_api = SSEApi()
            for event in sse_api.sse_hil_run(ex_pkg_id):
                if event.event == eo_sse.SSE_TEXT_EVENT:
                    eo_sse.sse_print_command_text(event)
                elif event.event == eo_sse.SSE_RESULT_EVENT:
                    result_event_obj = json.loads(event.data)
                    return result_event_obj["exitCode"]
                else:
                    _logger.debug(f"got unhandled SSE Event: {event.event}")

            # If the command hasn't returned anything yet, exit here
            return 2

        print("starting hil run...", file=sys.stderr)
        try:
            response = api_client.init_hil_run_from_ci(
                body=HilRunCreateProps(ci_run_id=ex_pkg_id)
            )
            print(f"HIL run started successfully. View progress here: {response.url}")
            return 0
        except ApiException as exc:
            if exc.status == 424:  #
                raise NoAvailableHilDevice(f"{exc.body.decode()}") from exc
            raise exc

    except (
        NoRepoIdException,
        NoHILSDKPathException,
        HILSDKPathDoesNotExistException,
        HILPackageCreationException,
        NetworkException,
        UnauthorizedUserException,
        EmbedOpsException,
        NoAvailableHilDevice,
    ) as exc:
        echo_error_and_fix(exc)
        return 2
    except ApiException as exc:
        echo_error_and_fix(
            EmbedOpsException(
                fix_message=f"Uploading HIL execution package failed: {exc.body.decode()}"
            )
        )
    except Exception:  # pylint: disable=W0718
        traceback.print_exc()
    return -1
