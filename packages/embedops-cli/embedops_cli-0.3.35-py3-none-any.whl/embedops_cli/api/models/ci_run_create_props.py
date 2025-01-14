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


class CIRunCreateProps(object):
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
        "branch": "str",
        "source_type": "str",
        "commit_id": "str",
        "name": "str",
        "pipeline_id": "str",
        "pipeline_url": "str",
        "status": "str",
        "type": "CIRunType",
    }

    attribute_map = {
        "branch": "branch",
        "source_type": "sourceType",
        "commit_id": "commitId",
        "name": "name",
        "pipeline_id": "pipelineId",
        "pipeline_url": "pipelineUrl",
        "status": "status",
        "type": "type",
    }

    def __init__(
        self,
        branch=None,
        source_type=None,
        commit_id=None,
        name=None,
        pipeline_id=None,
        pipeline_url=None,
        status=None,
        type=None,
    ):  # noqa: E501
        """CIRunCreateProps - a model defined in Swagger"""  # noqa: E501
        self._branch = None
        self._source_type = None
        self._commit_id = None
        self._name = None
        self._pipeline_id = None
        self._pipeline_url = None
        self._status = None
        self._type = None
        self.discriminator = None
        self.branch = branch
        if source_type is not None:
            self.source_type = source_type
        self.commit_id = commit_id
        if name is not None:
            self.name = name
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_url is not None:
            self.pipeline_url = pipeline_url
        if status is not None:
            self.status = status
        self.type = type

    @property
    def branch(self):
        """Gets the branch of this CIRunCreateProps.  # noqa: E501


        :return: The branch of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this CIRunCreateProps.


        :param branch: The branch of this CIRunCreateProps.  # noqa: E501
        :type: str
        """
        if branch is None:
            raise ValueError(
                "Invalid value for `branch`, must not be `None`"
            )  # noqa: E501

        self._branch = branch

    @property
    def source_type(self):
        """Gets the source_type of this CIRunCreateProps.  # noqa: E501


        :return: The source_type of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CIRunCreateProps.


        :param source_type: The source_type of this CIRunCreateProps.  # noqa: E501
        :type: str
        """
        allowed_values = ["branch", "tag"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}".format(  # noqa: E501
                    source_type, allowed_values
                )
            )

        self._source_type = source_type

    @property
    def commit_id(self):
        """Gets the commit_id of this CIRunCreateProps.  # noqa: E501


        :return: The commit_id of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this CIRunCreateProps.


        :param commit_id: The commit_id of this CIRunCreateProps.  # noqa: E501
        :type: str
        """
        if commit_id is None:
            raise ValueError(
                "Invalid value for `commit_id`, must not be `None`"
            )  # noqa: E501

        self._commit_id = commit_id

    @property
    def name(self):
        """Gets the name of this CIRunCreateProps.  # noqa: E501


        :return: The name of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CIRunCreateProps.


        :param name: The name of this CIRunCreateProps.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this CIRunCreateProps.  # noqa: E501


        :return: The pipeline_id of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this CIRunCreateProps.


        :param pipeline_id: The pipeline_id of this CIRunCreateProps.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

    @property
    def pipeline_url(self):
        """Gets the pipeline_url of this CIRunCreateProps.  # noqa: E501


        :return: The pipeline_url of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_url

    @pipeline_url.setter
    def pipeline_url(self, pipeline_url):
        """Sets the pipeline_url of this CIRunCreateProps.


        :param pipeline_url: The pipeline_url of this CIRunCreateProps.  # noqa: E501
        :type: str
        """

        self._pipeline_url = pipeline_url

    @property
    def status(self):
        """Gets the status of this CIRunCreateProps.  # noqa: E501


        :return: The status of this CIRunCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CIRunCreateProps.


        :param status: The status of this CIRunCreateProps.  # noqa: E501
        :type: str
        """
        allowed_values = ["running", "success", "failure"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this CIRunCreateProps.  # noqa: E501


        :return: The type of this CIRunCreateProps.  # noqa: E501
        :rtype: CIRunType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CIRunCreateProps.


        :param type: The type of this CIRunCreateProps.  # noqa: E501
        :type: CIRunType
        """
        if type is None:
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

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
        if issubclass(CIRunCreateProps, dict):
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
        if not isinstance(other, CIRunCreateProps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
