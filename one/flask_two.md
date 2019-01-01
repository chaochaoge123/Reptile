### 1. 蓝图
- 另一种flask实例，不能执行(run)
- 使用
```
蓝图文件 detail.py：
from flask  import Blueprint
detail_blue=Blueprint ('serv',__name__)   # serv 文件夹名
@detail_blue .route('/add_user',methods=["POST","GET"])
def add_user():
    return '添加用户'
    
flask文件：
from serv import detail
app.register_blueprint (detail .detail_blue)
```
- 配置
```
detail_blueprint = Blueprint("serv",__name__, template_folder="serv_temp",
static_folder="serv_static",
static_url_path="/serv_static",url_prefix="/servs")
# url_prefix="/servs" url前缀
```
### 2.特殊装饰器
- 错误信息
```
@app.errorhandler(404)
def my_404(args):
    return Markup('<h1>页面不存在</h1>')
```
- 在处理函数之前访问
```
@app.before_request  # 访问函数之前触发，类似于Django中间件
def be1():
    print(be1)
    return None   # None表示往下执行，否则停住(not None)
```
- 函数之后访问
```
@app.after_request  #在函数处理完后触发
def af1(res):
    print('hello')
    return res
```
- 顺序
`be1 -> be2 -> af2 -> af1`
- @app.template_folder() 类偏函数的方法
- @app.template_global() 全局函数

### 3. CBV
```
from flask import Flask, views, render_template, request

app = Flask(__name__)


class Login(views.MethodView):
    def get(self):
        methods = ["POST", "GET"]
        return render_template("tset.html")

    def post(self):
        username = request.form.get('username')
        pwd = request.form.get('password')
        if username == "yin" and pwd == 'ff':
            return "登录成功"
        return "失败"


app.add_url_rule("/logingg", endpoint=None, view_func=Login.as_view(name='logingg'))

if __name__ == '__main__':
    app.run("0.0.0.0", 9527, debug=True)

```

















