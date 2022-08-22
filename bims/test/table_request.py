import requests
import json

url = "http://127.0.0.1:8081/api/v1/table/list"

payload = json.dumps({
   "dataSourceType": "click_house",
   "dbName": "dbup"
})
headers = {
   'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
   'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)