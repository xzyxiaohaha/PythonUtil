import os

def find_unique_jpg(jpg_folder, xml_folder):
    # 获取jpg文件夹中的所有文件名
    jpg_files = set(os.listdir(jpg_folder))

    # 获取xml文件夹中的所有文件名
    xml_files = set(os.listdir(xml_folder))

    # 找出jpg文件夹中不在xml文件夹中的文件
    unique_jpg_files = jpg_files - xml_files

    return unique_jpg_files

# 示例用法
jpg_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-fangxiangpan230530-train\images\train\404000599AA'
xml_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-fangxiangpan230530-train\labels\train_xml'

unique_jpg_files = find_unique_jpg(jpg_folder, xml_folder)

print("Unique JPG files:")
for file in unique_jpg_files:
    print(file)
