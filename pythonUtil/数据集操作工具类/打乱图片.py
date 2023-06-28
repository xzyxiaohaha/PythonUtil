# -*- coding = utf-8 -*-
# @Time : 5/5/2023 10:47 AM
# @Author : zyxiao
# @File : 打乱图片.py
# @Software : {PyCharm}

import os
import random

path = r'F:\pycharm-workspace\fireDataset\NormalImage'  # 替换为你的目录路径

for file in os.listdir(path):
    if file.endswith('.jpg'):
        # 生成一个随机的文件名
        new_name = str(random.randint(1, 1000000000)) + '.jpg'
        # 检查新文件名是否已经存在，如果存在则重新生成新文件名
        while os.path.exists(os.path.join(path, new_name)):
            new_name = str(random.randint(1, 1000000000)) + '.jpg'
        # 重命名文件
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
