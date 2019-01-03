# 使用wtforms的类必须要继承它的Form类
from wtforms import Form, widgets, validators
# simple：普通字段   core：核心字段   html5：H5新增的字段
from wtforms.fields import simple, core, html5


class RegisterForm(Form):
    username = simple.StringField(
        label='用户名',
        # 给这个字段添加样式
        render_kw={'class': 'form-control'},
        # 可以定义多个校验规则
        validators=[
            # DataRequired字段必填
            validators.DataRequired(message='用户名不能为空'),
            # length字段的长度限制
            # message:用户填写错误时的错误信息
            validators.length(min=2, max=8, message='长度必须在2-8之间')
        ],
        # widget=widgets.TextArea()
    )
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
    phone = simple.StringField(
        label='手机号码',
        validators=[
            validators.Regexp(regex="^1[3-9][0-9]{9}$",message='手机格式不正确')
        ]

    )
    # H5新增的标签email
    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
        ],
        widget=widgets.TextInput(input_type='email'),
    )
    # 核心字段core,单选框
    gender = core.RadioField(
        label='性别',
        choices=((1, '男'), (2, '女')),
        # 前端传过来的数据是字符串类型，coerce可以把穿过来的数据转换类型
        # 因为数据库存的1是int类型，前端选择"男"，传过来的是字符串1
        coerce=int,
        default=1
    )
    # 单选下拉菜单
    city = core.SelectField(
        label='城市',
        choices=(('sz', '深圳'), ('gz', '广州'), )
    )
    # 多选下拉菜单
    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '美女'),
            (2, 'xiong'),
        ),
    )
    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        # 把多选下拉菜单设置成列表
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # 从数据库获取数据 做到实时更新
        # self.favor.choices = ORM操作
        # 这里演示一下更改
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))








