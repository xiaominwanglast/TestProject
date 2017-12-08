#coding:utf-8
# rpcserver.py
import pickle
from selenium import webdriver
from multiprocessing.connection import Listener
from threading import Thread

drive = webdriver.Firefox()


def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()


class RPCHandler(object):
    def __init__(self):
        # rpc functions map
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                   # 接收到一条消息, 使用pickle协议编码
                func_name, args, kwargs = pickle.loads(connection.recv())
                   # rpc调用函数，并返回结果
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    print(type(r))
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


if __name__ == '__main__':
       # 写几个测试方法
    def add():
        reload(rpcclient)
        rpcclient.get(drive)


       # 新建一个handler类实例, 并将add方法注册到handler里面
    import rpcclient
    from imp import reload

    rpc_handler = RPCHandler()
    rpc_handler.register_function(add)

    # 运行server
    rpc_server(rpc_handler, ('localhost', 17001), authkey=b'tab_space')