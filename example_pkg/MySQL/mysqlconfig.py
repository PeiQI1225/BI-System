import json

import pymysql
import random
import time

# 创建数据库连接
config = {
    "host": 'localhost',  # 连接主机, 默认127.0.0.1
    "user": 'root',  # 用户名
    "passwd": 'root',  # 密码
    "port": 3306,  # 端口，默认为3306
    "db": 'bi_system',  # 数据库名称
    "charset": 'utf8',  # 字符编码
    "cursorclass": pymysql.cursors.DictCursor}

conn = pymysql.connect(**config)
# 生成游标对象 cursor
cursor = conn.cursor()


def insertdata(name: str, descr: str, dataSourceType: str, dbName: str, tableName: str, schema,
               createUser: str):
    app_id = random.randrange(1, 100)
    insert_time = time.mktime(time.localtime())
    sql = f"INSERT data_set VALUES(Null,{app_id},'{name}','{descr}','{dataSourceType}','{dbName}','{tableName}','{schema}','{createUser}',Null,{insert_time},Null,0);"
    try:
        cursor.execute(sql)
        sql = f'select id from data_set where name = "{name}" and descr="{descr}" and data_source_type="{dataSourceType}" and db_name="{dbName}" and table_name="{tableName}" and create_user="{createUser}" and create_time = {insert_time};'
        cursor.execute(sql)
        dataSetId = cursor.fetchall()[0]
        # 提交当前游标的全部操作
        conn.commit()
    except:
        conn.rollback()
        dataSetId = None
    # 查看更新后的结果
    return dataSetId


def getdataSetList(orderBy: str, order: str, page: int, pageSize: int, creatUser: str, keyword: str):
    try:
        sql = f"SELECT * FROM data_set where create_user = '{creatUser}' and descr like '%{keyword}%' or name like '%{keyword}%' order by {orderBy},{order} LIMIT {(page - 1) * pageSize},{pageSize}; "
        cursor.execute(sql)
        conn.commit()
        return cursor.fetchall()
    except:
        conn.rollback()
        return None


def gettotalCount(creatUser: str, keyword: str):
    try:
        sql = f"SELECT COUNT(*) FROM data_set where create_user = '{creatUser}' and descr like '%{keyword}%' or name like '%{keyword}%';"
        cursor.execute(sql)
        number = cursor.fetchall()
        count = number[0]['COUNT(*)']
        conn.commit()
        return count
    except:
        conn.rollback()
        return None


def deletedataSet(id: int):
    try:
        sql = f'DELETE FROM data_set WHERE id={id};'
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        conn.rollback()
        return False


def getschema(dataSetId):
    try:
        sql = f"select * from data_set where id = {dataSetId};"
        cursor.execute(sql)
        schema = cursor.fetchall()
        conn.commit()
    except:
        conn.rollback()
        schema = None
    # 查看更新后的结果
    return schema
