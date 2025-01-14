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


class ProjectGroupUpdateProps(object):
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
    swagger_types = {"project_perm": "str"}

    attribute_map = {"project_perm": "projectPerm"}

    def __init__(self, project_perm=None):  # noqa: E501
        """ProjectGroupUpdateProps - a model defined in Swagger"""  # noqa: E501
        self._project_perm = None
        self.discriminator = None
        self.project_perm = project_perm

    @property
    def project_perm(self):
        """Gets the project_perm of this ProjectGroupUpdateProps.  # noqa: E501


        :return: The project_perm of this ProjectGroupUpdateProps.  # noqa: E501
        :rtype: str
        """
        return self._project_perm

    @project_perm.setter
    def project_perm(self, project_perm):
        """Sets the project_perm of this ProjectGroupUpdateProps.


        :param project_perm: The project_perm of this ProjectGroupUpdateProps.  # noqa: E501
        :type: str
        """
        if project_perm is None:
            raise ValueError(
                "Invalid value for `project_perm`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["admin", "read", "update"]  # noqa: E501
        if project_perm not in allowed_values:
            raise ValueError(
                "Invalid value for `project_perm` ({0}), must be one of {1}".format(  # noqa: E501
                    project_perm, allowed_values
                )
            )

        self._project_perm = project_perm

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
        if issubclass(ProjectGroupUpdateProps, dict):
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
        if not isinstance(other, ProjectGroupUpdateProps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
