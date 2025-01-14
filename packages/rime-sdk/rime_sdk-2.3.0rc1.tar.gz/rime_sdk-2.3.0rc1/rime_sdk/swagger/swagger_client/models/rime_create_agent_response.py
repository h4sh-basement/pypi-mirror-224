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

class RimeCreateAgentResponse(object):
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
        'config': 'str',
        'agent_id': 'RimeUUID'
    }

    attribute_map = {
        'config': 'config',
        'agent_id': 'agentId'
    }

    def __init__(self, config=None, agent_id=None):  # noqa: E501
        """RimeCreateAgentResponse - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self._agent_id = None
        self.discriminator = None
        if config is not None:
            self.config = config
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def config(self):
        """Gets the config of this RimeCreateAgentResponse.  # noqa: E501

        File that contains configuration values for installing the agent.  # noqa: E501

        :return: The config of this RimeCreateAgentResponse.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this RimeCreateAgentResponse.

        File that contains configuration values for installing the agent.  # noqa: E501

        :param config: The config of this RimeCreateAgentResponse.  # noqa: E501
        :type: str
        """

        self._config = config

    @property
    def agent_id(self):
        """Gets the agent_id of this RimeCreateAgentResponse.  # noqa: E501


        :return: The agent_id of this RimeCreateAgentResponse.  # noqa: E501
        :rtype: RimeUUID
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this RimeCreateAgentResponse.


        :param agent_id: The agent_id of this RimeCreateAgentResponse.  # noqa: E501
        :type: RimeUUID
        """

        self._agent_id = agent_id

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
        if issubclass(RimeCreateAgentResponse, dict):
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
        if not isinstance(other, RimeCreateAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
