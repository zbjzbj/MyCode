from flask import Flask, render_template, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import json


app = Flask(__name__)

USERS = {
    1: {'name': '明凯', 'count': 300},
    2: {'name': '厂长', 'count': 200},
    3: {'name': '7酱', 'count': 600},
}

WEBSOCKET_LIST = []


@app.route('/')
def index():
    return render_template('websocket.html', users=USERS)


@app.route('/vote')
def vote():
    # 处理websocket
    # 判断是什么类型的请求，HTTP还是websocket
    # 看能否获取得到websocket的对象
    ws = request.environ.get("wsgi.websocket")
    if not ws:
        return "这是HTTP协议的请求"
    # 把所有用户的ws对象存到一个列表
    WEBSOCKET_LIST.append(ws)
    while True:
        # 获取前端传过来的uid，给打野票数 +1
        uid = ws.receive()
        # 如果前端主动断开连接
        # 那么后端也关闭与前端的连接
        if not uid:
            WEBSOCKET_LIST.remove(ws)
            ws.close()
            break
        uid = int(uid)
        USERS[uid]["count"] += 1
        data = {
            "uid": uid,
            "name": USERS[uid]["name"],
            "count": USERS[uid]["count"]
        }
        for ws in WEBSOCKET_LIST:
            # 给前端发送新的数据
            ws.send(json.dumps(data))


if __name__ == '__main__':
    # app.run()
    # 这样启服务的意思是：即支持HTTP协议，也支持websocket协议
    http_server = WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
