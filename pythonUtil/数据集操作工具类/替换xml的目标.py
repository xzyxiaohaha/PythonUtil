import xml.etree.ElementTree as ET
import os

# 定义需要查找和替换的目标名称
target_name = "T1AD_nasidakayin"
replace_name = "T1AD_nasidakeyin"

# 定义xml文件所在的目录
xml_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230613_chaoyi_houshijing\labels_new_hebing"

# 遍历xml目录下的所有xml文件
for filename in os.listdir(xml_dir):
    if not filename.endswith(".xml"):
        continue

    # 解析xml文件
    xml_path = os.path.join(xml_dir, filename)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    num = 0
    # 查找并替换目标名称
    for obj in root.findall("object"):
        name = obj.find("name").text
        if name == target_name:
            obj.find("name").text = replace_name
            num += 1
            print(num)

    # 保存修改后的xml文件
    tree.write(xml_path)
