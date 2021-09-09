#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/7 4:17 下午
# @Author : zhenyu lei
# @File : __init__.py.py
# @desc :

# 导入对象
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.v1 import api_v1  # 不同模块注册路由


def create_app():
    app = FastAPI(
        title="CharmCode.cn",
        description="https://www.charmcode.cn",
        version="0.1.1",
        docs_url="/api/v1/docs",  # 自定义文档地址
        openapi_url="/api/v1/openapi.json",  #
        redoc_url=None,  # 禁用redoc文档
    )

    origins = []

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    # 导入路由, 前缀设置
    app.include_router(
        api_v1,
        prefix="/api/v1/mall",
    )

    config = {
                'connections': {
                    # Dict format for connection
                    'default': {
                        'engine': 'tortoise.backends.asyncpg',
                        'credentials': {
                            'host': 'localhost',
                            'port': '5432',
                            'user': 'tortoise',
                            'password': 'qwerty123',
                            'database': 'test',
                        }
                    },
                    # Using a DB_URL string
                    'default': 'postgres://postgres:qwerty123@localhost:5432/events'
                },
                'apps': {
                    'models': {
                        'models': ['__main__'],
                        # If no default_connection specified, defaults to 'default'
                        'default_connection': 'default',
                    }
                }
            }
    # register_tortoise 同步方法
    register_tortoise(app, config=config)

    # 使用原生SQL查询或者插入
    # default = Tortoise.get_connection('defautl')
    # await default.execute_query_dict('select * from default');

    # 异常捕获
    # register_exception(app)

    # 跨域设置
    # register_cors(app)

    return app
