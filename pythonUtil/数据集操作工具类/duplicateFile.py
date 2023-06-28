# -*- coding = utf-8 -*-
# @Time : 12/10/2022 1:12 PM
# @Author : zyxiao
# @File : duplicateFile.py
# @Software : {PyCharm}
import shutil
import os
import cv2
import numpy as np

# 对一个文件夹下的所有图片去重
# 1.首先排除图片大小不一样的情况，如果图片大小不一样，图片内容也肯定不一样
# 2.使用opencv读取两个图片，使用subtract()判断两个图片是否一样
if __name__ == '__main__':

    load_path = r'F:\pycharm-workspace\zhou\train\images'  # 要去重的文件夹

    save_path = r'F:\pycharm-workspace\zhou\train\images_duplicate'  # 空文件夹，用于存储检测到的重复的照片

    os.makedirs(save_path, exist_ok=True)

    # 获取图片列表 file_map，字典{文件路径filename : 文件大小image_size}

    file_map = {}

    image_size = 0

    # 遍历filePath下的文件、文件夹（包括子目录）

    for parent, dirnames, filenames in os.walk(load_path):

        # for dirname in dirnames:

        # print('parent is %s, dirname is %s' % (parent, dirname))

        for filename in filenames:
            # print('parent is %s, filename is %s' % (parent, filename))

            # print('the full name of the file is %s' % os.path.join(parent, filename))

            image_size = os.path.getsize(os.path.join(parent, filename))

            file_map.setdefault(os.path.join(parent, filename), image_size)

    # 获取的图片列表按 文件大小image_size 排序

    file_map = sorted(file_map.items(), key=lambda d: d[1], reverse=False)
    # print(file_map)
    file_list = []
    file_list2 = []
    for filename, image_size in file_map:
        file_list.append(filename)
        file_list2.append(image_size)

    num = len(file_list)
    flag =0
    for i in range(0,num-1):
        if(file_list2[i]==file_list2[i+1]):

            image1 = cv2.imread(file_list[i])
            image2 = cv2.imread(file_list[i+1])
            try:
                difference = cv2.subtract(image1, image2)
                result = not np.any(difference)  # if difference is all zeros it will return False
                if result is True:
                    print(file_list[i], "==========", file_list[i + 1])
                    with open('../重复2.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                        file.write(file_list[i] + "===================================" + file_list[i+1] + "\n")
                        file.close()
                    flag += 1
            except cv2.error as e:
                continue
            # with open('重复.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
            #     file.write(file_list[i] + "===================================" + file_list[i+1] + "\n")
            #     file.close()
            #     print("正在移除重复照片：", image)

        # print(file_list[i],file_list2[i])
    print(flag)
    # 取出重复的图片

    # file_repeat = []

    # for currIndex, filename in enumerate(file_list):
    #
    #     dir_image1 = file_list[currIndex]
    #
    #     dir_image2 = file_list[currIndex + 1]
    #     # print(dir_image1)
    #     # print(dir_image2)
    #     image1 = cv2.imread(dir_image1)
    #     image2 = cv2.imread(dir_image2)
    #     difference = cv2.subtract(image1, image2)
    #     result = not np.any(difference)
    #
    #     if result is True:
    #
    #         file_repeat.append(file_list[currIndex + 1])
    #
    #         print("\n相同的图片：", file_list[currIndex], file_list[currIndex + 1])
    #
    #     else:
    #
    #         print('\n不同的图片：', file_list[currIndex], file_list[currIndex + 1])
    #
    #     currIndex += 1
    #
    #     if currIndex >= len(file_list) - 1:
    #         break

    # 将重复的图片移动到新的文件夹，实现对原文件夹降重

    # for image in file_repeat:
    #     shutil.move(image, save_path)
    #     print("正在移除重复照片：", image)
