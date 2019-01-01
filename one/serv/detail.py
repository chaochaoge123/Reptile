from flask import Blueprint,request

detail_blue = Blueprint('serv', __name__,url_prefix="/se")  # serv 文件夹名


@detail_blue.route('/add_user',methods=["POST", "GET"])
def add_user():
    print(request.path)
    return '添加用户'















