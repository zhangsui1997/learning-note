# session
```
from flask import session,Flask
app = Flask(__name__)
app.session_cookie_name="xxx"
app.secret_key = "XXXXXX"
```

## 第一次请求时
此时请求中没有cookie  
在创建RequestContext时其中包括了request和session此时的session=None  
触发wsgi_app:  
```
ctx = self.request_context(environ)
        error = None
        try:
            try:
                ctx.push()  # 在此处
                response = self.full_dispatch_request() # 运行视图函数
            except Exception as e:
               ...
```
ctx.push()执行session相关操作:  
```
 if self.session is None:
            session_interface = self.app.session_interface
            self.session = session_interface.open_session(  # open_session
                self.app, self.request
            )

            if self.session is None:
                self.session = session_interface.make_null_session(self.app)
```
open_session  
```
    def open_session(self, app, request):
        获取session签名的算法
        s = self.get_signing_serializer(app)
	如果为空 直接返回None
        if s is None:
            return None
        val = request.cookies.get(app.session_cookie_name)
	# 如果val为空，即request.cookies为空
        if not val:
            return self.session_class()
        max_age = total_seconds(app.permanent_session_lifetime)
        try:
            data = s.loads(val, max_age=max_age) # 解密
            return self.session_class(data)      # 返回session字典 数据都在字典里
        except BadSignature:
            return self.session_class()
```
设置session: session["key"] = value(调用这个类字典类的__set__item__方法)

