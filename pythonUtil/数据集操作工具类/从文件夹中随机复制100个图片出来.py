import os
import random
import shutil

source_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230619_chaoyi_dangshui_data\dangshuitiao-huizong'
destination_dir = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230628_chaoyi_dangshui\train'
num_images = 60

# 获取源目录中所有图片文件的列表
image_files = [file for file in os.listdir(source_dir) if file.endswith(('.jpg', '.png', '.jpeg'))]

# 随机选择指定数量的图片文件
selected_files = random.sample(image_files, num_images)

# 复制选中的图片文件到目标目录
for file in selected_files:
    source_path = os.path.join(source_dir, file)
    destination_path = os.path.join(destination_dir, file)
    shutil.copy2(source_path, destination_path)
    print(f"复制文件：{file}")

print("复制完成！")
