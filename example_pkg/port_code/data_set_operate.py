"""数据集操作接口"""
import datetime
import json

import random
import time

from fastapi import APIRouter
from example_pkg.Redis import RedisModel
from example_pkg.click_house import databases
from example_pkg.modules import Response

dbs_operate = APIRouter()

'''创建数据集
name:数据集名称,
descr:数据集描述, 
dataSourceType:数据源类型, 
dbName:数据库名, 
tableName:数据表名，
schema:数据集, 
createUser:创建用户
'''


@dbs_operate.post('./dataset/create')
async def create_dataset(name: str, descr: str, dataSourceType: str, dbName: str, tableName: str, schema: list,
                         createUser: str):
    # schema = [{'name': 'index'}, {"name": 'ts_code'}]
    user_data = json.loads(RedisModel().get_data("user_data").get("result"))
    cachedata = {}
    # dataset_list = []
    if dataSourceType == user_data.get("dataSourceType"):
        try:
            host = user_data.get('host')
            port = user_data.get('port')
            password = user_data.get('password')
            user = user_data.get('user')
            clients = databases(host=host, port=port, user=user, password=password)
            # for i in schema:
            #     schemas = i['name']
            #     tabledatas = clients.Gettabledata(database=dbName, table=tableName, schema=schemas)
            #     dataset_list.append(tabledatas)
            cachedata['id'] = random.randrange(0, 100)
            # cachedata['app_ip'] = random.randrange(0, 100)
            cachedata['app_ip'] = 1
            cachedata['name'] = name
            cachedata['descr'] = descr
            cachedata['data_source_type'] = dataSourceType
            cachedata['db_name'] = dbName
            # cachedata['schema'] = dataset_list
            cachedata['schema'] = schema
            cachedata['create_user'] = createUser
            cachedata['update_user'] = None
            cachedata['create_time'] = time.strftime("%Y-%m-%d %X")
            cachedata['staus'] = 0
            RedisModel().set_data(cachedata['app_ip'], json.dumps(cachedata))
            return Response(data={'dataSetId': cachedata['app_ip']}, msg='success', code=0).return_response()
        except:
            return Response(data=None, msg='fail', code=110).return_response()


'''数据集列表
orderBy:排列字段, 
order:排列方式, 
page:页数, 
pageSize:页大小, 
creatUser:创建用户, 
keyword:数据集名称或数据集descr关键字搜索
'''


@dbs_operate.post('./list')
async def dataset_list(orderBy: str, order: str, page: int, pageSize: int, creatUser: str, keyword: str):
    pass


"""数据集删除"""


@dbs_operate.post('./delete')
async def delete_dataset(id: int):
    pass


"""数据集信息"""


@dbs_operate.post('./info')
async def info_dataset(dataSetId: int):
    pass
