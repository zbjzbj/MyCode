from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

USERS = {
    1: {'name': '明凯', 'count': 300},
    2: {'name': '厂长', 'count': 200},
    3: {'name': '7酱', 'count': 600},
}


@app.route('/')
def index():
    return render_template('Poll.html', users=USERS)


@app.route('/vote', methods=['POST'])
def vote():
    # 接收uid,通过uid给打野票数 +1
    # 用户提交Json数据过来，用request.json获取
    uid = request.json.get('uid')
    USERS[uid]['count'] += 1
    return "投票成功"


@app.route('/get_vote')
def get_vote():
    # 返回users数据
    # jsonify 是flask自带的序列化器
    return jsonify(USERS)


if __name__ == '__main__':
    app.run()

