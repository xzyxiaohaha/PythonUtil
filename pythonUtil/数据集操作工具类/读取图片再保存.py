# -*- coding = utf-8 -*-
# @Time : 5/6/2023 10:43 AM
# @Author : zyxiao
# @File : 读取图片再保存.py
# @Software : {PyCharm}

import os
import cv2

# 定义要读取的文件夹路径和保存的文件夹路径
src_folder = r'F:\pycharm-workspace\selfCreateDataset_\images'
dst_folder = r'F:\pycharm-workspace\selfCreateDataset_\images2'

# 创建保存图片的文件夹
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# 遍历读取文件夹中的图片文件
for file_name in os.listdir(src_folder):
    # 判断文件是否是图片文件（这里仅判断后缀名）
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # 构造完整路径
        file_path = os.path.join(src_folder, file_name)
        # 使用cv2读取图片
        img = cv2.imread(file_path)
        # 保存图片到目标文件夹中
        save_path = os.path.join(dst_folder, file_name)
        cv2.imwrite(save_path, img)

