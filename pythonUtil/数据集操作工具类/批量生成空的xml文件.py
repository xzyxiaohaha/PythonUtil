# -*- coding = utf-8 -*-
# @Time : 5/5/2023 10:53 AM
# @Author : zyxiao
# @File : 批量生成空的xml文件.py
# @Software : {PyCharm}
import os
import xml.dom.minidom

img_path = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230615_chaoyi_houshijing\0616xinzeng\images2'
xml_path = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230615_chaoyi_houshijing\0616xinzeng\labels_xml2/'
for img_file in os.listdir(img_path):
    img_name = os.path.splitext(img_file)[0]

    # create an empty dom document object
    doc = xml.dom.minidom.Document()
    # creat a root node which name is annotation
    annotation = doc.createElement('annotation')
    # add the root node to the dom document object
    doc.appendChild(annotation)

    # add the folder subnode
    folder = doc.createElement('folder')
    folder_text = doc.createTextNode('VOC2012')
    folder.appendChild(folder_text)
    annotation.appendChild(folder)

    # add the filename subnode
    filename = doc.createElement('filename')
    filename_text = doc.createTextNode(img_file)
    filename.appendChild(filename_text)
    annotation.appendChild(filename)

    # add the path subnode
    path = doc.createElement('path')
    path_text = doc.createTextNode(img_path + img_file)
    path.appendChild(path_text)
    annotation.appendChild(path)

    # add the source subnode
    source = doc.createElement('source')
    database = doc.createElement('database')
    database_text = doc.createTextNode('Unknown')
    source.appendChild(database)
    database.appendChild(database_text)
    annotation.appendChild(source)

    # add the size subnode
    size = doc.createElement('size')
    width = doc.createElement('width')
    width_text = doc.createTextNode('1920')
    height = doc.createElement('height')
    height_text = doc.createTextNode('1080')
    depth = doc.createElement('depth')
    depth_text = doc.createTextNode('3')
    size.appendChild(width)
    width.appendChild(width_text)
    size.appendChild(height)
    height.appendChild(height_text)
    size.appendChild(depth)
    depth.appendChild(depth_text)
    annotation.appendChild(size)

    # add the segmented subnode
    segmented = doc.createElement('segmented')
    segmented_text = doc.createTextNode('0')
    segmented.appendChild(segmented_text)
    annotation.appendChild(segmented)

    # write into the xml text file
    # os.open(xml_path + '%s.xml' % img_name)
    fp = open(xml_path + '%s.xml' % img_name, 'w+')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')
    fp.close()