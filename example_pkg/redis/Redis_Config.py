import redis
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password="2001G1225")
r.set('1', '2')
