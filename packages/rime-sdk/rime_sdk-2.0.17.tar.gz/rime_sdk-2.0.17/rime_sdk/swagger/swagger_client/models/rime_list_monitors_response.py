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

class RimeListMonitorsResponse(object):
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
        'monitors': 'list[MonitorMonitor]',
        'next_page_token': 'str',
        'has_more': 'bool'
    }

    attribute_map = {
        'monitors': 'monitors',
        'next_page_token': 'nextPageToken',
        'has_more': 'hasMore'
    }

    def __init__(self, monitors=None, next_page_token=None, has_more=None):  # noqa: E501
        """RimeListMonitorsResponse - a model defined in Swagger"""  # noqa: E501
        self._monitors = None
        self._next_page_token = None
        self._has_more = None
        self.discriminator = None
        if monitors is not None:
            self.monitors = monitors
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if has_more is not None:
            self.has_more = has_more

    @property
    def monitors(self):
        """Gets the monitors of this RimeListMonitorsResponse.  # noqa: E501

        The list of monitors.  # noqa: E501

        :return: The monitors of this RimeListMonitorsResponse.  # noqa: E501
        :rtype: list[MonitorMonitor]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """Sets the monitors of this RimeListMonitorsResponse.

        The list of monitors.  # noqa: E501

        :param monitors: The monitors of this RimeListMonitorsResponse.  # noqa: E501
        :type: list[MonitorMonitor]
        """

        self._monitors = monitors

    @property
    def next_page_token(self):
        """Gets the next_page_token of this RimeListMonitorsResponse.  # noqa: E501

        The pagination token.  # noqa: E501

        :return: The next_page_token of this RimeListMonitorsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this RimeListMonitorsResponse.

        The pagination token.  # noqa: E501

        :param next_page_token: The next_page_token of this RimeListMonitorsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def has_more(self):
        """Gets the has_more of this RimeListMonitorsResponse.  # noqa: E501


        :return: The has_more of this RimeListMonitorsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this RimeListMonitorsResponse.


        :param has_more: The has_more of this RimeListMonitorsResponse.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

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
        if issubclass(RimeListMonitorsResponse, dict):
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
        if not isinstance(other, RimeListMonitorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
