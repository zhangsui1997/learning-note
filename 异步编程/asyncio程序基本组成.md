```
import asyncio
from functools import partial

async def get_url(number):
    print("get {}".format(number))
    return number

def callback(number,future):
    print("success {0}  {1} ".format(number,future.result()))


if __name__ == "__main__":
    loop = asyncio.get_event_loop() # 获取事件循环
    #task = loop.create_task( get_url(1) ) # 添加到事件循环中，是一个future对象
    task = asyncio.ensure_future(get_url(1)) 
    # 添加到时间循环中和上行代码作用一致，内部会检测是否有loop没有就创建一个再添加
    task.add_done_callback( partial(callback,1) ) 
    # 回调函数，在事件循环完成之后（只接受一个参数，需要使用偏函数来包装有参数的回调函数）
    loop.run_until_complete(task)
    print(task.result())
```
