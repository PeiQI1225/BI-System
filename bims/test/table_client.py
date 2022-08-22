import http.client
import json

conn = http.client.HTTPSConnection("127.0.0.1", 9001)
payload = json.dumps({
   "dataSourceType": "click_house",
   "dbName": "dbup"
})
headers = {
   'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
   'Content-Type': 'application/json'
}
conn.request("GET", "/api/v1/table/list", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))