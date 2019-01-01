from flask import Flask, request, render_template
from geventwebsocket.websocket import WebSocket
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import json

app = Flask(__name__)

user_socket_list = []
user_socket_dict = {}


@app.route("/index")
def index():
    return render_template("ws.html")


@app.route("/ws/<nickname>")
def ws(nickname):
    user_socket = request.environ.get("wsgi.websocket")  # type: WebSocket
    # user_ip = request.environ.get("")
    print(nickname, ":", request.environ.get("REMOTE_ADDR"))

    if user_socket:
        user_socket_dict[nickname] = user_socket

    print(len(user_socket_dict), user_socket_dict)
    while 1:
        msg = user_socket.receive()
        msg_dict = json.loads(msg)
        print(msg_dict)
        # {msg : "FUCK" ,to_user:yinwangba}
        # send_str = {"sender": nickname, "msg": msg}

        # msg[to_user] = teacher
        usocket = user_socket_dict[msg_dict.get("to_user")]
        send_msg = json.dumps({"sender": nickname, "msg": msg_dict.get("msg")})
        usocket.send(send_msg)
        # dj = {sender:nickname,msg:"FUCK"}
        # usocket.send(dj)
        #----------------------------web端----------------------
        # {from_user:nickname,msg:"FUCK"}
        ####### {msg : "FUCK" ,to_user:yinwangba} ######
        # {msg : "FUCK too" ,to_user:nickname}



# http://127.0.0.1:9527/ws
# websocket://127.0.0.1:9527/ws

if __name__ == '__main__':
    # app.run("0.0.0.0",9527,debug=True)

    http_serv = WSGIServer(("0.0.0.0", 9527), app, handler_class=WebSocketHandler)

    http_serv.serve_forever()
