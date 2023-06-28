import os
import shutil

source_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230621_chaoyi_houshijing_finall\huanyuan_train\T1AD_huanyinghui\augment"  # 源目录，包含多个子文件夹
destination_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230621_chaoyi_houshijing_finall\huanyuan_train\T1AD_huanyinghui\augment2"  # 目标目录，用于存储复制的图片

# 遍历源目录下的子文件夹
for subdir in os.listdir(source_dir):
    subdir_path = os.path.join(source_dir, subdir)
    if not os.path.isdir(subdir_path):
        continue

    # 创建目标子文件夹
    destination_subdir = os.path.join(destination_dir, subdir)
    os.makedirs(destination_subdir, exist_ok=True)

    # 复制子文件夹中的前四张图片到目标子文件夹
    image_counter = 0
    for root, _, files in os.walk(subdir_path):
        for filename in files:
            if image_counter >= 2:
                break
            if filename.endswith((".jpg", ".jpeg", ".png")):
                source_image_path = os.path.join(root, filename)
                # destination_image_path = os.path.join(destination_subdir, filename)
                destination_image_path = os.path.join(destination_subdir, filename)
                # shutil.copyfile(source_image_path, destination_image_path)
                shutil.copyfile(source_image_path, destination_image_path)
                image_counter += 1
