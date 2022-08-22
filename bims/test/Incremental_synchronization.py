#!/usr/bin/env python3
# _*_ coding:utf8 _*_
 
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (DeleteRowsEvent,UpdateRowsEvent,WriteRowsEvent,)
import clickhouse_driver
import configparser
import os
 
configfile='repl.ini'
########## 配置文件repl.ini 操作 ##################
def create_configfile(configfile,log_file,log_pos):
  config = configparser.ConfigParser()
 
  if not os.path.exists(configfile):
    config['replinfo'] = {'log_file':log_file,'log_pos':str(log_pos)}
 
    with open(configfile,'w+') as f:
      config.write(f)
 
### repl.ini 写操作 ##################
def write_config(configfile,log_file,log_pos):
  config = configparser.ConfigParser()
  config.read(configfile)
 
  config.set('replinfo','log_file',log_file)
  config.set('replinfo','log_pos',str(log_pos))
 
  if os.path.exists(configfile):
    with open(configfile,'w+') as f:
      config.write(f)
  else:
    create_configfile(configfile)
 
### 配置文件repl.ini 读操作 ##################
def read_config(configfile):
  config = configparser.ConfigParser()
  config.read(configfile)
  # print(config['replinfo']['log_file'])
  # print(config['replinfo']['log_pos'])
  return (config['replinfo']['log_file'],int(config['replinfo']['log_pos']))
 
############# clickhouse 操作 ##################
def ops_clickhouse(db,table,sql):
  column_type_dic={}
  try:
    client = clickhouse_driver.Client(host='127.0.0.1',\
                     port=9000,\
                     user='default',\
                     password='clickhouse')
    # sql="select name,type from system.columns where database='{0}' and table='{1}'".format(db,table)
    client.execute(sql)
 
  except Exception as error:
    message = "获取clickhouse里面的字段类型错误. %s" % (error)
    # logger.error(message)
    print(message)
    exit(1)
 
MYSQL_SETTINGS = {'host':'127.0.0.1','port':13306,'user':'root','passwd':'Root@0101'}
only_events=(DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent)
def main():
  ## 每次重启时，读取上次同步的log_file,log_pos
  (log_file,log_pos) = read_config(configfile)
  # print(log_file+'|'+ str(log_pos))
  print('-----------------------------------------------------------------------------')
  stream = BinLogStreamReader(connection_settings=MYSQL_SETTINGS, resume_stream=True, blocking=True, \
                server_id=10,
                 only_tables='t_repl', only_schemas='test', \
                log_file=log_file,log_pos=log_pos, \
                only_events=only_events, \
                fail_on_table_metadata_unavailable=True, slave_heartbeat=10)
 
  try:
    for binlogevent in stream:
      for row in binlogevent.rows:
        ## delete操作
        if isinstance(binlogevent, DeleteRowsEvent):
          info = dict(row["values"].items())
          # print("DELETE FROM `%s`.`%s` WHERE %s = %s ;" %(binlogevent.schema ,binlogevent.table,binlogevent.primary_key,info[binlogevent.primary_key]) )
          # print("ALTER TABLE `%s`.`%s` DELETE WHERE %s = %s ;" %(binlogevent.schema ,binlogevent.table,binlogevent.primary_key,info[binlogevent.primary_key]) )
          sql="ALTER TABLE `%s`.`%s` DELETE WHERE %s = %s ;" %(binlogevent.schema ,binlogevent.table,binlogevent.primary_key,info[binlogevent.primary_key])
 
        ## update 操作
        elif isinstance(binlogevent, UpdateRowsEvent):
          info_before = dict(row["before_values"].items())
          info_after = dict(row["after_values"].items())
          # info_set = str(info_after).replace(":","=").replace("{","").replace("}","")
          info_set = str(info_after).replace(":", "=").replace("{", "").replace("}", "").replace("'","")
          # print("UPDATE `%s`.`%s` SET %s WHERE %s = %s ;"%(binlogevent.schema,binlogevent.table,info_set,binlogevent.primary_key,info_before[binlogevent.primary_key]  ) )
          # print("ALTER TABLE %s.%s UPDATE %s WHERE %s = %s ;"%(binlogevent.schema,binlogevent.table,info_set,binlogevent.primary_key,info_before[binlogevent.primary_key]  ) )
          sql = "ALTER TABLE %s.%s UPDATE %s WHERE %s = %s ;"%(binlogevent.schema,binlogevent.table,info_set,binlogevent.primary_key,info_before[binlogevent.primary_key]  )
 
        ## insert 操作
        elif isinstance(binlogevent, WriteRowsEvent):
          info = dict(row["values"].items())
          # print("INSERT INTO %s.%s(%s)VALUES%s ;"%(binlogevent.schema,binlogevent.table , ','.join(info.keys()) ,str(tuple(info.values())) ) )
          sql = "INSERT INTO %s.%s(%s)VALUES%s ;"%(binlogevent.schema,binlogevent.table , ','.join(info.keys()) ,str(tuple(info.values())) )
        ops_clickhouse('test', 't_repl',sql )
 
        # 当前log_file,log_pos写入配置文件
        write_config(configfile, stream.log_file, stream.log_pos)
 
  except Exception as e:
    print(e)
  finally:
    stream.close()
 
if __name__ == "__main__":
  main()
 
