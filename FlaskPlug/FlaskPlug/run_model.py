from FlaskPlug import db, create_app
# 一定要导入models 否则找不到表创建不出来
from FlaskPlug.models import *


app = create_app()
# app_context()就是前两篇文章里面Flask请求上下文走过的流程啊
# app_ctx = AppContext(app)
app_ctx = app.app_context()
# with 就会去走AppContext的__enter__和__exit__方法
# __enter__就是去取app了，__exit__就是删除
with app_ctx:
    # db.create_all()
    db.drop_all()
