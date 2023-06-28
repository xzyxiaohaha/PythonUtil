import os
import random
import shutil

source_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230613_chaoyi_houshijing\heji-huanyuan_finall_huanyuan"  # 源目录，包含多个子文件夹
destination_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230613_chaoyi_houshijing\val"  # 目标目录，用于存储复制的图片

# 遍历源目录下的子文件夹
for subdir in os.listdir(source_dir):
    subdir_path = os.path.join(source_dir, subdir)
    if not os.path.isdir(subdir_path):
        continue

    # 获取子文件夹中的所有图片文件
    image_files = [f for f in os.listdir(subdir_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if len(image_files) > 0:
        # 从图片文件列表中随机选择一张图片
        random_image = random.choice(image_files)

        # 创建目标文件夹
        destination_subdir = os.path.join(destination_dir, subdir)
        os.makedirs(destination_subdir, exist_ok=True)

        # 复制随机选择的图片到目标文件夹
        source_image_path = os.path.join(subdir_path, random_image)
        destination_image_path = os.path.join(destination_subdir, random_image)
        shutil.move(source_image_path, destination_image_path)
