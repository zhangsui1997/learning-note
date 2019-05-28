# request如何区分不同的请求?
## requset在一个flask app中如何区分不同的请求，返回不同的数据呢？
```
import threading
try:
    from greenlet import getcurrent as get_ident #依赖greenlet库 实现对协程的支持 greenlet.greenlet当前协程的标识
except ImportError:
    try:
        from threading import get_ident #对线程的支持 threading.get_ident当前线程的标识
    except ImportError:
        from _thread import get_ident
# 以上三个方法的作用都是对不同的请求得到不同的标识

class myLocal(object):
    def __init__(self):
        object.__setattr__(self, "__storage__", {})
        object.__setattr__(self, "__getIdent__", get_ident) # 如果调用当前的setattr方法会出现递归问题

    def __setattr__(self, key, value):
        ident = self.__getIdent__()
        try:
            self.__storage__[ident][key] = value
        except KeyError:                          # 每一个请求都有其不同的标识，将唯一标识作为其字典的键
            self.__storage__[ident]={key:value}   # 就可以实现不同请求的隔离

    def __getattr__(self, item):
        try:
            return self.__storage__[self.__getIdent__()][item]
        except KeyError:
            raise AttributeError(item)

    def __delattr__(self, item):
        try:
            del self.__storage__[self.__getIdent__()][item]
        except KeyError:
            raise AttributeError(item)

local = myLocal()
def task(num):
    local.value=num
    import time
    time.sleep(1)
    #print(local.value, " ", threading.current_thread().name)

for i in range(20):
    th = threading.Thread(target=task,args=(i,),name="线程%s"%i)
    th.start()
print(local.__storage__)
```
