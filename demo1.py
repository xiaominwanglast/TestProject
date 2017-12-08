#coding:utf-8
import requests
import socket
from functools import wraps
def defind_requests(fun):
    @wraps(fun)
    def _request(self):
        try:
            fun(self)
        except requests.HTTPError as e:
            return e
        except requests.ConnectionError as e:
            return e
        except socket.timeout as e:
            return e
    return _request

class login_diandaemail(object):
    '''
    login in dianda_email with username and password
    '''
    def __init__(self):
        self.username='wangxm@diandainfo.com'
        self.password='Dianda123456'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',}

    def __str__(self):
        '''
        get self._class_.__dict__
        :return: username and password
        '''
        return self.username+' '+self.password

    @property
    def login_email_data(self):
        login_data={'User':self.username,
                    'Password':self.password}
        login_url='http://mail.diandainfo.com/WorldClient.dll?View=Main'
        return login_data,login_url

    @defind_requests
    def login_email(self):
        #TODO change the type of post
        #return the requests data
        login_data=self.login_email_data
        rq=requests.post(url=login_data[1],data=login_data[0],headers=self.headers)
        print rq.status_code
        return rq.text


print login_diandaemail()
login_diandaemail().login_email()





