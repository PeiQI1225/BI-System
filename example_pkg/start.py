
import time

from typing import Optional, List
from starlette.responses import RedirectResponse
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header
from port_code import database_operate, data_set_operate, other_operate

BI_system = FastAPI(
    title='简易BI系统实现',
    description='BI系统',
    version='1.0.0',
    docs_url='/docs',   # 测试页面
    redoc_url='/redocs',
)


BI_system.middleware('http')


BI_system.add_middleware(
    CORSMiddleware,
    allow_origins=[  # 应该允许进行跨域请求的来源列表,可以用’*’来允许任何来源
        '*'
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
BI_system.include_router(database_operate.db_operate, prefix='/api/v1', tags=['数据库操作'])
BI_system.include_router(data_set_operate.dbs_operate, prefix="/api/v1/dataset", tags=["数据集操作"])
BI_system.include_router(other_operate.other_operate, prefix='/api/v1', tags=['其它操作'])


if __name__ == '__main__':
    uvicorn.run('start:BI_system', host='127.0.0.1', port=8001, reload=True, debug=1, workers=1)
