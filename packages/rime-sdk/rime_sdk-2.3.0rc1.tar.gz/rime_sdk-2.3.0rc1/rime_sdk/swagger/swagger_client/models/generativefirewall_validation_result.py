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

class GenerativefirewallValidationResult(object):
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
        'type': 'GenerativefirewallValidationType',
        'rules': 'list[GenerativefirewallRuleOutput]'
    }

    attribute_map = {
        'type': 'type',
        'rules': 'rules'
    }

    def __init__(self, type=None, rules=None):  # noqa: E501
        """GenerativefirewallValidationResult - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._rules = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if rules is not None:
            self.rules = rules

    @property
    def type(self):
        """Gets the type of this GenerativefirewallValidationResult.  # noqa: E501


        :return: The type of this GenerativefirewallValidationResult.  # noqa: E501
        :rtype: GenerativefirewallValidationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GenerativefirewallValidationResult.


        :param type: The type of this GenerativefirewallValidationResult.  # noqa: E501
        :type: GenerativefirewallValidationType
        """

        self._type = type

    @property
    def rules(self):
        """Gets the rules of this GenerativefirewallValidationResult.  # noqa: E501

        Output of all the different firewall rules.  # noqa: E501

        :return: The rules of this GenerativefirewallValidationResult.  # noqa: E501
        :rtype: list[GenerativefirewallRuleOutput]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this GenerativefirewallValidationResult.

        Output of all the different firewall rules.  # noqa: E501

        :param rules: The rules of this GenerativefirewallValidationResult.  # noqa: E501
        :type: list[GenerativefirewallRuleOutput]
        """

        self._rules = rules

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
        if issubclass(GenerativefirewallValidationResult, dict):
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
        if not isinstance(other, GenerativefirewallValidationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
