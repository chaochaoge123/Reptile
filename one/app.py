from flask import Flask,request,render_template,send_file,redirect,url_for,jsonify,Markup,session
from serv import detail
app = Flask(__name__)
# app.config.from_object(FlaskConfigDebug)  导入配置文件
app.register_blueprint (detail .detail_blue )

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/login')
# def login():
#     print(request.method )
#     print(request.form )
#     return render_template('tset.html')
# def log():
#     # return url_for('my_login')  # 后半段地址
#     return jsonify({'status':666})
# app.add_url_rule ('/login',endpoint= 'my_login',view_func=log,methods= ["POST",'GET'] )


# @app.route('/file')
# def fil():
#     return send_file(r'F:\flask\one\static\4444444444.PNG')
#
@app.route('/login',methods= ('POST','GET'))
def reque():
    print(request .method )
    if request .method =='POST':
        print(request .values,type(request .values ))
        print(request .values .to_dict()) # 前台数据字典形式
        urluser_name=request.args.get('username')
        username=request .form.get('username')
        password=request .form.get('password')
        print(request .path)
        #上传文件，保存
        print(request.files, type(request.files))
        f=request .files['my']
        f.save(f.filename)

        if username=='yin' and password =='gg':
            session['user']=username
            return redirect('/file')
    return render_template('tset.html')
#


# 路由
@app.route('/log',methods= ("POST","GET"),endpoint= 'mylog')
# endpoint= 'mylog' 反向解析
# redirect_to= '/log'  重定向
# defaults= {'nid':10}  默认参数
# strict_slashes=True  严格url格式
def hello():
     return 'Hello World!'

# /index/<int:nid> 动态路由
@app.route('/index/<int:nid>', endpoint='myindex', )
def index(nid):
    print(nid)
    return url_for(endpoint='myundex', nid=nid)  # 返回url后半部分


# 特殊装饰器
@app.errorhandler(404)
def my_404(args):
    food = 'chicken'
    print('今天 %s' % (food))
    print('今天 {}'.format(food))
    print(f'今天{food}')
    return Markup('<h1>页面不存在</h1>')

@app.before_request  # 访问函数之前触发，类似于Django中间件
def be1():
    if session .get('user'):
        return None

    if request.path=="/login":
        return None
    # return  None   # None表示往下执行，否则停住(not None)
    # return '再见'  # 不在执行be2函数和视图函数

@app.before_request  # 访问函数之前触发，类似于Django中间件
def be2():
    print(be2)
    return None

@app.after_request
def af(r):
    print('OK')
    return r

@app.after_request  #在函数处理完后触发
def af1(res):
    print(res)
    return res




if __name__ == '__main__':
     app.run(debug= True )

#debug= True  代码改动就重启