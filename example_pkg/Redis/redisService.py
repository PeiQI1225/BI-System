import json

from .Redis_Config import Strict_Redis

import redis


class RedisDBConfig:
    HOST = '127.0.0.1'
    PORT = 6379
    DBID = 1


def operator_status(func):
    """get operatoration status
    """

    def gen_status(*args, **kwargs):
        error, result = None, None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            error = str(e)

        return {'result': result, 'error': error}

    return gen_status


class RedisModel(object):
    def __init__(self):
        if not hasattr(RedisModel, 'pool'):
            RedisModel.create_pool()
        self._connection = redis.Redis(connection_pool=RedisModel.pool)

    # python中，所有类的实例中的成员变量，都是公用一个内存地址，因此，及时实例化多个RedisCache类，内存中存在的pool也只有一个
    @staticmethod
    def create_pool():
        RedisModel.pool = redis.ConnectionPool(
            host=RedisDBConfig.HOST,
            port=RedisDBConfig.PORT,
            db=RedisDBConfig.DBID)

    @operator_status
    def set_data(self, key, value):
        """set data with (key, value)
        """
        self._connection.set(key, value)

    @operator_status
    def get_data(self, key):
        """get data by key
        """
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        """delete cache by key
        """
        self._connection.delete(key)
