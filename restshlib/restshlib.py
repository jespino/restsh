#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import urlparse
import urllib

class RestSH():
    base_url = ""
    headers = {}

    def __init__(self, base_url=""):
        self.base_url = base_url

    def post(self, url, data):
        urlparts = urlparse.urlparse(self.base_url+url)
        conn = httplib.HTTPConnection(urlparts[1])
        rel_url = "%s?%s" % (urlparts[2], urlparts[4])
        conn.request("POST", rel_url, urllib.urlencode(data), self.headers)
        return conn.getresponse()

    def put(self, url, data):
        urlparts = urlparse.urlparse(self.base_url+url)
        conn = httplib.HTTPConnection(urlparts[1])
        rel_url = "%s?%s" % (urlparts[2], urlparts[4])
        conn.request("PUT", rel_url, urllib.urlencode(data), self.headers)
        return conn.getresponse()

    def get(self, url):
        urlparts = urlparse.urlparse(self.base_url+url)
        conn = httplib.HTTPConnection(urlparts[1])
        rel_url = "%s?%s" % (urlparts[2], urlparts[4])
        conn.request("GET", rel_url, None, self.headers)
        return conn.getresponse()

    def delete(self, url):
        urlparts = urlparse.urlparse(self.base_url+url)
        conn = httplib.HTTPConnection(urlparts[1])
        rel_url = "%s?%s" % (urlparts[2], urlparts[4])
        conn.request("DELETE", rel_url, None, self.headers)
        return conn.getresponse()

    def set_header(self, key, value):
        self.headers[key] = value

    def unset_header(self, key):
        self.headers.pop(key)

    def set_base_url(self, base_url):
        self.base_url = base_url
