"""数据集操作接口"""

import json

from fastapi import APIRouter

from example_pkg.MySQL.mysqlconfig import insertdata, getdataSetList, gettotalCount, deletedataSet, getschema
from example_pkg.Redis import RedisModel
from example_pkg.click_house import databases
from example_pkg.modules import Response
from example_pkg.port_code.otherformat import formatSchema

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
async def create_dataset(name: str, descr: str, dataSourceType: str, dbName: str, tableName: str, schema,
                         createUser: str):
    try:
        dataSetId = insertdata(name=name, descr=descr, dataSourceType=dataSourceType, dbName=dbName,
                               tableName=tableName
                               , schema=schema, createUser=createUser)
        if dataSetId is not None:
            return Response(data={'dataSetId': dataSetId}).return_response()
        else:
            return Response(data=None, msg='fail', code=110).return_response()
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
    try:
        data = {}
        dataSetList = getdataSetList(orderBy=orderBy, order=order, page=page, pageSize=pageSize, creatUser=creatUser,
                                     keyword=keyword)
        totalCount = gettotalCount(creatUser=creatUser, keyword=keyword)
        data['dataSetList'] = dataSetList
        data['totalCount'] = totalCount
        return Response(data=data).return_response()
    except:
        return Response(data=None, msg='fail', code=110).return_response()


"""数据集删除"""


@dbs_operate.post('./delete')
async def delete_dataset(id: int):
    if deletedataSet(id=id):
        return Response(data=True).return_response()
    return Response(data=False, msg='fail', code=110).return_response()


"""数据集信息"""


@dbs_operate.post('./info')
async def info_dataset(dataSetId: int):
    try:
        data_list = getschema(dataSetId=dataSetId)
        schema_list = formatSchema(data_list)
        data = {}
        dimensionList = []
        metricList = []
        functionList = []
        for i in schema_list:
            if i['isPartition']:
                dimensionList.append(i)
            else:
                metricList.append(i)
        data['dimensionList'] = dimensionList
        data['metricList'] = metricList
        data['functionList'] = functionList
        return Response(data=data).return_response()
    except:
        return Response(data=False, msg='fail', code=110).return_response()
