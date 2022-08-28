"""其它接口"""
import json

from fastapi import APIRouter

from example_pkg.MySQL.mysqlconfig import getschema
from example_pkg.Redis import RedisModel
from example_pkg.click_house import databases
from example_pkg.port_code.otherformat import formatSchema, makesql

other_operate = APIRouter()

'''查询接口'''


@other_operate.post('./query')
async def select(dataSetId: int, cache: bool, whereList: list, groupByList: list, sort: list):  # selectList: list,
    dataset = getschema(dataSetId)
    dbName = dataset[0]['db_name']
    tableName = dataset[0]['table_name']
    dataSourceType = dataset[0]['data_source_type']
    user_data = json.loads(RedisModel().get_data("user_data").get("result"))
    if dataSourceType == user_data.get("dataSourceType"):
        try:
            host = user_data.get('host')
            port = user_data.get('port')
            password = user_data.get('password')
            user = user_data.get('user')
            clients = databases(host=host, port=port, user=user, password=password)
            schema_list = formatSchema(dataset)
            sql = makesql(schemes_list=schema_list, dbname=dbName, tablename=tableName, whereList=whereList, groupByList=groupByList, sort=sort)
            all_data = {}
            for i in schema_list:
                name = i['name']
                data = clients.Gettabledata(schema=name, database=dbName, table=tableName)
                all_data[name] = data
            if cache:
                RedisModel().set_data("dataset", json.dumps(all_data))
            return all_data
        except:
            pass
