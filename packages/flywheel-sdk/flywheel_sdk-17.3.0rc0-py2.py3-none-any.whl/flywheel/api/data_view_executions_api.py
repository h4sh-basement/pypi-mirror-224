# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flywheel.api_client import ApiClient
import flywheel.models

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

class DataViewExecutionsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_view_execution(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Delete a data_view_execution

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param bool async_: Perform the request asynchronously
        :return: DeletedResult
        """
        ignore_simplified_return_value = kwargs.pop('_ignore_simplified_return_value', False)
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.delete_view_execution_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_view_execution_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
            if (
                data
                and hasattr(data, 'return_value')
                and not ignore_simplified_return_value
            ):
                return data.return_value()
            return data


    def delete_view_execution_with_http_info(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Delete a data_view_execution

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param bool async: Perform the request asynchronously
        :return: DeletedResult
        """

        all_params = ['data_view_execution_id',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_view_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_view_execution_id' is set
        if ('data_view_execution_id' not in params or
                params['data_view_execution_id'] is None):
            raise ValueError("Missing the required parameter `data_view_execution_id` when calling `delete_view_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_execution_id' in params:
            path_params['data_view_execution_id'] = params['data_view_execution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/data_view_executions/{data_view_execution_id}/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedResult',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_all_data_view_executions(self, **kwargs):  # noqa: E501
        """Get a list of data_view_executions

        This method makes a synchronous HTTP request by default.

        :param bool exhaustive: Set to return a complete list regardless of permissions
        :param str filter: The filter to apply. (e.g. label=my-label,created>2018-09-22)
        :param str sort: The sort fields and order. (e.g. label:asc,created:desc)
        :param int limit: The maximum number of entries to return.
        :param int skip: The number of entries to skip.
        :param int page: The page number (i.e. skip limit*page entries)
        :param str after_id: Paginate after the given id. (Cannot be used with sort, page or skip)
        :param list[str] x_accept_feature:
        :param bool async_: Perform the request asynchronously
        :return: union[Page,list[DataViewExecution]]
        """
        ignore_simplified_return_value = kwargs.pop('_ignore_simplified_return_value', False)
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.get_all_data_view_executions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_data_view_executions_with_http_info(**kwargs)  # noqa: E501
            if (
                data
                and hasattr(data, 'return_value')
                and not ignore_simplified_return_value
            ):
                return data.return_value()
            return data


    def get_all_data_view_executions_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of data_view_executions

        This method makes a synchronous HTTP request by default.

        :param bool exhaustive: Set to return a complete list regardless of permissions
        :param str filter: The filter to apply. (e.g. label=my-label,created>2018-09-22)
        :param str sort: The sort fields and order. (e.g. label:asc,created:desc)
        :param int limit: The maximum number of entries to return.
        :param int skip: The number of entries to skip.
        :param int page: The page number (i.e. skip limit*page entries)
        :param str after_id: Paginate after the given id. (Cannot be used with sort, page or skip)
        :param list[str] x_accept_feature:
        :param bool async: Perform the request asynchronously
        :return: union[Page,list[DataViewExecution]]
        """

        all_params = ['exhaustive','filter','sort','limit','skip','page','after_id','x_accept_feature',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_data_view_executions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exhaustive' in params:
            query_params.append(('exhaustive', params['exhaustive']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'after_id' in params:
            query_params.append(('after_id', params['after_id']))  # noqa: E501

        header_params = {}
        if 'x_accept_feature' in params:
            header_params['x-accept-feature'] = params['x_accept_feature']  # noqa: E501
            collection_formats['x-accept-feature'] = ''  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/data_view_executions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='union[Page,list[DataViewExecution]]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_data_view_execution(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Get a single data_view_execution

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param bool async_: Perform the request asynchronously
        :return: DataViewExecution
        """
        ignore_simplified_return_value = kwargs.pop('_ignore_simplified_return_value', False)
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.get_data_view_execution_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_data_view_execution_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
            if (
                data
                and hasattr(data, 'return_value')
                and not ignore_simplified_return_value
            ):
                return data.return_value()
            return data


    def get_data_view_execution_with_http_info(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Get a single data_view_execution

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param bool async: Perform the request asynchronously
        :return: DataViewExecution
        """

        all_params = ['data_view_execution_id',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_view_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_view_execution_id' is set
        if ('data_view_execution_id' not in params or
                params['data_view_execution_id'] is None):
            raise ValueError("Missing the required parameter `data_view_execution_id` when calling `get_data_view_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_execution_id' in params:
            path_params['data_view_execution_id'] = params['data_view_execution_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/data_view_executions/{data_view_execution_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataViewExecution',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_data_view_execution_data(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Get the data from a data_view_execution

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param str ticket: download ticket id
        :param str file_format:
        :param str file_name: download ticket filename
        :param bool async_: Perform the request asynchronously
        :return: None
        """
        ignore_simplified_return_value = kwargs.pop('_ignore_simplified_return_value', False)
        kwargs['_return_http_data_only'] = True
        kwargs['_preload_content'] = False

        if kwargs.get('async_'):
            return self.get_data_view_execution_data_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_data_view_execution_data_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
            if (
                data
                and hasattr(data, 'return_value')
                and not ignore_simplified_return_value
            ):
                return data.return_value()
            return data


    def get_data_view_execution_data_with_http_info(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Get the data from a data_view_execution

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param str ticket: download ticket id
        :param str file_format:
        :param str file_name: download ticket filename
        :param bool async: Perform the request asynchronously
        :return: None
        """

        all_params = ['data_view_execution_id','ticket','file_format','file_name',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_view_execution_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_view_execution_id' is set
        if ('data_view_execution_id' not in params or
                params['data_view_execution_id'] is None):
            raise ValueError("Missing the required parameter `data_view_execution_id` when calling `get_data_view_execution_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_execution_id' in params:
            path_params['data_view_execution_id'] = params['data_view_execution_id']  # noqa: E501

        query_params = []
        if 'ticket' in params:
            query_params.append(('ticket', params['ticket']))  # noqa: E501
        if 'file_format' in params:
            query_params.append(('file_format', params['file_format']))  # noqa: E501
        if 'file_name' in params:
            query_params.append(('file_name', params['file_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/data_view_executions/{data_view_execution_id}/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def save_data_view_execution(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Save a data_view_execution to a project

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param str file_format:
        :param bool async_: Perform the request asynchronously
        :return: FileEntry
        """
        ignore_simplified_return_value = kwargs.pop('_ignore_simplified_return_value', False)
        kwargs['_return_http_data_only'] = True

        if kwargs.get('async_'):
            return self.save_data_view_execution_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.save_data_view_execution_with_http_info(data_view_execution_id, **kwargs)  # noqa: E501
            if (
                data
                and hasattr(data, 'return_value')
                and not ignore_simplified_return_value
            ):
                return data.return_value()
            return data


    def save_data_view_execution_with_http_info(self, data_view_execution_id, **kwargs):  # noqa: E501
        """Save a data_view_execution to a project

        This method makes a synchronous HTTP request by default.

        :param str data_view_execution_id: (required)
        :param str file_format:
        :param bool async: Perform the request asynchronously
        :return: FileEntry
        """

        all_params = ['data_view_execution_id','file_format',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_data_view_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_view_execution_id' is set
        if ('data_view_execution_id' not in params or
                params['data_view_execution_id'] is None):
            raise ValueError("Missing the required parameter `data_view_execution_id` when calling `save_data_view_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_view_execution_id' in params:
            path_params['DataViewExecutionId'] = params['data_view_execution_id']  # noqa: E501

        query_params = []
        if 'file_format' in params:
            query_params.append(('file_format', params['file_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/data_view_executions/{DataViewExecutionId}/save', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)
