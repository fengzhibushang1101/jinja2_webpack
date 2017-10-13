#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2017/10/11 16:03
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""
import os
import sys
import traceback

from tornado import ioloop, web, options, httpserver
from lib.utils.logger_util import logger

import os
import sys
import traceback

from views.index import IndexHandler

if 'threading' in sys.modules:
    del sys.modules['threading']

from tornado import ioloop, web, options, httpserver
from lib.utils.logger_util import logger

SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(sys.argv[0]), "templates"),
    static_path=os.path.join(os.path.dirname(sys.argv[0]), "static"),
    cookie_secret="",
    login_url="/",
)

urls = [
    (r'/', IndexHandler),
]


options.define('port', default=9801, type=int)


def main():
    try:
        options.parse_command_line()
        port = options.options.port
        SETTINGS['PORT'] = port
        app = web.Application(
            handlers=urls, debug=True,
            **SETTINGS
        )
        server = httpserver.HTTPServer(app)
        server.listen(SETTINGS['PORT'])
        ioloop.IOLoop().instance().start()

    except Exception, e:
        print traceback.format_exc(e)
        logger.error(traceback.format_exc(e))

if __name__ == '__main__':
    print "http://localhost:9801/"
    logger.info("the server is going to start...")
    main()
