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

class RimeListImagesRequest(object):
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
        'page_token': 'str',
        'page_size': 'str',
        'pip_libraries': 'list[ListImagesRequestPipLibraryFilter]'
    }

    attribute_map = {
        'page_token': 'pageToken',
        'page_size': 'pageSize',
        'pip_libraries': 'pipLibraries'
    }

    def __init__(self, page_token=None, page_size=None, pip_libraries=None):  # noqa: E501
        """RimeListImagesRequest - a model defined in Swagger"""  # noqa: E501
        self._page_token = None
        self._page_size = None
        self._pip_libraries = None
        self.discriminator = None
        if page_token is not None:
            self.page_token = page_token
        if page_size is not None:
            self.page_size = page_size
        if pip_libraries is not None:
            self.pip_libraries = pip_libraries

    @property
    def page_token(self):
        """Gets the page_token of this RimeListImagesRequest.  # noqa: E501

        Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results.  # noqa: E501

        :return: The page_token of this RimeListImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._page_token

    @page_token.setter
    def page_token(self, page_token):
        """Sets the page_token of this RimeListImagesRequest.

        Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results.  # noqa: E501

        :param page_token: The page_token of this RimeListImagesRequest.  # noqa: E501
        :type: str
        """

        self._page_token = page_token

    @property
    def page_size(self):
        """Gets the page_size of this RimeListImagesRequest.  # noqa: E501

        The maximum number of Image objects to return in a single page.  # noqa: E501

        :return: The page_size of this RimeListImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this RimeListImagesRequest.

        The maximum number of Image objects to return in a single page.  # noqa: E501

        :param page_size: The page_size of this RimeListImagesRequest.  # noqa: E501
        :type: str
        """

        self._page_size = page_size

    @property
    def pip_libraries(self):
        """Gets the pip_libraries of this RimeListImagesRequest.  # noqa: E501

        Optional. Filters the list for libraries that are installed on the Managed Image. The filter is only active when the list is not empty. When this filter is specified, do not include a pageToken field in the request.  # noqa: E501

        :return: The pip_libraries of this RimeListImagesRequest.  # noqa: E501
        :rtype: list[ListImagesRequestPipLibraryFilter]
        """
        return self._pip_libraries

    @pip_libraries.setter
    def pip_libraries(self, pip_libraries):
        """Sets the pip_libraries of this RimeListImagesRequest.

        Optional. Filters the list for libraries that are installed on the Managed Image. The filter is only active when the list is not empty. When this filter is specified, do not include a pageToken field in the request.  # noqa: E501

        :param pip_libraries: The pip_libraries of this RimeListImagesRequest.  # noqa: E501
        :type: list[ListImagesRequestPipLibraryFilter]
        """

        self._pip_libraries = pip_libraries

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
        if issubclass(RimeListImagesRequest, dict):
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
        if not isinstance(other, RimeListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
