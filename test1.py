#coding:utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
headers={'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
url='http://www.songqinnet.com/login'
session=requests.Session()
rq=session.get(url=url,headers=headers)
s = etree.HTML(rq.text)
text=s.xpath('//input[@name="_csrf_token"]/@value')
_csrf_token=text[0]
print _csrf_token
bs=BeautifulSoup(rq.text,'lxml')
print bs.find('input',attrs={'name':'_csrf_token'})['value']
print re.findall('name="_csrf_token" value="(.*?)"',rq.text)
# post_rq=session.post(url='http://www.songqinnet.com/login_check',data={'_username':'18895392732',
#                                      '_password':'ASD123456',
#                                      '_remember_me':'on',
#                                      '_target_path':'/',
#                                      '_csrf_token':_csrf_token},headers=headers)
# get_rq=session.get(url='http://www.songqinnet.com/partner/login?goto=/',headers=headers)
# for value in post_rq.cookies:
#     print value
#print get_rq.text