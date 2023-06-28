# -*- coding = utf-8 -*-
# @Time : 5/5/2023 9:51 AM
# @Author : zyxiao
# @File : png_to_jpg.py
# @Software : {PyCharm}
import time

from PIL import Image
import os

# 遍历当前目录下的所有png文件
for file in os.listdir(r'F:\pycharm-workspace\selfCreateDataset_\normal'):

    # if file.endswith('.png'):
    if file.endswith('.jpg'):
        # 读取png文件
        img = Image.open('F:\pycharm-workspace\selfCreateDataset_/normal/' +file)
        # 取得原文件名（去掉后缀）
        filename = os.path.splitext(file)[0]
        # 将png文件转为jpg，并保存
        try:
            img.convert('RGB').save(f'F:/pycharm-workspace/selfCreateDataset_/normal2/{filename}.jpg')
        except:
            print(file + "is incorrect===============")
        print("save F:/pycharm-workspace/fireDataset_/Normal2/"+filename+".jpg")
