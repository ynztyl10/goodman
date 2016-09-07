# coding=utf-8

from lib.constants import *
from controllers.errorCtrl import ErrorCtrl
from lib.agents.mysqlAgent import MysqlAgent
from lib.agents.redisAgent import RedisAgent
from lib.agents.memcacheAgent import MemcacheAgent
from lib.exceptions import UnSupportedEngineException

        


class AgentCtrl(object):
    """docstring for AgentCtrl"""

    agents = {
        "mysql": MysqlAgent,
        "redis": RedisAgent,
        "memcache": MemcacheAgent
    }

    def __init__(self, config):
        agentHandler = self.agents.get(config['engine'], "")
        if not agentHandler:
            raise UnSupportedEngineException
        self.agent = agentHandler(config)

    def process(self, action):
        self.agent.init()
        res = self.agent.do_transaction(action)
        self.agent.destory()
        return res








