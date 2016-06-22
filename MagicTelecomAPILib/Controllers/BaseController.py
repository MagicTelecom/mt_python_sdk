# -*- coding: utf-8 -*-

"""
   MagicTelecomAPILib

   This file was automatically generated by APIMATIC BETA v2.0 on 06/22/2016
"""

from MagicTelecomAPILib.Http.RequestsClient import *
from MagicTelecomAPILib.APIException import APIException

class BaseController(object):

    """All controllers inherit from this base class. It manages shared HTTP clients and global API errors."""

    http_client = RequestsClient()

    def __init__(self, client):
        if client != None:
            self.http_client = client

    def validate_response(self, response):
        if response.status_code == 401:
            raise APIException("You are not authenticated", response.status_code, response.raw_body)
        elif response.status_code == 403:
            raise APIException("This action needs a valid WSSE header", response.status_code, response.raw_body)
        elif response.status_code == 400:
            raise APIException("Http bad request", response.status_code, response.raw_body)
        elif (response.status_code < 200) or (response.status_code > 206): #[200,206] = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.raw_body)