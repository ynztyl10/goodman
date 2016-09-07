# coding=utf-8
import logging
from lib.memcache import Client
logger = logging.getLogger(__file__)



class MemcacheAgent(object):

    def __init__(self, config):
        con_str = "%s:%s" % (config.get('host','127.0.0.1'), config.get('port',11211))
        self.client = Client([con_str], debug=0)

    def init(self):
        pass


    def do_transaction(self, action):
        command = action['command']
        value_list = action['data'].split()
        logger.debug(value_list)
        res = getattr(self.client,command)(*value_list)
        if not res:
            return False
        return res

    def destory(self):
        pass


