"""数据库操作相关接口"""

from fastapi import APIRouter
from clickhouse_driver import Client
from clickhouse.BaseConfig import client


db_operate = APIRouter()

'''数据源接口'''


@db_operate.post('.datasource/list')
async def data_source():
    pass


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
