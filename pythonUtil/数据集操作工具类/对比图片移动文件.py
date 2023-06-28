import os
import shutil

def move_unique_images(source_folder1, source_folder2, destination_folder):
    # 获取两个源文件夹中的所有文件名
    files1 = os.listdir(source_folder1)
    files2 = os.listdir(source_folder2)

    # 仅存在于一个文件夹中的文件
    unique_files = set(files1) ^ set(files2)

    for unique_file in unique_files:
        # 构建文件路径
        if unique_file in files1:
            source_file = os.path.join(source_folder1, unique_file)
        else:
            source_file = os.path.join(source_folder2, unique_file)

        # 移动文件到目标文件夹
        shutil.move(source_file, destination_folder)
        print(f"Moved {source_file} to {destination_folder}")

# 示例用法
source_folder1 = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\images\augment'
source_folder2 = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230526\augument\augement\val'
destination_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\images\augment2'

move_unique_images(source_folder1, source_folder2, destination_folder)
