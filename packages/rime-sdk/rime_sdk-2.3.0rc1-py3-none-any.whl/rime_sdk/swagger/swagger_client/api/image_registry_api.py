# coding: utf-8

"""
    Robust Intelligence REST API

    API methods for Robust Intelligence. Users must authenticate using the `rime-api-key` header.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: dev@robustintelligence.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rime_sdk.swagger.swagger_client.api_client import ApiClient


class ImageRegistryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def image_registry_create_image(self, body, **kwargs):  # noqa: E501
        """CreateImage  # noqa: E501

        Creates a new Managed Image with a unique name.  Managed images are not currently supported in a Cloud deployment. Please reach out to Robust Intelligence for support if this functionality is required for your deployment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_create_image(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RimeCreateImageRequest body: (required)
        :return: RimeCreateImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_registry_create_image_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.image_registry_create_image_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def image_registry_create_image_with_http_info(self, body, **kwargs):  # noqa: E501
        """CreateImage  # noqa: E501

        Creates a new Managed Image with a unique name.  Managed images are not currently supported in a Cloud deployment. Please reach out to Robust Intelligence for support if this functionality is required for your deployment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_create_image_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RimeCreateImageRequest body: (required)
        :return: RimeCreateImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_registry_create_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `image_registry_create_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        auth_settings = ['X-Firewall-Api-Key', 'rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/images', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeCreateImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def image_registry_delete_image(self, name, **kwargs):  # noqa: E501
        """DeleteImage  # noqa: E501

        Deletes a specified Managed Image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_delete_image(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of existing Managed Image to delete. (required)
        :return: RimeDeleteImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_registry_delete_image_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.image_registry_delete_image_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def image_registry_delete_image_with_http_info(self, name, **kwargs):  # noqa: E501
        """DeleteImage  # noqa: E501

        Deletes a specified Managed Image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_delete_image_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of existing Managed Image to delete. (required)
        :return: RimeDeleteImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_registry_delete_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `image_registry_delete_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Firewall-Api-Key', 'rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/images/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeDeleteImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def image_registry_get_image(self, name, **kwargs):  # noqa: E501
        """GetImage  # noqa: E501

        Returns the definition of a specified Managed Image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_get_image(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the existing Managed Image. (required)
        :return: RimeGetImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_registry_get_image_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.image_registry_get_image_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def image_registry_get_image_with_http_info(self, name, **kwargs):  # noqa: E501
        """GetImage  # noqa: E501

        Returns the definition of a specified Managed Image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_get_image_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the existing Managed Image. (required)
        :return: RimeGetImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_registry_get_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `image_registry_get_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Firewall-Api-Key', 'rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/images/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeGetImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def image_registry_list_images(self, **kwargs):  # noqa: E501
        """ListImages  # noqa: E501

        List all Managed Images that match a specified set of constraints.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_list_images(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token: Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results.
        :param str page_size: The maximum number of Image objects to return in a single page.
        :return: RimeListImagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_registry_list_images_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.image_registry_list_images_with_http_info(**kwargs)  # noqa: E501
            return data

    def image_registry_list_images_with_http_info(self, **kwargs):  # noqa: E501
        """ListImages  # noqa: E501

        List all Managed Images that match a specified set of constraints.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_list_images_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token: Specifies a page of the list returned by a ListImages query. The ListImages query returns a pageToken when there is more than one page of results.
        :param str page_size: The maximum number of Image objects to return in a single page.
        :return: RimeListImagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_token', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_registry_list_images" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Firewall-Api-Key', 'rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/images', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeListImagesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def image_registry_list_images2(self, body, **kwargs):  # noqa: E501
        """ListImages  # noqa: E501

        List all Managed Images that match a specified set of constraints.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_list_images2(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RimeListImagesRequest body: (required)
        :return: RimeListImagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_registry_list_images2_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.image_registry_list_images2_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def image_registry_list_images2_with_http_info(self, body, **kwargs):  # noqa: E501
        """ListImages  # noqa: E501

        List all Managed Images that match a specified set of constraints.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} # TODO page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # TODO # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this     # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers) # TODO     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['INSERT_OBJECT_KEY']) # TODO     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_list_images2_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RimeListImagesRequest body: (required)
        :return: RimeListImagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_registry_list_images2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `image_registry_list_images2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        auth_settings = ['X-Firewall-Api-Key', 'rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/images/list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeListImagesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def image_registry_update_build_info(self, body, **kwargs):  # noqa: E501
        """UpdateBuildInfo updates the information about an image after an image build for it has completed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_update_build_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RimeUpdateBuildInfoRequest body: (required)
        :return: RimeUpdateBuildInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.image_registry_update_build_info_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.image_registry_update_build_info_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def image_registry_update_build_info_with_http_info(self, body, **kwargs):  # noqa: E501
        """UpdateBuildInfo updates the information about an image after an image build for it has completed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.image_registry_update_build_info_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RimeUpdateBuildInfoRequest body: (required)
        :return: RimeUpdateBuildInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_registry_update_build_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `image_registry_update_build_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        auth_settings = ['X-Firewall-Api-Key', 'rime-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/internal/images/update-info', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RimeUpdateBuildInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
