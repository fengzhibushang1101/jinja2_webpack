#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2017/10/11 16:29
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""
from views.base import BaseHandler


class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        render_settings = {
            "name": "jyq"
        }
        self.render("index/index.html", **render_settings)