"""
app.config.root_path: 项目的根路径
os.walk:
    遍历你给的路径下的所有文件(会递归遍历)
    每次循环的根文件夹的路径，文件夹的名字组成的列表，和文件组成的列表
    dirpath, dirnames, filenames
zipfile: 压缩解压文件的模块
shutil: 也是压缩解压文件的模块，还能移动啥的
"""

from flask import Blueprint, request, render_template
from flask import current_app as app
import shutil
from uploadCode.models import CodeRecord
from uploadCode import db
import os
import time


uploadBlue = Blueprint('uploadBlue', __name__)


# zip包上传
@uploadBlue.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template("upload.html", error="")
    # 先获取前端传过来的文件
    file = request.files.get("zip_file")
    # 判断是否是zip包
    zip_file_type = file.filename.rsplit(".", 1)
    if zip_file_type[-1] != "zip":
        return render_template("upload.html", error="文件必须是zip包")
    # 解压路径
    upload_path = os.path.join(app.config.root_path, "files", zip_file_type[0]+str(time.time()))
    print(upload_path)
    # 解压前端传过来的文件file到upload_path这个路径
    shutil._unpack_zipfile(file, upload_path)
    # 遍历保存的文件夹得到所有.py文件
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(upload_path):
        for filename in filenames:
            file_type = filename.rsplit(".", 1)
            if file_type[-1] != "py":
                continue
            file_path = os.path.join(dirpath, filename)
            file_list.append(file_path)
    # 打开每个文件读取行数
    sum_num = 0
    for path in file_list:
        with open(path, mode="rb") as f:
            for line in f:
                if line.strip().startswith(b"#"):
                    continue
                sum_num += 1
    # 得到总行数去保存数据库
    return str(sum_num)


# 柱状图
@uploadBlue.route("/")
def index():
    # 展示用户提交代码柱状图
    queryset = db.session.query(CodeRecord).all()
    date_list = []
    num_list = []
    for obj in queryset:
        date_list.append(str(obj.upload_date))
        num_list.append(obj.code_nums)
    return render_template("index.html", date_list=date_list, num_list=num_list)

