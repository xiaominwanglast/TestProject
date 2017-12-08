#coding:utf-8
import requests
import json
import urllib2
url='http://192.168.1.101:15673/api/exchanges/%2F/amq.default/publish'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
         'authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q='}
data_json={"vhost":"/",
           "name":"amq.default",
           "properties":{"delivery_mode":1,"headers":{}},
           "routing_key":"finance.inOutDetail",
           "delivery_mode":"1",
           "payload":json.dumps({
                    "messageId": "TEST-ID-0000023",
                    "data": {
                            "type": 1,
                            "goodId": 113898,
                            "warehouseId": 10,
                            "quantity": 100,
                            "mainOrderId": 117199,
                            "isGift": 0
                            }
                    }).encode('utf-8'),
           "headers":{},
           "props":{},
           "payload_encoding":"string"
           }

res=requests.post(url=url,data=json.dumps(data_json),headers=headers)
print res.text