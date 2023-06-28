# -*- coding = utf-8 -*-
# @Time : 5/7/2023 5:35 PM
# @Author : zyxiao
# @File : 删除yolo标注文件中的某一类标签.py
# @Software : {PyCharm}

import os
# 1是火

dir_path = r'F:\pycharm-workspace\zhou\test\labels_txt' # 文件夹路径
class_to_remove = '1' # 要删除的类别名称
file_extension = '.txt' # 文件扩展名

# 遍历文件夹下所有文件
for filename in os.listdir(dir_path):
    if filename.endswith(file_extension):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'r') as f:
            lines = f.readlines()
        with open(file_path, 'w') as f:
            for line in lines:
                # 如果不是要删除的类别，就将行写回文件
                if line.split()[0] != class_to_remove:
                    f.write(line)
