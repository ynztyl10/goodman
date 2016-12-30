# coding=utf-8
import redis
import json
import logging
from lib.constants import DATA_SEPERATOR
# config = {
#     "host":"127.0.0.1",
#     "port":6379
# }

# action = {
#     "command" : "get",
#     "data" : "test"
# }
logger = logging.getLogger(__file__)
class RedisAgent(object):

    def __init__(self, config):
        self.client = redis.StrictRedis(host=config['host'], port=int(config['port']), db=0, password=config.get('passwd',None))


    def init(self):
        pass


    def do_transaction(self, action):
        command = action['command']
        key = action['data'].split(DATA_SEPERATOR)[0]
        values = " ".join(action['data'].split(DATA_SEPERATOR)[1:])
        value_list = self.format_values(key, values)
        res = getattr(self.client,command)(*value_list)
        if not res:
            return False
        return res

    def destory(self):
        pass

    def format_values(self, key, values):
        value_list = [key]
        try:
            value_json = json.loads(values)
            value_list.append(value_json)
        except Exception, e:
            logger.debug("not a json str, use split")
            value_list = value_list + values.split()
        return value_list
            

# if __name__ == '__main__':
#     r = RedisAgent(config)
#     print r.do_transaction(action)
