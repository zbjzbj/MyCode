from flask import Blueprint, session, render_template, request
from FlaskPlug import db
from FlaskPlug.models import Tag, Book, Publisher
from FlaskPlug.utils.MyForms import RegisterForm
from FlaskPlug.utils.MyFormsTest import TestForm


userBlue = Blueprint("userBlue", __name__)


@userBlue.route('/register', methods=['GET', 'POST'])
def register():
    # 实例化form
    form_obj = RegisterForm()
    if request.method == "POST":
        form_obj = RegisterForm(request.form)
        if form_obj.validate():
            # 可以写入数据库，这里演示，不写入
            # 验证通过的数据都保存在data这个大字典里面
            # username = form_obj.data.get('username')
            # password = form_obj.data.get('pwd')
            # user_obj = User(username=username, password=password)
            # db.session.add(user_obj)
            # db.session.commit()
            # db.session.close()
            return "注册成功"
    return render_template('register.html', form_obj=form_obj)


@userBlue.route("/test", methods=['GET', 'POST'])
def test():
    # 实例化form
    form_obj = TestForm()
    if request.method == "POST":
        form_obj = TestForm(request.form)
        if form_obj.validate():
            # 包含每个字段的数据的字典
            print(form_obj.data)
            # 这是一个包含各种配置选项以及自定义表单行为的能力的对象
            print(form_obj.meta)
            return "注册成功"
        # 包含每个字段的错误列表的DECT。如果没有验证表单，或者没有错误，则为空。
        print(form_obj.errors)
    return render_template('test.html', form_obj=form_obj)


