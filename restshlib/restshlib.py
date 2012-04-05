#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import urlparse
import urllib

class RestSH():
    base_url = ""
    headers = {}
    settings = {}

    def __init__(self, base_url=""):
        self.base_url = base_url

    def _prepare_connection(self, url):
        urlparts = urlparse.urlparse(self.base_url+url)
        if urlparts[0] == "https":
            conn = httplib.HTTPSConnection(urlparts[1])
        else:
            conn = httplib.HTTPConnection(urlparts[1])
        conn.set_debuglevel(self.settings.get('httplib_debuglevel', 0))
        rel_url = "%s?%s" % (urlparts[2], urlparts[4])
        return (conn, rel_url)

    def post(self, url, data):
        (conn, rel_url) = self._prepare_connection(url)
        conn.request("POST", rel_url, urllib.urlencode(data), self.headers)
        return conn.getresponse()

    def put(self, url, data):
        (conn, rel_url) = self._prepare_connection(url)
        conn.request("PUT", rel_url, urllib.urlencode(data), self.headers)
        return conn.getresponse()

    def get(self, url):
        (conn, rel_url) = self._prepare_connection(url)
        conn.request("GET", rel_url, None, self.headers)
        return conn.getresponse()

    def delete(self, url):
        (conn, rel_url) = self._prepare_connection(url)
        conn.request("DELETE", rel_url, None, self.headers)
        return conn.getresponse()

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
