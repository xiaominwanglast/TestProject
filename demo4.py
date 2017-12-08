#coding:utf-8
a='provinceId=370000&cityId=371200&cityName=%E8%8E%B1%E8%8A%9C%E5%B8%82&cityType=1&checkSaleType=0&shortName=lw&paymentAccountMall=2699ae10-66e1-11e7-be7c-a15ee685384b&accountKeyMall=1204B263B14BCCDD50FDE5F3C1BCDF10&paymentAccountApp=40051180-7363-11e7-b981-730d5fd6d881&accountKeyApp=2A5C5296E0FDD87C278C03221CF7053E&warehouseAddress=%E5%B1%B1%E4%B8%9C%E7%9C%81%E8%8E%B1%E8%8A%9C%E5%B8%82%E5%9B%9B%E5%B7%9D%E4%B8%AD%E8%B7%AF23%E5%8F%B7&warehousePhone=18301924915&warehouseContact=%E6%97%A0%E6%9D%8E&contactPhoneNum=18301924915'
import urllib
na=urllib.unquote(a)
n={}
for i in na.split('&'):
    j=i.split('=')
    n[j[0]]=j[1]
print n