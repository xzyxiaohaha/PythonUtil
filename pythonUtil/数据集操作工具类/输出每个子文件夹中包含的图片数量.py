import os


def count_images_in_subdirectories(folder):
    if not os.path.isdir(folder):
        print(f"{folder} 不是一个有效的文件夹路径")
        return

    subdirectories = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    if len(subdirectories) == 0:
        print("该文件夹下没有子目录")
    else:
        print("子目录中的图片数量:")
        for subdir in subdirectories:
            subdir_path = os.path.join(folder, subdir)
            image_files = [name for name in os.listdir(subdir_path) if
                           os.path.isfile(os.path.join(subdir_path, name)) and name.lower().endswith(
                               (".jpg", ".jpeg", ".png"))]
            image_count = len(image_files)
            print(f"{subdir}: {image_count} 张图片")


# 指定文件夹路径
folder_path = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230613_chaoyi_houshijing\heji-huanyuan_finall_huanyuan"

# 调用函数输出每个子文件夹中的图片数量
count_images_in_subdirectories(folder_path)
