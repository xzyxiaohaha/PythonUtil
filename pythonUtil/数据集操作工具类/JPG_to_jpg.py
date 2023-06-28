# -*- coding = utf-8 -*-
# @Time : 5/5/2023 10:25 AM
# @Author : zyxiao
# @File : JPG_to_jpg.py
# @Software : {PyCharm}


import os
from PIL import Image

# 设置要转换的文件夹路径
dir_path = r'F:\pycharm-workspace\fireDataset\testt'

# 遍历文件夹中所有文件
#这种直接修改后缀的方法，应该是不可取的，会造成文件读取错误
for file_name in os.listdir(dir_path):
    if file_name.endswith('.JPG'):  # 判断文件是否为JPG格式
        # 打开图片，转换为RGB格式，然后保存为jpg格式
        img_path = os.path.join(dir_path, file_name)
        img = Image.open(img_path).convert('RGB')
        new_file_name = file_name.replace('.JPG', '.jpg')
        new_img_path = os.path.join(dir_path, new_file_name)
        img.save("F:/pycharm-workspace/fireDataset/testt/1/"+new_file_name, quality=95)


num = 0
dir_path = r"F:\pycharm-workspace\fireDataset\NormalImage"
for file_name in os.listdir(dir_path):
    if file_name.endswith('.JPG'):  # 判断文件是否为JPG格式
        num +=1
        print(num)

