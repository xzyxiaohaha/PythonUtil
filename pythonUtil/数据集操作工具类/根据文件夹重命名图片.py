import os
import shutil

def rename_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # if file.lower().endswith(('.xml')):
            # if file.lower().endswith(('.txt')):
                # 获取文件的完整路径
                file_path = os.path.join(root, file)

                # 获取文件所在的目录路径
                folder_path = os.path.dirname(file_path)

                # 获取目录路径的层级
                folder_levels = folder_path.split(os.sep)

                # 构建新的文件名
                new_file_name = '_'.join(folder_levels) + '_' + file


                #############此处需要改成路径长度+1，注意路径不要带“/”或者“\”######################
                new_file_name = "0628add_" + new_file_name[77:]
                # new_file_name = new_file_name[:17]+'_l'+new_file_name[35:]
            # '0627add_dangshui2_0627add_dangshui2eft_6_02-13.jpg'
                # 构建新的文件路径
                new_file_path = os.path.join(folder_path, new_file_name)

                # 重命名文件
                shutil.move(file_path, new_file_path)
                print(f"Renamed {file_path} to {new_file_path}")

# 示例用法
directory = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230628_chaoyi_dangshui\images\val'

rename_images(directory)
