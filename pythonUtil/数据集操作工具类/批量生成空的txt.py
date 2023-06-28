# -*- coding = utf-8 -*-
# @Time : 5/5/2023 11:00 AM
# @Author : zyxiao
# @File : 批量生成空的txt.py
# @Software : {PyCharm}

import os
import shutil

# 定义原始目录和目标目录
src_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230628_chaoyi_dangshui\images\train'
dest_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230628_chaoyi_dangshui\labels\train'

# 遍历原始目录中的所有jpg文件
for filename in os.listdir(src_dir):
    if filename.endswith('.jpg'):
        # 生成对应的txt文件名
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        # 在目标目录中创建空的txt文件
        txt_path = os.path.join(dest_dir, txt_filename)
        open(txt_path, 'a').close()
