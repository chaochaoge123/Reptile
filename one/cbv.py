from flask import Flask, views, render_template, request

app = Flask(__name__)


class Login(views.MethodView):
    methods = ["POST", "GET"]
    def get(self):
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
