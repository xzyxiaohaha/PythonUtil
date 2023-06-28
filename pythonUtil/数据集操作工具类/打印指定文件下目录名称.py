import os


def print_subdirectories(folder):
    if not os.path.isdir(folder):
        print(f"{folder} 不是一个有效的文件夹路径")
        return

    subdirectories = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    if len(subdirectories) == 0:
        print("该文件夹下没有子目录")
    else:
        print("子目录名称:")
        for subdir in subdirectories:
            print(subdir)


# 指定文件夹路径
folder_path = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230613_chaoyi_houshijing\heji-huanyuan_finall_huanyuan"

# 调用函数打印子目录名称
print_subdirectories(folder_path)
