import os
import xml.etree.ElementTree as ET

# 定义目标顺序
target_order = [
    'cebiao_1', 'cebiao_2', 'cebiao2_1', 'cebiao2_2', 'cebiao3_1', 'cebiao3_2',
    'wsb_tanjinghei_1', 'wsb_tanjinghei_2', 'wsb_kaqibai_1', 'wsb_kaqibai_2',
    'wsb_kejihui_1', 'wsb_kejihui_2', 'wsb_tanjinghei2_1', 'wsb_tanjinghei2_2',
    'wsb_kaqibai2_1', 'wsb_kaqibai2_2', 'wsb_kejihui2_1', 'wsb_kejihui2_2',
    'wsb_ganlanhui_1', 'wsb_ganlanhui_2', 'wsb_yizeyin_1', 'wsb_yizeyin_2',
    'wsb_haiyanhui_1', 'wsb_haiyanhui_2', 'wsb_hei_1', 'wsb_hei_2', 'wsb_bai_1',
    'wsb_bai_2', 'wsb_tanjinghei3_1', 'wsb_tanjinghei3_2', 'wsb_kaqibai3_1',
    'wsb_kaqibai3_2', 'wsb_laiyinlan_1', 'wsb_laiyinlan_2', 'wsb_huanyinghui_1',
    'wsb_huanyinghui_2', 'wsb_luolanzi_1', 'wsb_luolanzi_2', 'wsb_xueshihong_1',
    'wsb_xueshihong_2', 'wsb_nasidakeyin_1', 'wsb_nasidakeyin_2', 'wsb_jiguanglv_1',
    'wsb_jiguanglv_2', 'shenyelan_1', 'shenyelan_2', 'wsb_jiguanglv2_1',
    'wsb_jiguanglv2_2', 'wsb_kejihui3_1', 'wsb_kejihui3_2', 'cebiao4',
    'wsb_jiguanglv3_1', 'wsb_jiguanglv3_2','dangshui', 'dangshui2', 'dangshui3'
]

def reorder_objects(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    objects = root.findall('object')
    object_names = [obj.find('name').text for obj in objects]

    # 按照指定顺序重新排列 objects
    sorted_objects = sorted(objects, key=lambda obj: target_order.index(obj.find('name').text))

    # 清空原始 objects
    for obj in objects:
        root.remove(obj)

    # 添加重新排序后的 objects
    for obj in sorted_objects:
        root.append(obj)

    # 保存修改后的 XML 文件
    tree.write(xml_file)

# 指定目录路径
directory = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230619_chaoyi_dangshui_data\annotations_xml\val'

# 遍历目录下的 XML 文件
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        xml_file = os.path.join(directory, filename)
        reorder_objects(xml_file)
        print(f'Reordered objects in {filename}')

print('Finished reordering objects in XML files.')
