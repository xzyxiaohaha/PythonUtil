# -*- coding = utf-8 -*-
# @Time : 12/12/2022 7:52 PM
# @Author : zyxiao
# @File : yolo_to_voc.py
# @Software : {PyCharm}

from xml.dom.minidom import Document
import os
import cv2


# def makexml(txtPath, xmlPath, picPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
def makexml(picPath, txtPath, xmlPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
    """此函数用于将yolo格式txt标注文件转换为voc格式xml标注文件
    在自己的标注图片文件夹下建三个子文件夹，分别命名为picture、txt、xml
    """
    # dic = {'0': "boat",  # 创建字典用来对类型进行转换
    #        '1': "cat",  # 此处的字典要与自己的classes.txt文件中的类对应，且顺序要一致
    #        }
    # ['huanyuhui', 'kejihui', 'lanhualan', 'qingmeilv', 'songmohei', 'xingtubai',
     #             'huanyuhui_black', 'kejihui_black', 'lanhualan_black', 'qingmeilv_black', 'songmohei_black', 'xingtubai_black','360']
    # dic = {
    #        '0':'huanyuhui',
    # '1':'kejihui',
    # '2':'lanhualan',
    # '3':'qingmeilv',
    # '4':'songmohei',
    # '5':'xingtubai',
    # '6':'huanyuhui_black',
    # '7':'kejihui_black',
    # '8':'lanhualan_black',
    # '9':'qingmeilv_black',
    # '10':'songmohei_black',
    # '11':'xingtubai_black',
    # '12':'360',
    #        }

    # dic = {
    #     '0': '404000217AA',
    #     '1': '404000258AA',
    #     '2': '404000476AA',
    #     '3': '404000478AA',
    #     '4': '404000479AA',
    #     '5': '404000500AA',
    #     '6': '404000638AAABK',
    #     '7': '404000190AA',
    #     '8': '404000385AA',
    #     '9': '404000498AA',
    #     '10': '404000696AA',
    #     '11': '404000637AABBK',
    #     '12': '404000062AA',
    #     '13': '404000137AA',
    #     '14': '404000184AA',
    #     '15': '404000526AA',
    #     '16': '404000719AA',
    #     '17': '404000745AA',
    # }

    dic = {
        '0':'T18_jiguanglv',
    '1':'T18_kejihui',
    '2':'T18_xinkaqibai',
    '3':'T18_xintanjinghei',
    '4':'T1AD_hawanahui',
    '5':'T1AD_huanyinghui',
    '6':'T1AD_jiguanglv',
    '7':'T1AD_kejihui',
    '8':'T1AD_laiyinlan',
    '9':'T1AD_luolanzi',
    '10':'T1AD_nasidakeyin',
    '11':'T1AD_shenyelan',
    '12':'T1AD_xinkaqibai',
    '13':'T1AD_xintanjinghei',
    '14':'T1AD_xueshihong',
    '15':'T26_ganlanhui_bai',
    '16':'T26_ganlanhui_hei',
    '17':'T26_haiyanhui_bai',
    '18':'T26_haiyanhui_hei',
    '19':'T26_xinkaqibai_bai',
    '20':'T26_xinkaqibai_hei',
    '21':'T26_xintanjinghei_bai',
    '22':'T26_xintanjinghei_hei',
    '23':'T26_yizeyin_bai',
    '24':'T26_yizeyin_hei',
        '25':'360',
        '26':'arabic',
    }

    files = os.listdir(txtPath)
    num = 0
    for i, name in enumerate(files):
        num +=1
        # if(num <=1000 ):
        #     continue
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        txtFile = open(txtPath + name)
        txtList = txtFile.readlines()
        if(num == 30):
            print("来咯！")
        img = cv2.imread(picPath + name[0:-4] + ".jpg")
        Pheight, Pwidth, Pdepth = img.shape

        folder = xmlBuilder.createElement("folder")  # folder标签
        foldercontent = xmlBuilder.createTextNode("driving_annotation_dataset")
        folder.appendChild(foldercontent)
        annotation.appendChild(folder)  # folder标签结束

        filename = xmlBuilder.createElement("filename")  # filename标签
        filenamecontent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
        filename.appendChild(filenamecontent)
        annotation.appendChild(filename)  # filename标签结束

        size = xmlBuilder.createElement("size")  # size标签
        width = xmlBuilder.createElement("width")  # size子标签width
        widthcontent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthcontent)
        size.appendChild(width)  # size子标签width结束

        height = xmlBuilder.createElement("height")  # size子标签height
        heightcontent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightcontent)
        size.appendChild(height)  # size子标签height结束

        depth = xmlBuilder.createElement("depth")  # size子标签depth
        depthcontent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthcontent)
        size.appendChild(depth)  # size子标签depth结束

        annotation.appendChild(size)  # size标签结束

        for j in txtList:
            # print(j)
            oneline = j.strip().split(" ")
            object = xmlBuilder.createElement("object")  # object 标签
            picname = xmlBuilder.createElement("name")  # name标签
            namecontent = xmlBuilder.createTextNode(dic[oneline[0]])
            picname.appendChild(namecontent)
            object.appendChild(picname)  # name标签结束

            pose = xmlBuilder.createElement("pose")  # pose标签
            posecontent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(posecontent)
            object.appendChild(pose)  # pose标签结束

            truncated = xmlBuilder.createElement("truncated")  # truncated标签
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)  # truncated标签结束

            difficult = xmlBuilder.createElement("difficult")  # difficult标签
            difficultcontent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultcontent)
            object.appendChild(difficult)  # difficult标签结束

            bndbox = xmlBuilder.createElement("bndbox")  # bndbox标签
            xmin = xmlBuilder.createElement("xmin")  # xmin标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)  # xmin标签结束

            ymin = xmlBuilder.createElement("ymin")  # ymin标签
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)  # ymin标签结束

            xmax = xmlBuilder.createElement("xmax")  # xmax标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)  # xmax标签结束

            ymax = xmlBuilder.createElement("ymax")  # ymax标签
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)  # ymax标签结束

            object.appendChild(bndbox)  # bndbox标签结束

            annotation.appendChild(object)  # object标签结束

        f = open(xmlPath + name[0:-4] + ".xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()

if __name__ == "__main__":
    # picPath = r"F:\pycharm-workspace\fireDataset\images2/"  # 图片所在文件夹路径，后面的/一定要带上
    # txtPath = r"F:\pycharm-workspace\fireDataset\labels2/"  # txt所在文件夹路径，后面的/一定要带上
    # xmlPath = r"F:\pycharm-workspace\fireDataset\labels2_xml/"  # xml文件保存路径，后面的/一定要带上
    picPath = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230621_chaoyi_houshijing_finall\230616_chaoyi_houshijing_finall\images\val/"  # 图片所在文件夹路径，后面的/一定要带上
    txtPath = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230621_chaoyi_houshijing_finall\230616_chaoyi_houshijing_finall\labels\val/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230621_chaoyi_houshijing_finall\230616_chaoyi_houshijing_finall\labels_xml\val/"  # xml文件保存路径，后面的/一定要带上
    makexml(picPath, txtPath, xmlPath)


    # import cv2
    #
    # img = cv2.imread(r"F:\pycharm-workspace\selfCreateDataset\normal\0006082.jpg")
    # path = r"F:\pycharm-workspace\selfCreateDataset\normal\0006082.txt"
    # img = cv2.imread(path[0:-4] + ".jpg")
    # if img is not None:
    #     print("Image loaded successfully")
    #     print(img.shape)
    # else:
    #     print("Failed to load image")
