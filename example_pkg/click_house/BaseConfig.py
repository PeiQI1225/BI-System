from clickhouse_driver import Client
from example_pkg.Redis.redisService import RedisModel


class client:
    def __init__(self, host, password, user, port):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.client = Client(host=self.host, port=self.port, user=self.user, password=self.password)
    # def connect(self):
    #     """
    #     clickhouse连接：
    #     host：主机
    #     port：端口（默认端口：8123）
    #     user：用户名（默认原始用户default)
    #     passwd：密码
    #     连接成功后返回连接中所有的数据库
    #     """
    #
    #     sql = 'show databases'
    #     database = client.execute(sql)
    #     return database


class databases(client):
    def __init__(self, host, password, user='default', port=9000):
        super().__init__(host, password, user, port)

    def GetDatabase(self):
        # client = Client(host=self.host, port=self.port, user=self.user, password=self.password)
        sql = 'show databases'
        databases = self.client.execute(sql)
        return databases

    def GetTable(self, database):
        # client = Client(host=self.host, port=self.port, user=self.user, password=self.password)
        sql = f'show tables in {database}'
        tables = self.client.execute(sql)
        return tables

    def Getschema(self, database, table):
        # client = Client(host=self.host, port=self.port, user=self.user, password=self.password)
        sql = f"select name,type,comment from system.columns where database='{database}' and table='{table}'"
        # sql = f"select partition  from system.parts WHERE table='cfd_stocks'"
        schemalist = self.client.execute(sql)
        datalist = []
        for i in schemalist:
            i = list(i)
            schema = {}
            schema['name'] = i[0]
            schema['type'] = i[1]
            schema['descr'] = i[2]
            if i[0] in self.client.execute(f"select partition  from system.parts WHERE table='{table}'"):
                schema['ispartition'] = True
            else:
                schema['ispartition'] = False
            datalist.append(schema)
        return datalist

    def Gettabledata(self, database, table, schema):
        sql = f"select {schema} From {database}.{table}"
        tabledata = self.client.execute(sql)
        return tabledata

#
# a = databases(host="139.224.74.8", port=9000, user="default", password="2001G1225")
# print(a.Getschema(database='dbup', table='check'))
# a.Gettabledata(database='dbup', table='cfd_stocks')
# clients = client(host="139.224.74.8", port=9000, user="default", password="2001G1225", )
# print(clients.connect())
# create table dbup.visits(userid int,visitdate date,website String) engine=MergeTree() PARTITION BY toYYYYMM(visitdate) order by userid;
