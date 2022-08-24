"""数据库操作相关接口"""

from fastapi import APIRouter
from clickhouse_driver import Client

from clickhouse import client

db_operate = APIRouter()

'''数据源接口
NetworkError:主机错误
ServerException：密码错误/用户名错误
SocketTimeoutError：端口错误
'''

response = {}


@db_operate.post('.datasource/list')
async def data_source(host: str, port: int, user: str, password: str):
    try:
        clients = client(host=host, port=port, user=user, password=password)
        clients.connect()
        response['data'] = [{"dataSourceName": "ClickHouse", "dataSourceType": "click_house"}]
        response['msg'] = 'success'
        response['code'] = 0
        return response
    except:
        response['data'] = None
        response['msg'] = '连接失败'
        response['code'] = 110
        return response


'''数据源下的数据库'''


@db_operate.post('.db/list')
async def get_database(dataSourType: str):
    pass


'''数据库下的表'''


@db_operate.post('.table/list')
async def get_list(dataSourType: str, dbName: str):
    pass


'''表的schema'''


@db_operate.post('.table/schema')
async def table_schema(dataSourType: str, dbName: str, tableName):
    pass
