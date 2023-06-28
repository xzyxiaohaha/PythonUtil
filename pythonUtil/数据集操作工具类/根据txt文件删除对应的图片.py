# -*- coding = utf-8 -*-
# @Time : 5/7/2023 5:58 PM
# @Author : zyxiao
# @File : 根据txt文件删除对应的图片.py
# @Software : {PyCharm}

# 根据标注的txt文件，将对应的图片文件提取到另外一个地方
import os
def moveFile():
    path_in = r"F:\Undergraduate-graduation-design\deliver_dataset\lables"  # 需要修改的标签文件夹
    path_in2 = r"F:\Undergraduate-graduation-design\deliver_dataset\images"  # 要修改的图片文件夹
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    class_name = ".jpg"  # 图片的文件名后缀
    print(file_in, num_file_in)  # 输出获取到的文件名和数目
    flag = 0
    for i in range(0, num_file_in):
        # path = path_in + "/" + file_in[i]  # 标签的路径
        path2 = path_in2 + "/" + file_in[i][:-4] + class_name  # 图片的路径
        print(path2)
        # os.remove(path)
        os.remove(path2)
        flag += 1
    print("一共删除", flag, "个文件")

if __name__ == '__main__':
    moveFile()