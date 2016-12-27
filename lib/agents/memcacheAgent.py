# coding=utf-8
import logging
from lib.memcache import Client
import phpserialize as phpse
import json
logger = logging.getLogger(__file__)



class MemcacheAgent(object):

    storage_commands = ['set','add','replace']
    del_commands = ['delete']
    retrieval_commands = ['get','gets']

    def __init__(self, config):
        con_str = "%s:%s" % (config.get('host','127.0.0.1'), config.get('port',11211))
        self.client = Client([con_str], debug=0)

    def init(self):
        pass


    def do_transaction(self, action):
        command = action['command']
        value_list = action['data'].split()
        logger.debug(value_list)
        value_list = self.format(command,value_list)
        try:
            res = getattr(self.client,command)(*value_list)
            if not res:
                return False
            out = self.format(command,res)
            logger.debug(out)
            return out
        except Exception,e:
            return {"error":str(e)}
        

    def format(self,command,value_list):
        if command in self.storage_commands:
            return self.format_storage_commands(value_list)
        elif command in self.retrieval_commands:
            return self.format_retrieval_commands(value_list)
        elif command in self.del_commands:
            return self.format_del_commands(value_list)
        return value_list

    def format_retrieval_commands(self,data):
        if not data:
            return data
        try:
            return phpse.loads(data)
        except Exception, e:
            logger.warning(e)
            return data

    def format_del_commands(self,data):
        return data

    def format_storage_commands(self,value):
        if not isinstance(value,list):
            return self.format_storage_commands_str(value)
        else:
            return self.format_storage_commands_list(value)
    
    def format_storage_commands_str(self,value):
        return value;

    def format_storage_commands_list(self,value_list):
        try:
            json_data = json.loads(value_list[-1])
            phpse_data = phpse.dumps(json_data)
            value_list[-1] = phpse_data
            return value_list
        except Exception, e:
            logger.warning(e)
            return value_list


    def destory(self):
        pass


