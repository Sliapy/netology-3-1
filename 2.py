import requests
import json

url = 'http://requestbin.fullcontact.com/1949hn21'
json = {
    'month': 'May',
    'result': '1:0',
    'team': 'Manchester'
}

# response = requests.post(url, json=json)
# print(response.status_code)

url2 = 'http://httpbin.org'
params = {
    'id': [1, 2, 3]
}
response = requests.get(url2, params=params)
print(response.json())
