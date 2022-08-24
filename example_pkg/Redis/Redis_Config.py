import redis


class Strict_Redis:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 6379
        self.db = 1
        self.__connent = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    # def connent(self):
    #     return self.__connent
