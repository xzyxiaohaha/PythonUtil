import os
import argparse

# 定义一个函数，用于统计一个目录下的图片文件数量
def count_images(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            count += 1
    return count

# # 创建一个命令行参数解析器
# parser = argparse.ArgumentParser(description="统计指定目录下的子目录中包含的图片文件数量。")
# parser.add_argument("--directory", metavar="DIRECTORY", type=str, help="指定要统计的目录路径。")
#
# # 解析命令行参数
# args = parser.parse_args()
#
# # 获取要统计的目录路径
# directory = args.directory
directory = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230620_chaoyi_dangshui_data\huanyuan-train'
# 遍历指定目录下的所有子目录
for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    if os.path.isdir(subdir_path):
        # 统计子目录中的图片文件数量
        image_count = count_images(subdir_path)
        print("子目录 %s 中包含 %d 个图片文件。" % (subdir, image_count))
