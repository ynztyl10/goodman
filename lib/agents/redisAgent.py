# coding=utf-8
import redis

# config = {
#     "host":"127.0.0.1",
#     "port":6379
# }

# action = {
#     "command" : "get",
#     "data" : "test"
# }

class RedisAgent(object):

    def __init__(self, config):
        self.client = redis.StrictRedis(host=config['host'], port=int(config['port']), db=0, password=config.get('passwd',None))


    def init(self):
        pass


    def do_transaction(self, action):
        command = action['command']
        value_list = action['data'].split()
        res = getattr(self.client,command)(*value_list)
        if not res:
            return False
        return res

    def destory(self):
        pass

# if __name__ == '__main__':
#     r = RedisAgent(config)
#     print r.do_transaction(action)
