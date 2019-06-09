# 异步编程的原理
都是基于 IO多路复用+回调+事件循环来实现  
```
from selectors import DefaultSelector # 会自动选择适合操作系统的IO多路复用函数  
selector = DefaultSelectors()
selector.register( socket.fileno(文件描述符)， 事件(EVENT_WRITE等), 回调函数 ) # 注册回调

def loop(): # 编写事件循环
    ready = selector.select()  # 返回准备好的事件
    while 条件:
        处理ready...
    
```

# asyncio的基本接口
## loop = asyncio.get_event_loop() 获取事件循环
## asyncio.create_task()
接受一个协程，安排它的运行时间，并返回一个task对象。
## asyncio.ensure_future()
接受一个future对象或者协程，如果是协程包装成task，是future的话就不做处理直接返回。  

**asyncio.create_task()和asyncio.ensure_future()都可以设置回调 add_call_back()**  

## asyncio.wait()
接受一个协程列表将其包装成一个task对象  
可以接受两个参数timeout=None, return_when=ALL_COMPLETED超时间和何时返回  
设置了之后可以返回未完成的future

## asyncio.gather()
接受不限个数的协程对象将其包装成一个task对象    
支持分组，cancel等操作   
按照顺序返回结果  
