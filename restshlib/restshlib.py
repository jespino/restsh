#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

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

    def __init__(self, base_url=""):
        self.base_url = base_url

    def post(self, url, data):
        return requests.post(
                self.base_url+url,
                data=data,
                headers=self.headers,
                auth=self.auth
        )

    def put(self, url, data):
        return requests.put(
                self.base_url+url,
                data=data,
                headers=self.headers,
                auth=self.auth
        )

    def get(self, url):
        return requests.get(
                self.base_url+url,
                headers=self.headers,
                auth=self.auth
        )

    def delete(self, url):
        return requests.delete(
                self.base_url+url,
                headers=self.headers,
                auth=self.auth
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
