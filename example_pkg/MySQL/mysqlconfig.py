import pymysql
from DBUtils.PooledDB import PooledDB


class MysqlServer():
    def __init__(self):
        self.maxusage = None
        self.host = '127.0.0.1'
        self.user = 'root'
        self.passwd = 'root'
        self.db = "bi_system"
        self.port = 3306
        self.charset = "utf8"
        self.pool = PooledDB(pymysql, maxusage=self.maxusage, host=self.host, user=self.user,
                             passwd=self.passwd, db=self.db, port=self.port, charset=self.charset)


conn = MysqlServer
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
