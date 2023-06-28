# import os
# import shutil
#
# # 指定源文件夹和目标文件夹路径
# img_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\images\train'
# txt_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\labels\train'
# target_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\huanyuan'

import os
import shutil

# 定义源文件夹路径和目标文件夹路径
image_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\images\train'
label_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\labels\train'
output_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-houshijing230529\huanyuan'

# 创建目标文件夹
os.makedirs(output_folder, exist_ok=True)

# 获取所有图片文件名
image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg") or f.endswith(".png")]

# 遍历图片文件
for image_file in image_files:
    # 获取对应的标注文件名
    label_file = os.path.splitext(image_file)[0] + ".txt"

    # 检查标注文件是否存在
    if not os.path.exists(os.path.join(label_folder, label_file)):
        continue

    # 读取标注文件的第一行内容
    with open(os.path.join(label_folder, label_file), "r") as f:
        first_line = f.readline()
        if not first_line:
            continue

    # 获取标注文件中的类别
    class_name = first_line.split()[0]

    # 将相同类别的图片复制到指定文件夹中
    class_output_folder = os.path.join(output_folder, class_name)
    os.makedirs(class_output_folder, exist_ok=True)
    shutil.copy(os.path.join(image_folder, image_file), class_output_folder)

print("复制完成！")
