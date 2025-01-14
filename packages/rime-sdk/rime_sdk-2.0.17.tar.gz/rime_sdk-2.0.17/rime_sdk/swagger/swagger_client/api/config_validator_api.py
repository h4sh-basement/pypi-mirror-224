# coding: utf-8

"""
    RIME Rest API

    API methods for RIME. Must be authenticated with `rime-api-key` header.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: dev@robustintelligence.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rime_sdk.swagger.swagger_client.api_client import ApiClient


class ConfigValidatorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def config_validator_validate_test_config(self, body, config_type, **kwargs):  # noqa: E501
        """ValidateTestConfig  # noqa: E501

        Returns whether the provided JSON string is a valid test config. Test configs include Stress Test, Test Suite, Continuous Test, and Continuous Test Incremental configs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.config_validator_validate_test_config(body, config_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfigvalidatorConfigTypeBody body: (required)
        :param str config_type: The type of config to validate. (required)
        :return: RimeValidateTestConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.config_validator_validate_test_config_with_http_info(body, config_type, **kwargs)  # noqa: E501
        else:
            (data) = self.config_validator_validate_test_config_with_http_info(body, config_type, **kwargs)  # noqa: E501
            return data

    def config_validator_validate_test_config_with_http_info(self, body, config_type, **kwargs):  # noqa: E501
        """ValidateTestConfig  # noqa: E501

        Returns whether the provided JSON string is a valid test config. Test configs include Stress Test, Test Suite, Continuous Test, and Continuous Test Incremental configs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.config_validator_validate_test_config_with_http_info(body, config_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfigvalidatorConfigTypeBody body: (required)
        :param str config_type: The type of config to validate. (required)
        :return: RimeValidateTestConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'config_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method config_validator_validate_test_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `config_validator_validate_test_config`")  # noqa: E501
        # verify the required parameter 'config_type' is set
        if ('config_type' not in params or
                params['config_type'] is None):
            raise ValueError("Missing the required parameter `config_type` when calling `config_validator_validate_test_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_type' in params:
            path_params['configType'] = params['config_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/internal/config-validator/{configType}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeValidateTestConfigResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
