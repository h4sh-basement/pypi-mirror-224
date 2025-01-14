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

class RimeSeverityCounts(object):
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
        'num_none_severity': 'str',
        'num_low_severity': 'str',
        'num_high_severity': 'str'
    }

    attribute_map = {
        'num_none_severity': 'numNoneSeverity',
        'num_low_severity': 'numLowSeverity',
        'num_high_severity': 'numHighSeverity'
    }

    def __init__(self, num_none_severity=None, num_low_severity=None, num_high_severity=None):  # noqa: E501
        """RimeSeverityCounts - a model defined in Swagger"""  # noqa: E501
        self._num_none_severity = None
        self._num_low_severity = None
        self._num_high_severity = None
        self.discriminator = None
        if num_none_severity is not None:
            self.num_none_severity = num_none_severity
        if num_low_severity is not None:
            self.num_low_severity = num_low_severity
        if num_high_severity is not None:
            self.num_high_severity = num_high_severity

    @property
    def num_none_severity(self):
        """Gets the num_none_severity of this RimeSeverityCounts.  # noqa: E501


        :return: The num_none_severity of this RimeSeverityCounts.  # noqa: E501
        :rtype: str
        """
        return self._num_none_severity

    @num_none_severity.setter
    def num_none_severity(self, num_none_severity):
        """Sets the num_none_severity of this RimeSeverityCounts.


        :param num_none_severity: The num_none_severity of this RimeSeverityCounts.  # noqa: E501
        :type: str
        """

        self._num_none_severity = num_none_severity

    @property
    def num_low_severity(self):
        """Gets the num_low_severity of this RimeSeverityCounts.  # noqa: E501


        :return: The num_low_severity of this RimeSeverityCounts.  # noqa: E501
        :rtype: str
        """
        return self._num_low_severity

    @num_low_severity.setter
    def num_low_severity(self, num_low_severity):
        """Sets the num_low_severity of this RimeSeverityCounts.


        :param num_low_severity: The num_low_severity of this RimeSeverityCounts.  # noqa: E501
        :type: str
        """

        self._num_low_severity = num_low_severity

    @property
    def num_high_severity(self):
        """Gets the num_high_severity of this RimeSeverityCounts.  # noqa: E501


        :return: The num_high_severity of this RimeSeverityCounts.  # noqa: E501
        :rtype: str
        """
        return self._num_high_severity

    @num_high_severity.setter
    def num_high_severity(self, num_high_severity):
        """Sets the num_high_severity of this RimeSeverityCounts.


        :param num_high_severity: The num_high_severity of this RimeSeverityCounts.  # noqa: E501
        :type: str
        """

        self._num_high_severity = num_high_severity

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
        if issubclass(RimeSeverityCounts, dict):
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
        if not isinstance(other, RimeSeverityCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
