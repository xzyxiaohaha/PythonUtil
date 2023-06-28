import os
import xml.etree.ElementTree as ET

# 指定目录路径
directory = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230619_chaoyi_dangshui_data\230619_chaoyi_dangshui_finall\labels_xml\train'

# 统计每个 object 的标签数量
object_label_count = {}

# 遍历目录下的 XML 文件
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        xml_file = os.path.join(directory, filename)
        tree = ET.parse(xml_file)
        root = tree.getroot()

        objects = root.findall('object')
        for obj in objects:
            name = obj.find('name').text
            if name in object_label_count:
                object_label_count[name] += 1
            else:
                object_label_count[name] = 1

# 打印每个 object 的标签数量
for name, count in object_label_count.items():
    print(f"Object '{name}': {count} labels")

print('Finished counting object labels.')
