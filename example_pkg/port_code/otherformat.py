"""schema数据格式化"""


def formatSchema(schema):
    schema = schema[0]
    schema_str = schema['schema_data']
    schema_list = eval(schema_str)
    return schema_list


def makesql(schemes_list, dbname, tablename, whereList, groupByList, sort):
    scheme_list = []
    for i in schemes_list:
        scheme_list.append(i["name"])
    schema = ",".join(scheme_list)
    whereList = [str(k) for k in list(whereList[0].values())]
    where = " ".join(whereList)
    group = ",".join(groupByList)
    sort_list = []
    for j in sort:
        sort_list.append(list(j.values()))
    sortstr = ",".join(str(k) for k in sort_list[0])
    sql = f"select {schema} from {dbname}.{tablename} where {where} group by {group} order  by {sortstr}"
    return sql


#
# schema_list = [{"name": "index", "type": "str", "descr": "", "isPartition": True},
#                {"name": "ts_code", "isPartition": False},
#                {"name": "close", "type": "str", "descr": "", "isPartition": True},
#                {"name": "vol", "isPartition": False}]
# whereList = [{"field": "ts_code", "op": "in", "valueList": ["FRA40.FXCM", "US30.FXCM"]}]
# groupByList = [" "]
# sort = [{"field": "vol", "order": "desc"}]
# makesql(schema_list, "dbup", "cfd_stocks", whereList, groupByList, sort)
