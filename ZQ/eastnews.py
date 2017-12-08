#coding:utf-8
# import requests
# headers={'User-Agent': 'okhttp/3.4.1',
#          'Accept-Encoding':'gzip',
#          'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
# #同步接口
# taskcenter_tongbu_url='https://kp.dftoutiao.com/taskfinishnew/sync_address_book'
# taskcenter_tongbu_data={'accid':'101664738'}
# taskcenter_tongbu_res=requests.post(url=taskcenter_tongbu_url,data=taskcenter_tongbu_data,headers=headers)
# print taskcenter_tongbu_res.text
#签到接口

# sign_url='https://kp.dftoutiao.com/sign3/take_s'
# sign_response=requests.post(url=sign_url)
"""
accid	101664738
ts	1510822068
sign	980d59abb4dc8e6cd088d1c190f0be3c
"""
import os
print os.path.dirname(os.getcwd())