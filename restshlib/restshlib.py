#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import copy
import shlex

DEFAULT_SETTINGS = {
    'print_request': "no",
    'print_body': "yes",
    'print_headers': "no",
    'print_status': "no",
    'auth_method': "basic",
}

class RestSHLib():
    base_url = ""
    headers = {}
    settings = DEFAULT_SETTINGS
    auth = None

    def __init__(self, base_url="", global_data={}):
        self.base_url = base_url
        self.g_data = global_data

    def parse_user_data(self, data):
        """
        Parse user data. 

        This method receives a list of user parameters splitted by shlex.
        If length of data is 1 and starts with dict, restshlib automatic
        eval the content of this argument. Example::
            
            post http://url "dict({'foo': 1})"
        
        Else, try parse key value like this::
            
            post http://url key=value keyN=valueN
        """

        try:
            result = eval(data, copy.deepcopy(self.g_data))
            if not isinstance(result, (str, unicode, bytes, dict)):
                raise ValueError("Invalid parameters")
            return result

        except (SyntaxError) as e:
            data = shlex.split(data)

            if len(data) == 0:
                return {}

            dict_data = {}
            for _part in data:
                try:
                    key, value = _part.split("=", 1)
                except ValueError as e:
                    raise ValueError("Invalid parameters")

                dict_data[key] = value

            return dict_data
            
    def post(self, url, data):
        return requests.post(
            self.base_url + url,
            data = self.parse_user_data(data),
            headers = self.headers,
            auth = self.auth
        ) 

    def put(self, url, data):
        return requests.put(
            self.base_url + url,
            data = self.parse_user_data(data),
            headers = self.headers,
            auth = self.auth
        )

    def get(self, url, data):
        return requests.get(
            self.base_url + url,
            headers = self.headers,
            auth = self.auth,
            params = self.parse_user_data(data),
        )

    def delete(self, url, data):
        return requests.delete(
            self.base_url + url,
            headers = self.headers,
            auth = self.auth,
            params = self.parse_user_data(data),
        )

    def set_header(self, key, value):
        self.headers[key] = value

    def unset_header(self, key):
        self.headers.pop(key)

    def set_setting(self, key, value):
        self.settings[key] = value

    def unset_setting(self, key):
        self.settings.pop(key)

    def set_base_url(self, base_url):
        self.base_url = base_url

    def set_auth(self, username, password, typ="basic"):
        if typ == "basic":
            self.auth = HTTPBasicAuth(username, password)
        elif typ == "digest":
            self.auth = HTTPDigestAuth(username, password)

    def unset_header(self, key):
        self.headers.pop(key)
