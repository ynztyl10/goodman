# coding=utf-8
import MySQLdb
from MySQLdb import converters
import itertools


class MysqlAgent(object):

    def __init__(self, config):
        conv = converters.conversions.copy()
        conv[246] = float    # convert decimals to floats
        conv[12] = str       # convert datetime to strings
        self.connect = MySQLdb.connect(connect_timeout=2,host=config.get('host', '127.0.0.1'), port=int(config.get('port', 3306)), user=config.get(
            'user', 'root'), passwd=config.get('passwd', 'root'), db=config.get('schema', 'testdb'), charset=config.get('charset', 'utf8'), conv=conv)

    def init(self):
        pass

    def dict_fetchall(self, cursor):
        """Returns all rows from a cursor as a list of dicts"""
        desc = cursor.description
        return [dict(itertools.izip([col[0] for col in desc], row))
                for row in cursor.fetchall()]

    def do_transaction(self, action):
        with self.connect:
            self.cursor = self.connect.cursor()
            try:
                res = self.cursor.execute(action['data'])
                if not res:
                    return False
                return self.dict_fetchall(self.cursor)
            except Exception,e:
                return {"error":e}

    def destory(self):
        pass
