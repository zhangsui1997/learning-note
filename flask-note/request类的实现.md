# flask中request类的实现
##  request类中实现的方法  

method : 请求的方法 request.method  

form : 返回form的内容 request.form  {"username": "123", "password": "1234"}  

例：url：xxxx ?a=1&b=2  
args : args返回请求中的参数  request.args  
返回值：{"a": "1", "b": "2"}  
values : request.values values返回请求中的参数和form
返回值CombinedMultiDict([ImmutableMultiDict([('a', '1'), ('b', '2')]), ImmutableMultiDict([('username', '123'), ('password', '1234')])])  

cookies : cookies信息  request.cookies
headers : 请求headers信息，返回的结果是个list
url、path、script_root、base_url、url_root : 看结果比较直观
date、files : date是请求的数据，files随请求上传的文件

## 如何实现将请求转化成可用的request类呢？  
例：一个get请求 "GET / Http:1.1\r\nHost:www.baidu.com\r\n\r\n" 如何得到request.method为GET呢？
底层中的wsgi服务器接受这样的请求(environ)
flask中编写一个类对其进行封装：
```
environ = "GET / http/1.1\r\nHost:www.baidu.com\r\n\r\n"
# wsgi接受这样的请求，一般还包括请求体和请求头

class Request(environ):
    def __init__(self,environ):
        self.environ = environ
    def method(self):  #  以实现request.method方法为例
        pass           #  flask对字符串进行处理得到请求方法

request = Request(environ)
```
