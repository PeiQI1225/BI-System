"""数据库操作相关接口"""

from fastapi import APIRouter
import json
from example_pkg.click_house import databases
from example_pkg.Redis import RedisModel
from .modules import Response

db_operate = APIRouter()

'''数据源接口
NetworkError:主机错误
ServerException：密码错误/用户名错误
SocketTimeoutError：端口错误
'''


@db_operate.post('.datasource/list')
async def data_source(host: str, port: int, user: str, password: str):
    try:
        databases(host=host, port=port, user=user, password=password)
        # clients = client(host=host, port=port, user=user, password=password)
        # clients.connect()
        response = Response(data={"dataSourceName": "ClickHouse", "dataSourceType": "click_house"}).return_response()
        user_data = {"host": host, "port": port, "user": user, "password": password, "dataSourceType": "click_house"}
        RedisModel().set_data("user_data", json.dumps(user_data))
        return response
    except:
        response = Response(data=None, msg='fail', code=110).return_response()
        return response


'''数据源下的数据库'''


@db_operate.post('.db/list')
async def get_database(dataSourType: str):
    user_data = json.loads(RedisModel().get_data("user_data").get("result"))
    if dataSourType == user_data.get("dataSourceType"):
        try:
            # 数据拆分
            host = user_data.get('host')
            port = user_data.get('port')
            password = user_data.get('password')
            user = user_data.get('user')
            clients = databases(host=host, port=port, user=user, password=password)
            database = clients.GetDatabase()
            response = Response(data=database).return_response()
            return response
        except:
            response = Response(data=None, msg='fail', code=110).return_response()
            return response


'''数据库下的表'''


@db_operate.post('.table/list')
async def get_list(dataSourType: str, dbName: str):
    user_data = json.loads(RedisModel().get_data("user_data").get("result"))
    if dataSourType == user_data.get("dataSourceType"):
        try:
            host = user_data.get('host')
            port = user_data.get('port')
            password = user_data.get('password')
            user = user_data.get('user')
            clients = databases(host=host, port=port, user=user, password=password)
            tables = clients.GetTable(dbName)
            response = Response(data=tables).return_response()
            return response
        except:
            response = Response(data=None, msg='fail', code=110).return_response()
            return response


'''表的schema'''


@db_operate.post('.table/schema')
async def table_schema(dataSourType: str, dbName: str, tableName):
    pass
