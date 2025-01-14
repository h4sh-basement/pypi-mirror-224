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

class RimeGetDatasetFileUploadURLResponse(object):
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
        'upload_url': 'str',
        'done_file_upload_url': 'str',
        'destination_url': 'str',
        'upload_limit': 'str'
    }

    attribute_map = {
        'upload_url': 'uploadUrl',
        'done_file_upload_url': 'doneFileUploadUrl',
        'destination_url': 'destinationUrl',
        'upload_limit': 'uploadLimit'
    }

    def __init__(self, upload_url=None, done_file_upload_url=None, destination_url=None, upload_limit=None):  # noqa: E501
        """RimeGetDatasetFileUploadURLResponse - a model defined in Swagger"""  # noqa: E501
        self._upload_url = None
        self._done_file_upload_url = None
        self._destination_url = None
        self._upload_limit = None
        self.discriminator = None
        if upload_url is not None:
            self.upload_url = upload_url
        if done_file_upload_url is not None:
            self.done_file_upload_url = done_file_upload_url
        if destination_url is not None:
            self.destination_url = destination_url
        if upload_limit is not None:
            self.upload_limit = upload_limit

    @property
    def upload_url(self):
        """Gets the upload_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501


        :return: The upload_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this RimeGetDatasetFileUploadURLResponse.


        :param upload_url: The upload_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :type: str
        """

        self._upload_url = upload_url

    @property
    def done_file_upload_url(self):
        """Gets the done_file_upload_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501


        :return: The done_file_upload_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :rtype: str
        """
        return self._done_file_upload_url

    @done_file_upload_url.setter
    def done_file_upload_url(self, done_file_upload_url):
        """Sets the done_file_upload_url of this RimeGetDatasetFileUploadURLResponse.


        :param done_file_upload_url: The done_file_upload_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :type: str
        """

        self._done_file_upload_url = done_file_upload_url

    @property
    def destination_url(self):
        """Gets the destination_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501


        :return: The destination_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :rtype: str
        """
        return self._destination_url

    @destination_url.setter
    def destination_url(self, destination_url):
        """Sets the destination_url of this RimeGetDatasetFileUploadURLResponse.


        :param destination_url: The destination_url of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :type: str
        """

        self._destination_url = destination_url

    @property
    def upload_limit(self):
        """Gets the upload_limit of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501


        :return: The upload_limit of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :rtype: str
        """
        return self._upload_limit

    @upload_limit.setter
    def upload_limit(self, upload_limit):
        """Sets the upload_limit of this RimeGetDatasetFileUploadURLResponse.


        :param upload_limit: The upload_limit of this RimeGetDatasetFileUploadURLResponse.  # noqa: E501
        :type: str
        """

        self._upload_limit = upload_limit

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
        if issubclass(RimeGetDatasetFileUploadURLResponse, dict):
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
        if not isinstance(other, RimeGetDatasetFileUploadURLResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
