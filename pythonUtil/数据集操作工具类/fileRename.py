# -*- coding = utf-8 -*-
# @Time : 12/7/2022 4:55 PM
# @Author : zyxiao
# @File : fileRename.py
# @Software : {PyCharm}



import os
# fileRename()根据txt文件目录下的文件批量修改jpg和txt的文件名
def fileRename1():
    path_in = r"F:\pycharm-workspace\fireDataset\open_fire\open_fire_labels\txt_change"  # 待批量重命名的文件夹
    path_in2 = r"F:\pycharm-workspace\fireDataset\open_fire\savepath2"  # 待批量重命名的文件夹
    class_name = ".txt"  # 重命名后的文件名后缀
    class_name2 = ".jpg"
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    file_in2 = os.listdir(path_in2)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    num_file_in2 = len(file_in2)  # 获取文件数目
    print(file_in, num_file_in)  # 输出修改前的文件名
    print(file_in2, num_file_in2)  # 输出修改前的文件名

    for i in range(0, num_file_in):
        # t = str('%06d' %(i + 1))
        t = str('%07d' %(i + 4962))
        # print(t)
        # print(file_in[i][:-4]+class_name2)
        new_name = os.rename(path_in + "/" + file_in[i], path_in + "/" + t + class_name)  # 重命名文件名
        new_name2 = os.rename(path_in2 + "/" + file_in[i][:-4]+class_name2, path_in2 + "/" + t + class_name2)  # 重命名文件名

    file_out = os.listdir(path_in)
    file_out2 = os.listdir(path_in2)
    print(file_out)  # 输出修改后的结果
    print(file_out2)  # 输出修改后的结果

# name = '小明 '
# num = 1
# print('我的名字是%s,学号是%07d' % (name, num))
# schoolId =1
# ha = '%05d' % schoolId
# print(ha)

# fileRename2()直接批量修改文件名
def fileRename2():
    path_in = r"F:\pycharm-workspace\fireDataset\NormalImage"  # 待批量重命名的文件夹
    class_name = ".jpg"
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    print(file_in, num_file_in)  # 输出修改前的文件名
    for i in range(0, num_file_in):
        t = str('%07d' % (i + 5001))
        # print(path_in + "/" + file_in[i][:-4]+class_name, path_in + "/" + t + class_name)
        new_name = os.rename(path_in + "/" + file_in[i], path_in + "/" + t + class_name)  # 重命名文件名

    file_out = os.listdir(path_in)
    print(file_out)  # 输出修改后的结果

if __name__ == '__main__':
    fileRename2()
