#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2017/10/11 16:30
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""
import json
import random
import datetime
import functools
import urlparse
from urllib import urlencode
from string import digits, lowercase
from tornado.web import HTTPError
from tornado.escape import to_unicode
from torndsession.sessionhandler import SessionBaseHandler
from lib.utils.logger_util import logger


class BaseHandler(SessionBaseHandler):

    def get(self, *args, **kwargs):
        self.on_request()

    def post(self, *args, **kwargs):
        self.on_request()

    @property
    def params(self):
        return self._argument()

    @property
    def cookies(self):
        return self._cookies()

    def _argument(self):
        return self._flatten_arguments(self.request.arguments)

    def _cookies(self):
        cookies = dict()
        cookie_str = self.request.headers.get("Cookie")
        for cookie in cookie_str.split(";"):
            name, value = cookie.strip().split("=", 1)
            cookies[name] = value
        return cookies

    def on_request(self):
        logger.info(self.request.arguments)
        logger.info(self.request.full_url())
        logger.info(self.request.headers["X-Real-IP"])
        logger.info(self.session.get("user_id"))
        self.write_error(404)

    def statistic_access(self, user):
        pass

    def write_error(self, status_code, **kwargs):
        self.render({
            500: "500.html",
            403: "403.html",
            404: "404.html",
            400: "400.html",
            405: "405.html",
        }[status_code])

    @staticmethod
    def str_to_unicode(word):
        try:
            return to_unicode(word)
        except Exception, e:
            logger.info(e.message)
            return word.decode("unicode-escape")

    def _flatten_arguments(self, args):
        """
        去除请求中单值参数的数组结构

        """
        flattened = {}
        for key in args:
            if len(args[key]) == 1:
                flattened[key] = self.str_to_unicode(args[key][0])
            else:
                flattened[key] = [self.str_to_unicode(arg) for arg in args[key]]

        return flattened

    @staticmethod
    def random_string(length=16):
        """
        length: 随机数长度
        """
        chars = lowercase + digits
        return ''.join([random.choice(chars) for i in xrange(length)])

    def json_response(self, json_content):
        self.set_header("Cache-Control", "private")
        self.set_header("Date", datetime.datetime.now())
        self.set_header("Content-Type", "application/json;charset=utf-8")
        if type(json_content) == dict:
            json_content = json.dumps(json_content)
        self.write(json_content)


def authenticated(method):
    """Decorate methods with this to require that the user be logged in.

    If the user is not logged in, they will be redirected to the configured
    `login url <RequestHandler.get_login_url>`.

    If you configure a login url with a query parameter, Tornado will
    assume you know what you're doing and use it as-is.  If not, it
    will add a `next` parameter so the login page knows where to send
    you once you're logged in.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlparse.urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else:
                        next_url = self.request.uri
                    url += "?" + urlencode(dict(next=next_url))
                self.redirect(url)
                return
            raise HTTPError(403)
        else:
            self.statistic_access(self.current_user)
        return method(self, *args, **kwargs)
    return wrapper


def privilege_verifier(func):

    class_code = dict()

    def _allow_access(funcs, class_name):
        for i in funcs:
            if class_name in class_code[i]:
                return True
        return False

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        user = self.current_user
        class_name = self.__class__.__name__
        funcs = user.func.split(';') if user.func else [u'6']
        if u'0' in funcs or _allow_access(funcs, class_name):
            return func(self, *args, **kwargs)
        else:
            self.redirect('/')

    return wrapper
