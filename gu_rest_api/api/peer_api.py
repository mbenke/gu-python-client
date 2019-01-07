# coding: utf-8

"""
    Golem unlimited low level hub API

    API description in Markdown.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gu_rest_api.api_client import ApiClient


class PeerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_deployment(self, node_id, deployment_spec, **kwargs):  # noqa: E501
        """create_deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_deployment(node_id, deployment_spec, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :param DeploymentSpec deployment_spec: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_deployment_with_http_info(node_id, deployment_spec, **kwargs)  # noqa: E501
        else:
            (data) = self.create_deployment_with_http_info(node_id, deployment_spec, **kwargs)  # noqa: E501
            return data

    def create_deployment_with_http_info(self, node_id, deployment_spec, **kwargs):  # noqa: E501
        """create_deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_deployment_with_http_info(node_id, deployment_spec, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :param DeploymentSpec deployment_spec: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['node_id', 'deployment_spec']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_deployment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in local_var_params or
                local_var_params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `create_deployment`")  # noqa: E501
        # verify the required parameter 'deployment_spec' is set
        if ('deployment_spec' not in local_var_params or
                local_var_params['deployment_spec'] is None):
            raise ValueError("Missing the required parameter `deployment_spec` when calling `create_deployment`")  # noqa: E501

        if 'node_id' in local_var_params and not re.search(r'0x[0-9a-f]{40}', local_var_params['node_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `node_id` when calling `create_deployment`, must conform to the pattern `/0x[0-9a-f]{40}/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'deployment_spec' in local_var_params:
            body_params = local_var_params['deployment_spec']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/peers/{nodeId}/deployments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_peer_details(self, node_id, **kwargs):  # noqa: E501
        """Returns detailed peer info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_peer_details(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :return: PeerDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_peer_details_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_peer_details_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def get_peer_details_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """Returns detailed peer info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_peer_details_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :return: PeerDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['node_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_peer_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in local_var_params or
                local_var_params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `get_peer_details`")  # noqa: E501

        if 'node_id' in local_var_params and not re.search(r'0x[0-9a-f]{40}', local_var_params['node_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `node_id` when calling `get_peer_details`, must conform to the pattern `/0x[0-9a-f]{40}/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/peers/{nodeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PeerDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_deployments(self, node_id, **kwargs):  # noqa: E501
        """list_deployments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_deployments(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :return: list[DeploymentInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_deployments_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_deployments_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def list_deployments_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """list_deployments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_deployments_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :return: list[DeploymentInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['node_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_deployments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in local_var_params or
                local_var_params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `list_deployments`")  # noqa: E501

        if 'node_id' in local_var_params and not re.search(r'0x[0-9a-f]{40}', local_var_params['node_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `node_id` when calling `list_deployments`, must conform to the pattern `/0x[0-9a-f]{40}/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/peers/{nodeId}/deployments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeploymentInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_peers(self, **kwargs):  # noqa: E501
        """Returns a list hub peers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_peers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: list[PeerInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_peers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_peers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_peers_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list hub peers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_peers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: list[PeerInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_peers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/peers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PeerInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_deployment(self, node_id, deployment_id, **kwargs):  # noqa: E501
        """update_deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_deployment(node_id, deployment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :param str deployment_id: (required)
        :param list[Command] command:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_deployment_with_http_info(node_id, deployment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_deployment_with_http_info(node_id, deployment_id, **kwargs)  # noqa: E501
            return data

    def update_deployment_with_http_info(self, node_id, deployment_id, **kwargs):  # noqa: E501
        """update_deployment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_deployment_with_http_info(node_id, deployment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: GU Network node identifier (required)
        :param str deployment_id: (required)
        :param list[Command] command:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['node_id', 'deployment_id', 'command']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_deployment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in local_var_params or
                local_var_params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `update_deployment`")  # noqa: E501
        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in local_var_params or
                local_var_params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `update_deployment`")  # noqa: E501

        if 'node_id' in local_var_params and not re.search(r'0x[0-9a-f]{40}', local_var_params['node_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `node_id` when calling `update_deployment`, must conform to the pattern `/0x[0-9a-f]{40}/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501
        if 'deployment_id' in local_var_params:
            path_params['deploymentId'] = local_var_params['deployment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'command' in local_var_params:
            body_params = local_var_params['command']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['serviceToken', 'systemName']  # noqa: E501

        return self.api_client.call_api(
            '/peers/{nodeId}/deployments/{deploymentId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
