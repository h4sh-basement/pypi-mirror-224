# coding: utf-8

"""
    Robust Intelligence REST API

    API methods for Robust Intelligence. Users must authenticate using the `rime-api-key` header.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: dev@robustintelligence.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RimeUserRole(object):
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
        'subject_type': 'RimeSubjectType',
        'subject_id': 'str',
        'role': 'RimeActorRole',
        'implicit_grant': 'bool'
    }

    attribute_map = {
        'subject_type': 'subjectType',
        'subject_id': 'subjectId',
        'role': 'role',
        'implicit_grant': 'implicitGrant'
    }

    def __init__(self, subject_type=None, subject_id=None, role=None, implicit_grant=None):  # noqa: E501
        """RimeUserRole - a model defined in Swagger"""  # noqa: E501
        self._subject_type = None
        self._subject_id = None
        self._role = None
        self._implicit_grant = None
        self.discriminator = None
        if subject_type is not None:
            self.subject_type = subject_type
        if subject_id is not None:
            self.subject_id = subject_id
        if role is not None:
            self.role = role
        if implicit_grant is not None:
            self.implicit_grant = implicit_grant

    @property
    def subject_type(self):
        """Gets the subject_type of this RimeUserRole.  # noqa: E501


        :return: The subject_type of this RimeUserRole.  # noqa: E501
        :rtype: RimeSubjectType
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this RimeUserRole.


        :param subject_type: The subject_type of this RimeUserRole.  # noqa: E501
        :type: RimeSubjectType
        """

        self._subject_type = subject_type

    @property
    def subject_id(self):
        """Gets the subject_id of this RimeUserRole.  # noqa: E501


        :return: The subject_id of this RimeUserRole.  # noqa: E501
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this RimeUserRole.


        :param subject_id: The subject_id of this RimeUserRole.  # noqa: E501
        :type: str
        """

        self._subject_id = subject_id

    @property
    def role(self):
        """Gets the role of this RimeUserRole.  # noqa: E501


        :return: The role of this RimeUserRole.  # noqa: E501
        :rtype: RimeActorRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RimeUserRole.


        :param role: The role of this RimeUserRole.  # noqa: E501
        :type: RimeActorRole
        """

        self._role = role

    @property
    def implicit_grant(self):
        """Gets the implicit_grant of this RimeUserRole.  # noqa: E501


        :return: The implicit_grant of this RimeUserRole.  # noqa: E501
        :rtype: bool
        """
        return self._implicit_grant

    @implicit_grant.setter
    def implicit_grant(self, implicit_grant):
        """Sets the implicit_grant of this RimeUserRole.


        :param implicit_grant: The implicit_grant of this RimeUserRole.  # noqa: E501
        :type: bool
        """

        self._implicit_grant = implicit_grant

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RimeUserRole, dict):
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
        if not isinstance(other, RimeUserRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
