import os
import shutil

# 设置jpg文件所在的文件夹路径
jpg_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230627_chaoyi_dangshui\0627finall\images\val'

# 设置txt文件所在的文件夹路径
txt_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230627_chaoyi_dangshui\images\labels_xml'

# 设置目标文件夹路径
target_folder = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230627_chaoyi_dangshui\0627finall\labels_xml\val'

# 遍历jpg文件夹下的所有jpg文件
for jpg_file in os.listdir(jpg_folder):
    if jpg_file.endswith('.jpg'):
        # 构建对应的txt文件路径
        txt_file = os.path.join(txt_folder, jpg_file[:-4] + '.xml')
        # 判断txt文件是否存在
        if os.path.exists(txt_file):
            # 构建目标文件路径
            target_file = os.path.join(target_folder, os.path.basename(txt_file))
            # 移动txt文件到目标文件夹
            shutil.copy2(txt_file, target_file)
            print(f'copy {txt_file} to {target_file}')
