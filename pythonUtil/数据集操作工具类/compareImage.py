# -*- coding = utf-8 -*-
# @Time : 12/8/2022 12:12 AM
# @Author : zyxiao
# @File : compareImage.py
# @Software : {PyCharm}
import os


# path_in = r"F:\yan究生\组会\火灾识别论文\数据集\Deep Convolutional Neural Networks for Fire-Fire-Detection-Image-Dataset-master\Fire-Detection-Image-Dataset-master\Fire images"  # 待批量重命名的文件夹
# path_in2 = r"F:\yan究生\组会\火灾识别论文\数据集\Deep Convolutional Neural Networks for Fire-Fire-Detection-Image-Dataset-master\Fire-Detection-Image-Dataset-master\labels"  # 待批量重命名的文件夹
# class_name = ".jpg"  # 重命名后的文件名后缀
# class_name2 = ".txt"
# file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
# file_in2 = os.listdir(path_in2)  # 返回文件夹包含的所有文件名
# num_file_in = len(file_in)  # 获取文件数目
# num_file_in2 = len(file_in2)  # 获取文件数目
# print(file_in, num_file_in)  # 输出修改前的文件名
# print(file_in2, num_file_in2)  # 输出修改前的文件名
# for i in file_in2:
#     print(i[:-4])


import os
import cv2
import numpy as np
# 找出两个文件夹中重复的图片，并把重复的内容写入到compareImage.txt中
def compareImage():
    path_in = r"F:\pycharm-workspace\fireDataset\images2"  #需要修改的标签文件夹
    path_in2 = r"F:\pycharm-workspace\fireDataset\Fire-Smoke-Dataset\Fireimages"  # 要修改的图片文件夹
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    file_in2 = os.listdir(path_in2)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    num_file_in2 = len(file_in2)  # 获取文件数目
    print(file_in, num_file_in)  # 输出获取到的文件名和数目
    print(file_in2, num_file_in2)  # 输出获取到的文件名和数目
    flag = 0
    for i in range(0, num_file_in2):
        path2 = path_in2 + "/" + file_in2[i]  # 图片的路径
        print(i,":",path2)
        for j in range(0, num_file_in):
            path = path_in + "/" + file_in[j]  # 标签的路径
            print(i,"-",j, ":", path)
            image1 = cv2.imread(path)
            image2 = cv2.imread(path2)
            # with open('x.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
            #     file.write(str(i)+"-"+str(j) + ":" + path + "\n")
            #     file.close()
            try:
                difference = cv2.subtract(image1, image2)
                result = not np.any(difference)  # if difference is all zeros it will return False
                if result is True:
                    print(path2,"===================================",path)
                    # Note = open('x.txt', mode='a')
                    # Note.write('hello word 你好 '+'\n')  # \n 换行符
                    # Note.close()
                    with open('../compareImage.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                        file.write(path2+"==================================="+path + "\n")
                        file.close()
                # else:
                    # cv2.imwrite("result.jpg", difference)
                    # print("")
            except cv2.error as e:
                continue

#复制文件到指定目录下
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

import shutil   #文件操作库
# compareImage2()通过cv2读取两个文件夹下的图片，如果两个图片相同则直接删除
def compareImage2():
    path_in = r"F:\pycharm-workspace\fireDataset\open_fire\open_fire"  #需要修改的标签文件夹
    path_in2 = r"F:\pycharm-workspace\fireDataset\open_fire\open_fire2"  # 要修改的图片文件夹
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    file_in2 = os.listdir(path_in2)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    num_file_in2 = len(file_in2)  # 获取文件数目
    print(file_in, num_file_in)  # 输出获取到的文件名和数目
    print(file_in2, num_file_in2)  # 输出获取到的文件名和数目
    flag = 0
    save_path = r"F:\pycharm-workspace\fireDataset\open_fire\open_fire_duplicate/"
    for i in range(0, num_file_in2):
        path2 = path_in2 + "/" + file_in2[i]  # 图片的路径
        print(i,":",path2)
        for j in range(0, num_file_in):
            if(j == i):
                continue
            else:
                path = path_in + "/" + file_in[j]  # 标签的路径
                print(i,"-",j, ":", path)
                image1 = cv2.imread(path)
                image2 = cv2.imread(path2)
                # with open('x.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                #     file.write(str(i)+"-"+str(j) + ":" + path + "\n")
                #     file.close()
                try:
                    difference = cv2.subtract(image1, image2)
                    result = not np.any(difference)  # if difference is all zeros it will return False
                    if result is True:
                        print(path2,"===================================",path)
                        # Note = open('x.txt', mode='a')
                        # Note.write('hello word 你好 '+'\n')  # \n 换行符
                        # Note.close()
                        with open('../compareImage.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                            file.write(path2+"==================================="+path + "\n")
                            file.close()
                        # mycopyfile(path2,save_path)
                        shutil.move(path2, save_path)
                        print("正在移除重复照片：", path2)
                    # else:
                        # cv2.imwrite("result.jpg", difference)
                        # print("")
                except cv2.error as e:
                    continue

# deleteSameImage()用于移除compareImage.txt中记录的相同jpg文件
def deleteSameImage():
    # path_in = r"F:\pycharm-workspace\fireDataset\Deep Convolutional Neural Networks for Fire-Fire-Detection-Image-Dataset\Fireimages"  # 需要修改的标签文件夹
    # path_in2 = r"F:\pycharm-workspace\fireDataset\Deep Convolutional Neural Networks for Fire-Fire-Detection-Image-Dataset\labels"  # 要修改的图片文件夹
    class_name2 = ".txt"  # 标签的文件名后缀
    #
    # path = path_in + "/" + class_name       #标签的路径
    # path2 = path_in2 + "/" +  class_name2       #图片的路径
    fileHandler = open("../compareImage.txt", "r")
    # Get list of all lines in file
    listOfLines = fileHandler.readlines()
    # Close file
    fileHandler.close()
    flag = 0
    for line in listOfLines:
        path1 = line.strip()[:-85]   #strip用于去除开头和末端的空格
        str1 = ".jpg"
        path2 = line.strip()[ :line.strip().index(str1)] +class_name2
        # print(path1)
        # print(path2)
        os.remove(path1)
        os.remove(path2)
        flag += 1
    print("一共删除：",flag,"个文件")


def moveFile():
    path_in = r"F:\pycharm-workspace\fireDataset\open_fire\open_fire_labels\txt"  # 需要修改的标签文件夹
    path_in2 = r"F:\pycharm-workspace\fireDataset\open_fire\open_fire"  # 要修改的图片文件夹
    save_path = r"F:\pycharm-workspace\fireDataset\open_fire\savepath2/"
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    file_in2 = os.listdir(path_in2)  # 返回文件夹包含的所有文件名
    num_file_in = len(file_in)  # 获取文件数目
    num_file_in2 = len(file_in2)  # 获取文件数目
    # print(file_in, num_file_in)  # 输出获取到的文件名和数目
    # print(file_in2, num_file_in2)  # 输出获取到的文件名和数目
    className = ".jpg"
    flag = 0
    for epoch in file_in:
        print(epoch[0:7])
        mycopyfile(path_in2 + "/" + epoch[0:7] + ".jpg", save_path)
        flag += 1
    print(flag)

def moveFile2():
    path_in = r"F:\pycharm-workspace\fireDataset\images2"  # 需要修改的标签文件夹
    save_path = r"F:\pycharm-workspace\fireDataset\dataSet_yolov7_format\images\train/"
    file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    for epoch in file_in[0:4000]:
        print(path_in+"/"+epoch)
        mycopyfile(path_in+"/"+epoch, save_path)




if __name__ == '__main__':
    moveFile2()
    # moveFile()
    # path_in = r"F:\pycharm-workspace\fireDataset\images2"  # 需要修改的标签文件夹
    # path_in2 = r"F:\pycharm-workspace\fireDataset\labels2"  # 要修改的图片文件夹
    # file_in = os.listdir(path_in)  # 返回文件夹包含的所有文件名
    # file_in2 = os.listdir(path_in2)  # 返回文件夹包含的所有文件名
    # num_file_in = len(file_in)  # 获取文件数目
    # num_file_in2 = len(file_in2)  # 获取文件数目
    # # print(file_in, num_file_in)  # 输出获取到的文件名和数目
    # # print(file_in2, num_file_in2)  # 输出获取到的文件名和数目
    # for j in range(0,num_file_in):
    #     ha = path_in+"/"+file_in[j]
    #     ha2 = path_in2+"/"+file_in2[j]
    #     if ha[41:48] != ha2[41:48]:
    #         print(ha,"!!!!======",ha2)

    # deleteSameImage()
    # 图片路径
    # compareImage2()
    # path = r"F:\pycharm-workspace\fireDataset\images2\002490.jpg"
    # path2 = r"F:\pycharm-workspace\fireDataset\images2\002968.jpg"
    # image1 = cv2.imread(path)
    # image2 = cv2.imread(path2)
    # try:
    #     difference = cv2.subtract(image1, image2)
    #     result = not np.any(difference)  # if difference is all zeros it will return False
    #     if result is True:
    #         print("两张图片一样")
    #     else:
    #         # cv2.imwrite("result.jpg", difference)
    #         print("两张图片不一样")
    # except cv2.error as e:
    #     print("两个图片大小不一样")




# for j in range(0, num_file_in):
#     path = path_in + "/" + file_in[j]  # 标签的路径
#     # print(path)
#     for i in range(0, num_file_in2):
#         path2 = path_in2 + "/" + file_in2[i]  # 图片的路径
#         # print(path2)
#         image1 = cv2.imread(path)
#         image2 = cv2.imread(path2)
#         try:
#             difference = cv2.subtract(image1, image2)
#             result = not np.any(difference)  # if difference is all zeros it will return False
#             if result is True:
#                 print(path2,"================================",path)
#             # else:
#                 # cv2.imwrite("result.jpg", difference)
#                 # print("")
#         except cv2.error as e:
#             continue


        # image1 = cv2.imread(path)
        # image2 = cv2.imread(path2)
        # # print(image1)
        # # print(type(image1))
        # # print(type(image2))
        # if(image2.any() == image1.any()):
        #     print(path2,"=====",path)





