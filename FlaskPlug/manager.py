from FlaskPlug import create_app, db
from FlaskPlug.models import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 1. 导入SQLAlchemy的实例化db和script、migrate插件


app = create_app()
manager = Manager(app)
Migrate(app, db)  # 实例化


# 给manager添加命令
# manager.add_command("db", MigrateCommand)

"""
数据库迁移命令
依赖 flask-script
python manager.py db init # 初始化
python manager.py db migrate # 相当于Django的ORM的makemigrations
python manager.py db upgrade # 相当于Django的ORM的migrate
"""


# # 位置传参
# @manager.command
# def my_add(arg1, arg2):
#     """
#     自定义命令
#     python manager.py my_add 1 2
#     """
#     ret = int(arg1) + int(arg2)
#     print(arg1, arg2, ret)
#
#
# # 关键字传参
# # 关键字参数的简写：-n
# # 关键字参数全写：--name
# # 关键字的描述：dest
# @manager.option('-n', '--name', dest='name')
# @manager.option('-a', '--age', dest='age')
# def person(name, age):
#     """
#     自定义命令
#     执行： python manager.py person -n 小明 --age 28
#     """
#     print(name, age)


if __name__ == '__main__':
    # app.run()
    manager.run()
