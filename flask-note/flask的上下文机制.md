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

## flask的上下文管理机制
### 启动app 请求到来时
1.app.run() --> werkzug.runsimple(host,port,self,** options)会执行self()    
即执行Flask的__call__方法  

2.__ call__ --> self.wsgi_app(environ,start_reponse)    
```
def wsgi_app(self, environ, start_response):
    ctx = self.request_context(environ)  #3.1
    error = None
     try:
         try:
             ctx.push()                  #3.2
     ...
```
3.1 ctx = self.request_context(environ)封装请求相关  
    --> request_context里面将其再封装一层RequestContext(self, environ)  
    --> RequestContext里面含有request和session等:  
 ```
        def __init__(self, app, environ, request=None):
            self.app = app
            if request is None:
                request = app.request_class(environ)
            self.request = request                                  
            self.url_adapter = app.create_url_adapter(self.request)
            self.flashes = None
            self.session = None
  ```
3.2 ctx.push(),将ctx压入栈中:  
      -->_request_ctx_stack.push(self) #_request_ctx_stack是LocalStack对象  
      Localstack:  具体可见[flask如何区分不同的请求?](https://github.com/zhangsui1997/learning-note/blob/master/flask-note/request%E5%A6%82%E4%BD%95%E5%8C%BA%E5%88%86%E4%B8%8D%E5%90%8C%E7%9A%84%E8%AF%B7%E6%B1%82%EF%BC%9F.md)
```
      def __init__(self):
        self._local = Local() #这个local对象是flask实现的可以区分线程和协程的对象
```
4. 执行视图函数时  
   导入request :  
   ```
   request = LocalProxy(partial(_lookup_req_object, 'request')) #偏函数
   ```
   _lookup_req_object:  
   ```
   def _lookup_req_object(name):
       top = _request_ctx_stack.top  #return self._local.stack[-1]返回栈最后一个,是一个RequestContext对象
       if top is None:
           raise RuntimeError(_request_ctx_err_msg)
       return getattr(top, name)
   ```
   执行request.mehtod时候即是执行request.getattr即是：  
   LocalProxy的__getattr__方法: 最后return：    
   ```
   return getattr(self.__local, self.__name__) #这个local就是flask自己实现的
   ```
5.请求结束:  
ctx.auto_pop()  
将ctx从local中删除  
   



