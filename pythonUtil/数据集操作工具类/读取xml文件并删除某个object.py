import os
import xml.etree.ElementTree as ET

# 指定目标对象
target_objects = ['dangshui', 'dangshui2', 'dangshui3']

def remove_objects(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    objects = root.findall('object')
    for obj in objects:
        name = obj.find('name').text
        if name in target_objects:
            root.remove(obj)

    # 保存修改后的 XML 文件
    tree.write(xml_file)

# 指定目录路径
directory = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230619_chaoyi_dangshui_data\huanyuan-val2-xml'

# 遍历目录下的 XML 文件
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        xml_file = os.path.join(directory, filename)
        remove_objects(xml_file)
        print(f'Removed objects in {filename}')

print('Finished removing objects from XML files.')
