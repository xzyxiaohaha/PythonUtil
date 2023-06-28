import os

def add_prefix_to_images(directory, prefix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                original_path = os.path.join(root, file)
                new_filename = prefix + file
                new_path = os.path.join(root, new_filename)
                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} -> {new_path}")
            # if file.lower().endswith(('.xml')):
            #     original_path = os.path.join(root, file)
            #     new_filename = prefix + file
            #     new_path = os.path.join(root, new_filename)
            #     os.rename(original_path, new_path)
            #     print(f"Renamed: {original_path} -> {new_path}")

# 指定目录路径和要添加的前缀
directory_path = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\qingdao-fangxiangpan230530-train\redundance_heibaD:\xzy\pycharm-workspace\yolov5-6.0\data\230621_chaoyi_houshijing_finall\huanyuan_val\augment0625"
prefix = "redundance2"

# 调用函数添加前缀
add_prefix_to_images(directory_path, prefix)
