"""数据集操作接口"""
from fastapi import APIRouter

dbs_operate = APIRouter()

'''创建数据集
name:数据集名称,
descr:数据集描述, 
dataSourceType:数据源类型, 
dbName:数据库名, 
schema:数据集, 
createUser:创建用户
'''


@dbs_operate.post('./dataset/create')
async def create_dataset(name: str, descr: str, dataSourceType: str, dbName: str, schema: list, createUser: str):
    pass


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
