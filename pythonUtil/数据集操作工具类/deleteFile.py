# -*- coding = utf-8 -*-
# @Time : 2022/3/31 21:42
# @Author : zyxiao
# @File : deleteFile.py
# @Software : {PyCharm}
# import torch
# print(torch.cuda.is_available())
# print(torch.__version__)
import os

# 在进行多目标检测时会使用0,1，2代表某一类，本方法用于删除标注文件中含有某一类
def delete():
    path_in = r"F:\pycharm-workspace\fireDataset\Fire-Smoke-Dataset\labels"  # 需要修改的标签文件夹
    path_in2 = r"F:\pycharm-workspace\fireDataset\Fire-Smoke-Dataset\JPEGImages"  # 要修改的图片文件夹
    class_name = ".jpg"  # 图片的文件名后缀
    class_name2 = ".txt"    # 标签的文件名后缀
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    print(file_in, num_file_in)  # 输出获取到的文件名和数目
    flag = 0
    for i in range(0, num_file_in):
        path = path_in + "/" + file_in[i]       #标签的路径
        path2 = path_in2 + "/" + file_in[i][:-4] + class_name       #图片的路径
        f = open(path, encoding="utf-8")
        readContent = f.read()      #读取txt得到的内容
        for j in range(0, len(readContent)):
            if readContent[0] == "1":
                f.close()
                os.remove(path)
                os.remove(path2)
                flag += 1
                break

            if(readContent[j] == "\n"):
                try:
                    if(readContent[j+1] == '1'):        #如果得到标注内容中含有标签“1”，就删除这个标注文件
                        print(file_in[i],":存在1")
                        f.close()
                        os.remove(path)
                        os.remove(path2)
                        # print(path)
                        # print(path2)
                        flag += 1
                        break
                except IndexError as e:
                    print(e, "---")
    print("一共删除",flag,"个文件")

# 基础复制方法
import shutil
def mycopyfile(srcfile,dstpath):                       # 复制函数,
# srcfile 需要复制、移动的文件
# dstpath 目的地址
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        print ("copy %s -> %s"%(srcfile, dstpath + fname))

# 根据标注的txt文件，将对应的图片文件提取到另外一个地方
def moveFile():
    path_in = r"F:\pycharm-workspace\zhou\test\labels_txt_null"  # 需要修改的标签文件夹
    path_in2 = r"F:\pycharm-workspace\zhou\test\images"  # 要修改的图片文件夹
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    class_name = ".jpg"  # 图片的文件名后缀
    print(file_in, num_file_in)  # 输出获取到的文件名和数目
    flag = 0
    for i in range(0, num_file_in):
        # path = path_in + "/" + file_in[i]  # 标签的路径
        path2 = path_in2 + "/" + file_in[i][:-4] + class_name  # 图片的路径
        print(path2)
        mycopyfile(path2, r"F:\pycharm-workspace\zhou\test\images_null/")
        # os.remove(path)
        # os.remove(path2)
        flag += 1
    print("一共移动", flag, "个文件")

#删除给定txt文件中记录的重复文件
def delete2():
    fileHandler = open("../重复.txt", "r")
    # Get list of all lines in file
    listOfLines = fileHandler.readlines()
    # Close file
    fileHandler.close()
    classname = ".txt"
    flag = 0
    for line in listOfLines:
        path1 = line.strip()[86:]  # strip用于去除开头和末端的空格
        print(path1)
        path2 = path1[:33]+"labels2"+path1[40:47]+classname
        print(path2)
        os.remove(path1)
        os.remove(path2)
        flag += 1
    print("一共删除：", flag, "个文件")

#删除给定txt文件中记录的重复文件
def delete3():
    fileHandler = open("../重复2.txt", "r")
    # Get list of all lines in file
    listOfLines = fileHandler.readlines()
    # Close file
    fileHandler.close()
    classname = ".txt"
    flag = 0
    for line in listOfLines:
        path1 = line.strip()[91:]  # strip用于去除开头和末端的空格
        print(path1)
        os.remove(path1)
        flag += 1
    print("一共删除：", flag, "个文件")




if __name__ == '__main__':
    # delete4()
    # delete3()
    moveFile()

# num_file_in = len(file_in)  # 获取文件数目
# print(file_in, num_file_in)  # 输出修改前的文件名
#
# for i in range(0, num_file_in):
#     t = str('%06d' %(i + 1))
#     t = str('%06d' %(i + 1443))
#     # print(t)
#     # print(file_in[i][:-4]+class_name2)
#     new_name = os.rename(path_in + "/" + file_in[i], path_in + "/" + t + class_name)  # 重命名文件名
#
# file_out = os.listdir(path_in)
# print(file_out)  # 输出修改后的结果
# print(file_out2)  # 输出修改后的结果
