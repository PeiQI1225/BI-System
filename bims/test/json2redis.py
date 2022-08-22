import json
import redis
 
class RedisTT(object):
 def __init__(self):
  self.host = '127.0.0.1'
  self.port = '6379'
  self.r = redis.StrictRedis(host=self.host, port=self.port)
 
 def insertRedis(self, keyName, jsonStr): # 存入redis
  self.r.lpush(keyName, jsonStr)
 
def save():
 someexpert = {}
 someexpert['id'] = 10000
 someexpert['realname'] = 'expert-a'
 someexpert['organization'] = 'BUAA'
 if RedisTT().r.exists('someexpert'):
  RedisTT().r.delete('someexpert') # 删除key为someexpert的键值对
 RedisTT().insertRedis(keyName='someexpert', jsonStr=json.dumps(someexpert))
 
if __name__ == "__main__":
 save()

 print(RedisTT().r.lrange('someexpert', 0, RedisTT().r.llen('someexpert')))
