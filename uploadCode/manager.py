from uploadCode import create_app, db
from uploadCode.models import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 1. 导入SQLAlchemy的实例化db和script、migrate插件


app = create_app()
manager = Manager(app)
Migrate(app, db)  # 实例化


# 给manager添加命令
manager.add_command("db", MigrateCommand)

"""
数据库迁移命令
依赖 flask-script
python manager.py db init # 初始化
python manager.py db migrate # 相当于Django的ORM的makemigrations
python manager.py db upgrade # 相当于Django的ORM的migrate
"""


if __name__ == '__main__':
    # app.run()
    manager.run()
