# -*- coding = utf-8 -*-
# @Time : 1/12/2023 11:53 PM
# @Author : zyxiao
# @File : moveFile.py
# @Software : {PyCharm}
import os
import shutil

#基础方法：复制文件到指定目录下
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
def moveFile1():
    path_in = r"F:\Undergraduate-graduation-design\deliver_dataset\lables"  # 需要修改的标签文件夹
    images_save_path = r"F:\Undergraduate-graduation-design\deliver_dataset\label_image/"
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    for epoch in file_in:
        # print(epoch[:-4])
        mycopyfile(r"F:\Undergraduate-graduation-design\deliver_dataset\images/" + epoch[:-4]+".jpg", images_save_path)

# 切割数据集，训练集/验证集/测试集
def PartitionDataSet():
    path_in = r"F:\公司\鲸梦科技\螺栓素材\labels\train"  # 需要修改的标签文件夹
    images_save_path = r"F:\公司\鲸梦科技\螺栓素材\images\val/"
    labels_save_path = r"F:\公司\鲸梦科技\螺栓素材\labels\val/"
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    print(file_in)
    # print(len(file_in))
    flag = 0
    class_name1 = ".txt"
    class_name2 = ".jpg"
    for i in range(0, len(file_in), 8):
        print(file_in[i][:-4])
        labels = file_in[i][:-4] + class_name1
        images = file_in[i][:-4] + class_name2
        mycopyfile("F:/公司/鲸梦科技/螺栓素材/images/train/" + images, images_save_path)
        mycopyfile("F:/公司/鲸梦科技/螺栓素材/labels/train/" + labels, labels_save_path)

if __name__ == '__main__':
    # PartitionDataSet()
    moveFile1()