# 使用wtforms的类必须要继承它的Form类
from wtforms import Form, widgets, validators, ValidationError
# simple：普通字段   core：核心字段   html5：H5新增的字段
from wtforms.fields import simple, core, html5

def check_username(form, field):
    if len(field.data) < 2:
        raise ValidationError('错了，嘿嘿')


class TestForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[check_username, ]
    )

    def validate_username(form, field):
        if len(field.data) < 2:
            raise ValidationError('用户名至少两位字符')

    pwd = simple.PasswordField(
        label='密码',
        # 给这个字段添加样式
        render_kw={'class': 'form-control'},
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=8, max=16, message='长度必须在8-16之间')
        ],
    )
    re_pwd = simple.PasswordField(
        label='确认密码',
        # 给这个字段添加样式
        render_kw={'class': 'form-control'},
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=8, max=16, message='长度必须在8-16之间'),
            # EqualTo：校验两个字段的值是否相等
            validators.EqualTo('pwd', message='两次密码不一致')
        ],
    )






