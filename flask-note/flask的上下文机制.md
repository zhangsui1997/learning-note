## 请求上下文 和 应用上下文
请求上下文:  
1.request全局变量    
2.session全局变量    
应用上下文:   
1.current.app 获取当前的flask应用app  
2.g变量 可以在一次请求中的多个函数之间传递  
## flask机制实现使用到的小知识点
1.偏函数:
```
 from functools import partial
 re_func = partial(func,'request')  #调用func函数的时候使用，将'request'当作第一个参数传入
```
2.threading.local  
为了区分不同的请求，使用到了多线程threading.local的原理  
同时为了区分不同协程，依赖了第三方库greenlet  
flask为了同时支持多线程和协程编写了自己的local类  

##flask的上下文管理机制

