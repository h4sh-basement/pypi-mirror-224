# coding: utf-8

"""
    RIME Rest API

    API methods for RIME. Must be authenticated with `rime-api-key` header.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: dev@robustintelligence.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RimeLimitStatus(object):
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
        'limit': 'RimeLicenseLimit',
        'limit_status': 'RimeLimitStatusStatus',
        'limit_value': 'str',
        'current_value': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'limit_status': 'limitStatus',
        'limit_value': 'limitValue',
        'current_value': 'currentValue'
    }

    def __init__(self, limit=None, limit_status=None, limit_value=None, current_value=None):  # noqa: E501
        """RimeLimitStatus - a model defined in Swagger"""  # noqa: E501
        self._limit = None
        self._limit_status = None
        self._limit_value = None
        self._current_value = None
        self.discriminator = None
        if limit is not None:
            self.limit = limit
        if limit_status is not None:
            self.limit_status = limit_status
        if limit_value is not None:
            self.limit_value = limit_value
        if current_value is not None:
            self.current_value = current_value

    @property
    def limit(self):
        """Gets the limit of this RimeLimitStatus.  # noqa: E501


        :return: The limit of this RimeLimitStatus.  # noqa: E501
        :rtype: RimeLicenseLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this RimeLimitStatus.


        :param limit: The limit of this RimeLimitStatus.  # noqa: E501
        :type: RimeLicenseLimit
        """

        self._limit = limit

    @property
    def limit_status(self):
        """Gets the limit_status of this RimeLimitStatus.  # noqa: E501


        :return: The limit_status of this RimeLimitStatus.  # noqa: E501
        :rtype: RimeLimitStatusStatus
        """
        return self._limit_status

    @limit_status.setter
    def limit_status(self, limit_status):
        """Sets the limit_status of this RimeLimitStatus.


        :param limit_status: The limit_status of this RimeLimitStatus.  # noqa: E501
        :type: RimeLimitStatusStatus
        """

        self._limit_status = limit_status

    @property
    def limit_value(self):
        """Gets the limit_value of this RimeLimitStatus.  # noqa: E501


        :return: The limit_value of this RimeLimitStatus.  # noqa: E501
        :rtype: str
        """
        return self._limit_value

    @limit_value.setter
    def limit_value(self, limit_value):
        """Sets the limit_value of this RimeLimitStatus.


        :param limit_value: The limit_value of this RimeLimitStatus.  # noqa: E501
        :type: str
        """

        self._limit_value = limit_value

    @property
    def current_value(self):
        """Gets the current_value of this RimeLimitStatus.  # noqa: E501


        :return: The current_value of this RimeLimitStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this RimeLimitStatus.


        :param current_value: The current_value of this RimeLimitStatus.  # noqa: E501
        :type: str
        """

        self._current_value = current_value

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
        if issubclass(RimeLimitStatus, dict):
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
        if not isinstance(other, RimeLimitStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
