# coding: utf-8

"""
    EmbedOps API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@embedops.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class MetricResultCiRun(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "id": "str",
        "branch": "str",
        "commit_id": "str",
        "pipeline_id": "str",
        "pipeline_url": "str",
        "status": "str",
        "type": "CIRunType",
    }

    attribute_map = {
        "id": "id",
        "branch": "branch",
        "commit_id": "commitId",
        "pipeline_id": "pipelineId",
        "pipeline_url": "pipelineUrl",
        "status": "status",
        "type": "type",
    }

    def __init__(
        self,
        id=None,
        branch=None,
        commit_id=None,
        pipeline_id=None,
        pipeline_url=None,
        status=None,
        type=None,
    ):  # noqa: E501
        """MetricResultCiRun - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._branch = None
        self._commit_id = None
        self._pipeline_id = None
        self._pipeline_url = None
        self._status = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if branch is not None:
            self.branch = branch
        if commit_id is not None:
            self.commit_id = commit_id
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_url is not None:
            self.pipeline_url = pipeline_url
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this MetricResultCiRun.  # noqa: E501


        :return: The id of this MetricResultCiRun.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricResultCiRun.


        :param id: The id of this MetricResultCiRun.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def branch(self):
        """Gets the branch of this MetricResultCiRun.  # noqa: E501


        :return: The branch of this MetricResultCiRun.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this MetricResultCiRun.


        :param branch: The branch of this MetricResultCiRun.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def commit_id(self):
        """Gets the commit_id of this MetricResultCiRun.  # noqa: E501


        :return: The commit_id of this MetricResultCiRun.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this MetricResultCiRun.


        :param commit_id: The commit_id of this MetricResultCiRun.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this MetricResultCiRun.  # noqa: E501


        :return: The pipeline_id of this MetricResultCiRun.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this MetricResultCiRun.


        :param pipeline_id: The pipeline_id of this MetricResultCiRun.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

    @property
    def pipeline_url(self):
        """Gets the pipeline_url of this MetricResultCiRun.  # noqa: E501


        :return: The pipeline_url of this MetricResultCiRun.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_url

    @pipeline_url.setter
    def pipeline_url(self, pipeline_url):
        """Sets the pipeline_url of this MetricResultCiRun.


        :param pipeline_url: The pipeline_url of this MetricResultCiRun.  # noqa: E501
        :type: str
        """

        self._pipeline_url = pipeline_url

    @property
    def status(self):
        """Gets the status of this MetricResultCiRun.  # noqa: E501


        :return: The status of this MetricResultCiRun.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MetricResultCiRun.


        :param status: The status of this MetricResultCiRun.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this MetricResultCiRun.  # noqa: E501


        :return: The type of this MetricResultCiRun.  # noqa: E501
        :rtype: CIRunType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetricResultCiRun.


        :param type: The type of this MetricResultCiRun.  # noqa: E501
        :type: CIRunType
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(MetricResultCiRun, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricResultCiRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
