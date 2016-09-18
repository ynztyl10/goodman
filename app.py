# coding=utf-8
import os

from tornado import ioloop, web
import logging
from tornado.escape import json_encode, json_decode


from apps.proxy import ProxyHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='app.log',
                    filemode='a')
   
                                    
settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True
}


application = web.Application([
    (r'/proxy', ProxyHandler),
], **settings)

if __name__ == "__main__":
    application.listen(9090)
    ioloop.IOLoop.instance().start()
