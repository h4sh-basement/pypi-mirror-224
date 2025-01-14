# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.820
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid_notification.api_client import ApiClient
from lusid_notification.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid_notification.models.lusid_problem_details import LusidProblemDetails
from lusid_notification.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid_notification.models.manual_event import ManualEvent
from lusid_notification.models.manual_event_request import ManualEventRequest


class ManualEventApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def trigger_manual_event(self, manual_event_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.trigger_manual_event(manual_event_request, async_req=True)
        >>> result = thread.get()

        :param manual_event_request: The data required to trigger a manual event. (required)
        :type manual_event_request: ManualEventRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ManualEvent
        """
        kwargs['_return_http_data_only'] = True
        return self.trigger_manual_event_with_http_info(manual_event_request, **kwargs)  # noqa: E501

    def trigger_manual_event_with_http_info(self, manual_event_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.trigger_manual_event_with_http_info(manual_event_request, async_req=True)
        >>> result = thread.get()

        :param manual_event_request: The data required to trigger a manual event. (required)
        :type manual_event_request: ManualEventRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ManualEvent, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'manual_event_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_manual_event" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'manual_event_request' is set
        if self.api_client.client_side_validation and ('manual_event_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['manual_event_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `manual_event_request` when calling `trigger_manual_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'manual_event_request' in local_var_params:
            body_params = local_var_params['manual_event_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.1.820'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            201: "ManualEvent",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/manualevent', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
