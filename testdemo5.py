#coding:utf-8
# headers={'Authorization':'Cwu5YSzR2xVczbJr474pHr0rJHy_FFv_'}
import requests
session=requests.Session()
data={'cityIds':[320100],'firstCatalogId':'2000000','goodId':'137553','goodType':'0','goodsBrandName':'12','goodsName':'可乐666',"limit":2 ,'offset':'0','secondCatalogId':'2030000','taxType':'0','warehouseIds':'13'}

qq=session.post(url='http://192.168.1.245:35036/user/login',data={'username':'12345678910','password':'123456'})
print qq.text
print qq.headers
rq=session.post(url='http://192.168.1.245:35036/api/report/goods/list',data=data)
print rq.text