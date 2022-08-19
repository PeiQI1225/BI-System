from clickhouse_driver import Client


class client:
    def __init__(self, host, password, user='default', port=8123):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        """
        clickhouse连接：
        host：主机
        port：端口（默认端口：8123）
        user：用户名（默认原始用户default)
        passwd：密码
        连接成功后返回连接中所有的数据库
        """
        client = Client(host=self.host, port=self.port, user=self.user, password=self.password)
        sql = 'show databases'
        res = client.execute(sql)
        return res


class database(client):
    def __init__(self, database):
        self.database = database

    def GetDatabase(self):
        pass


clients = client(host="139.224.74.8", port=9000, user="default", password="2001G1225")
