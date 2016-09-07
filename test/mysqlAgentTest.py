#coding=utf-8

import unittest
from lib.agents.mysqlAgent import MysqlAgent

class MysqlAgentTest(unittest.TestCase):
    """docstring for MysqlAgentTest"""
    config = {
        "engine": "mysql",
        "host": "127.0.0.1",
        "port": 3306,
        "user": "puppy",
        "passwd": "puppy",
        "schema": "web_monitor"
    }
    action = {
        "command": "select",
        "data": "select * from tb_i_task limit 2"
    }
    def setUp(self):
        self.agent = MysqlAgent(self.config)

    def testSelect(self):
        res = self.agent.do_transaction(self.action)
        self.assertEqual(2,len(res))


if __name__ == '__main__':
    unittest.main()

        