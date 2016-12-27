#coding=utf-8

from tornado import web,escape
import logging
import json
from bson import json_util
from lib.constants import *
from lib.exceptions import UnSupportedEngineException
from controllers.errorCtrl import ErrorCtrl
from controllers.agentCtrl import AgentCtrl

logger = logging.getLogger(__file__)


class ProxyHandler(web.RequestHandler):
    
    def set_crx_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS, GET,DELETE')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
        self.set_header("Content-Type", "application/json")

    def return_err(self,errno):
        logger.warning('errno:%d',errno)
        res = ErrorCtrl.get_error(errno)
        return self.write(json.dumps((res),default=json_util.default))

    def post(self):
        self.set_crx_headers()
        if not self.request.body:
            logger.warning("request body is null!")
            self.return_err(PARAMS_NULL)
        data = self.get_argument('data','')
        if not data:
            logger.warning("data params is null!")
            self.return_err(PARAMS_NULL)
        data_json = escape.json_decode(data)
        check_res = self.params_check(data_json,['config','action'])
        if not check_res:
            logger.warning("config or action params is null!")
            self.return_err(PARAMS_NULL)
        config = data_json['config']
        action = data_json['action']
        try:
            agent_ctrl = AgentCtrl(config)
            res = agent_ctrl.process(action)
            res = {"errno" : SUCCESS,"data": res}
            return self.write(json.dumps((res),default=json_util.default))
        except UnSupportedEngineException,e:
            logger.warning(e)
            self.return_err(ENGINE_NOT_SUPPORT)
        



    def params_check(self,data,check_params):
        out = False
        if not check_params or not data:
            return out
        for item in check_params:
            if not data.has_key(item):
                return out
        return True




