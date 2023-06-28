import os
import shutil
import xml.etree.ElementTree as ET

# 指定VOC格式的XML文件和对应的图片所在的目录

xml_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-fangxiangpan230626_2\labels\val_xml'
img_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230620_chaoyi_dangshui_data\230620_chaoyi_dangshui_finall\images\train'

# 指定目标文件夹
output_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230620_chaoyi_dangshui_data\230620_chaoyi_dangshui_finall\huanyuan_train'

# 读取XML文件列表
xml_files = [f for f in os.listdir(xml_dir) if f.endswith('.xml')]

# 遍历XML文件列表，将对应的图片文件复制到目标文件夹中
for xml_file in xml_files:
    # 解析XML文件
    tree = ET.parse(os.path.join(xml_dir, xml_file))
    root = tree.getroot()
    # 获取图片文件名
    img_name = root.find('filename').text
    # 获取图片类别
    obj = root.find('object')

    if obj is None:
        print(img_name)
        continue


    cls_name = obj.find('name').text
    # print(cls_name)
    # if cls_name == '360':
    #     continue
    # 拼接源图片路径
    img_path = os.path.join(img_dir, img_name)
    # 判断图片文件是否存在
    if os.path.exists(img_path):
        # 拼接目标文件路径
        cls_dir = os.path.join(output_dir, cls_name)
        if not os.path.exists(cls_dir):
            os.makedirs(cls_dir)
        output_path = os.path.join(cls_dir, img_name)
        # 复制图片文件到目标文件夹
        shutil.copyfile(img_path, output_path)
        # shutil.move(img_path, output_path)


#huanyuhui_black_left_4_13-25.jpg
# right_4_44-18.jpg