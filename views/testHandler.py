#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2017/10/16 17:39
 @Author  : jyq
 @Software: PyCharm
 @Description:
"""
from views.base import BaseHandler


class TestHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.write("123123123123123")