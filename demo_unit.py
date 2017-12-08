#coding:utf-8
import requests
from bs4 import BeautifulSoup

page_url='http://www.runoob.com/python/python-variable-types.html'
rq=requests.get(page_url)
soup=BeautifulSoup(rq.text,'lxml')
# print bs.find('title').string
#
# print bs.find('meta',attrs={'name':'description'}).attrs['content']
#
# divs= bs.find_all('a',attrs={'target':'_top'})
# for i in divs:
#     print i.attrs['title'],
#     print 'http://www.runoob.com'+i.attrs['href']
# import re
# def __get_new_urls():
#     links=soup.find_all('a',href=re.compile(r'/python/.*\.html'))
#     for link in links:
#         new_url=link['href']
#
#         new_full_url=''.join(['www.runoob.com',new_url])
#         print new_full_url
#
# __get_new_urls()
def changeIntoStr(data, str_data=''):
    if isinstance(data, unicode):
        str_data = data.encode('utf-8')
    elif isinstance(data, str):
        str_data = data
    return str_data
import json
# import MySQLdb
# cn=MySQLdb.connect(host='192.168.1.101',port=3306,user='dddev',passwd='123456')
# cur=cn.cursor()
# cn.select_db('ctcdb_new_test')
# count=cur.execute('select WarehouseId,StoreGoodsOrderBranchId from store_order_branch_details where StoreGoodsOrderId=11114951 ORDER BY WarehouseId desc  LIMIT 1 ')
# info =cur.fetchmany(count)
# print info
session=requests.Session()
# login=session.post(url='http://192.168.1.251:40000/branch/login',data={'pwd':'e10adc3949ba59abbe56e057f20f883e','name':'wx001'})
# login_token=json.loads(changeIntoStr(login.text))
# print login.text
# list_data=session.post(url='http://192.168.1.251:40000/api/expressRouteDetail/list',data={"interfaceType":"FH","limit":20,"offset":0,"state":"TRUCK_LOAD"},headers={'Authorization':login_token['token']})
# json_list=json.loads(changeIntoStr(list_data.text))
# order='11114951'
# numberId='FH-4-11114951'
# print json_list
# receive=session.post(url='http://192.168.1.251:40000/api/expressRouteDetail/receive',data={'numberId':numberId},headers={'Authorization':login_token['token']})
# print receive.text
#
#
url='http://192.168.1.240:50000/v1/order/delivery/getGoods'
rq=session.post(url=url,data={"QRCode":"15_Order_3052"},headers={'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ODIsInBob25lIjoiMTc2MDIxMzMxNjMiLCJuYW1lIjoicXdlIiwiYWNjb3VudCI6InBzXzE3NjAyMTMzMTYzIiwidHJhZGVBY2NvdW50Tm8iOiJUWkgxMDAwNTM1Iiwid2FyZWhvdXNlSWQiOjE1LCJjaXR5SWQiOiIzMjAyMDAiLCJzaW5nbGVWYWx1ZSI6MTUxMjM3Mzg5MTcxOCwiZXhwIjoxNTE0OTY1ODkxNzE4fQ.F4hqQzgvwnqEMfWTieOJCDSJGhe6P6wsFwb9iSiluvk'})
print rq.text
