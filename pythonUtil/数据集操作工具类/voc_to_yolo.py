import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


def convert(size, box):
    x_center = (box[0] + box[1]) / 2.0
    y_center = (box[2] + box[3]) / 2.0
    x = x_center / size[0]
    y = y_center / size[1]
    w = (box[1] - box[0]) / size[0]
    h = (box[3] - box[2]) / size[1]
    return (x, y, w, h)


def convert_annotation(xml_files_path, save_txt_files_path, classes):
    xml_files = os.listdir(xml_files_path)
    print(xml_files)
    for xml_name in xml_files:
        print(xml_name)
        xml_file = os.path.join(xml_files_path, xml_name)
        out_txt_path = os.path.join(save_txt_files_path, xml_name.split('.')[0] + '.txt')
        out_txt_f = open(out_txt_path, 'w')
        tree = ET.parse(xml_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            # b=(xmin, xmax, ymin, ymax)
            print(w, h, b)
            bb = convert((w, h), b)
            out_txt_f.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == "__main__":
    # 需要转换的类别，需要一一对应
#     classes1 = ['ganlanhui',
# 'huanyinghui',
# 'huimohei',
# 'jiguanglv',
# 'kejihui',
# 'laiyinlan',
# 'luolanzi',
# 'xinkaqibai',
# 'xintanjinghei',
# 'xueshihong',
# 'yizeyin',
# '360',
# 'haiyanhui',
# 'nasidakayin',
# 'shenyelan',
#                 'ganlanhui2']

    # classes1 = ['huanyuhui', 'kejihui', 'lanhualan', 'qingmeilv', 'songmohei', 'xingtubai',
    #             'huanyuhui_black', 'kejihui_black', 'lanhualan_black', 'qingmeilv_black', 'songmohei_black', 'xingtubai_black','360']

    # classes1 = ['404000599AA', '404000664AA', '404000696AA', '404000847AA', 'heibai', 'heihong',
    #             'error']
    classes1 = ['404000599AA', '404000664AA', '404000696AA/', '404000847AA','error']
#     classes1 = ['404000062AA',
# '404000137AA',
# '404000184AA',
# '404000190AA',
# '404000217AA',
# '404000258AA',
# '404000385AA',
# '404000476AA',
# '404000478AA',
# '404000479AA',
# '404000498AA',
# '404000500AA',
# '404000637AABBK',
# '404000638AAABK',
# '404000719AA',
# '404000745AA']
#     classes1 = ['fxp1', 'fxp2','fxp3','fxp4','fxp5','fxp6','fxp7','fxp8']


#     classes1 = ['T18_jiguanglv',
# 'T18_kejihui',
# 'T18_xinkaqibai',
# 'T18_xintanjinghei',
# 'T1AD_hawanahui',
# 'T1AD_huanyinghui',
# 'T1AD_jiguanglv',
# 'T1AD_kejihui',
# 'T1AD_laiyinlan',
# 'T1AD_luolanzi',
# 'T1AD_nasidakeyin',
# 'T1AD_shenyelan',
# 'T1AD_xinkaqibai',
# 'T1AD_xintanjinghei',
# 'T1AD_xueshihong',
# 'T26_ganlanhui_bai',
# 'T26_ganlanhui_hei',
# 'T26_haiyanhui_bai',
# 'T26_haiyanhui_hei',
# 'T26_xinkaqibai_bai',
# 'T26_xinkaqibai_hei',
# 'T26_xintanjinghei_bai',
# 'T26_xintanjinghei_hei',
# 'T26_yizeyin_bai',
# 'T26_yizeyin_hei','360','arabic']
    classes1 = ['cebiao_1', 'cebiao_2', 'cebiao2_1', 'cebiao2_2', 'cebiao3_1', 'cebiao3_2',
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
    'wsb_jiguanglv3_1', 'wsb_jiguanglv3_2','dangshui', 'dangshui2', 'dangshui3']

    # 2、voc格式的xml标签文件路径
    xml_files1 = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230627_chaoyi_dangshui\0627finall\labels_xml\val'
    # 3、转化为yolo格式的txt标签文件存储路径
    save_txt_files1 = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230627_chaoyi_dangshui\0627finall\labels\val'

    convert_annotation(xml_files1, save_txt_files1, classes1)