import os
import random
import shutil

# 源目录，包含多个子目录
src_dir = r"D:\xzy\各种颜色\各种颜色\dnagshuitiao-augment"
# 目标目录，用于存放随机复制的图片
dst_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230628_chaoyi_dangshui\train"
# 每个子目录随机复制的图片数量
num_images_to_copy = 3

# 获取源目录下所有子目录的路径
subdirs = [os.path.join(src_dir, d) for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

# 遍历每个子目录，随机复制指定数量的图片到目标目录
for subdir in subdirs:
    # 获取当前子目录下所有图片的路径
    images = [os.path.join(subdir, f) for f in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, f)) and f.endswith(".jpg")]
    # 如果当前子目录下的图片数量小于要复制的数量，就复制所有图片
    num_images = min(len(images), num_images_to_copy)
    # 从当前子目录下所有图片中随机选择指定数量的图片
    selected_images = random.sample(images, num_images)
    # 遍历选中的图片，将它们复制到目标目录下
    for image in selected_images:
        shutil.copy(image, dst_dir)
