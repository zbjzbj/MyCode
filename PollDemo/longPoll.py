from flask import Flask, render_template, request, jsonify, session
import uuid
import queue


app = Flask(__name__)
app.secret_key = '切克闹'


USERS = {
    1: {'name': '明凯', 'count': 300},
    2: {'name': '厂长', 'count': 200},
    3: {'name': '7酱', 'count': 600},
}


Q_DICT = {
    # user_id: q对象
}


@app.route('/')
def index():
    # 模拟用户登录
    # 模拟用户登录后的唯一id
    user_id = str(uuid.uuid4())
    # 每个用户都有自己的Q对象
    Q_DICT[user_id] = queue.Queue()
    # 把用户的id存到session
    session['user_id'] = user_id
    # 页面展示投票的人的信息
    return render_template('longPoll.html', users=USERS)


@app.route('/vote', methods=['POST'])
def vote():
    # 处理投票，给打野的票数 +1
    # 用户提交Json数据过来，用request.json获取
    uid = request.json.get('uid')
    USERS[uid]['count'] += 1
    # 投票成功后，给每个用户的Q对象put最新的值进去
    for q in Q_DICT.values():
        q.put(USERS)
    return "投票成功"


@app.route('/get_vote')
def get_vote():
    # 请求进来，从session获取用户的id
    user_id = session.get('user_id')
    # 根据用户的id 获取用户的Q对象
    q = Q_DICT.get(user_id)
    # try:
    #     ret = q.get(timeout=30)
    # except queue.Empty:
    #     ret = ''
    ret = q.get()
    return jsonify(ret)


if __name__ == '__main__':
    app.run(host='192.168.11.23', port=5000)



