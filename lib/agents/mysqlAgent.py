# coding=utf-8
import MySQLdb
from MySQLdb import converters
import itertools
import logging

logger = logging.getLogger(__file__)

class MysqlAgent(object):

    def __init__(self, config):
        logger.debug(config)
        conv = converters.conversions.copy()
        conv[246] = float    # convert decimals to floats
        conv[12] = str       # convert datetime to strings
        conv[10] = str       # convert date to strings
        self.connect = MySQLdb.connect(connect_timeout=20,host=config.get('host', '127.0.0.1'), port=int(config.get('port', 3306)), user=config.get(
            'user', 'root'), passwd=config.get('passwd', 'root'), db=config.get('schema', 'testdb'), charset=config.get('charset', 'utf8'), conv=conv)
        self.charset = config.get('charset', 'utf8')
    def init(self):
        pass

    def dict_fetchall(self, cursor):
        """Returns all rows from a cursor as a list of dicts"""
        desc = cursor.description
        return [dict(itertools.izip([col[0] for col in desc], row))
                for row in cursor.fetchall()]

    def do_transaction(self, action):
        try:
            logger.debug(action)
            with self.connect:
                self.cursor = self.connect.cursor()
                action['data'] = action['data'].encode('utf-8').decode(self.charset)
                res = self.cursor.execute(action['data'])
                if not res:
                    return False
                return self.dict_fetchall(self.cursor)
        except MySQLdb.Error, e:
            logger.debug(e)
            try:
                logger.warning("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            except IndexError:
                logger.warning("MySQL Error: %s" % str(e))
            finally:
                return {"error":str(e)}
        finally:
            self.connect.close()


    def destory(self):
        pass
