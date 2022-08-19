"""其它接口"""

from fastapi import APIRouter

other_operate = APIRouter()


'''查询接口'''


@other_operate.post('./query')
async def select(dataSetId: int, cache: bool, selectList: list, whereList: list, groupByList: list, sort: list):
    pass
