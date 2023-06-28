import os
import shutil

def copy_images(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_directory, file)
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied {source_file_path} to {destination_file_path}")

# 示例用法
source_directory = r'D:\xzy\各种颜色\各种颜色\dnagshuitiao0626\3'
destination_directory = r'D:\xzy\各种颜色\各种颜色\dnagshuitiao0626\images\dangshui2'

copy_images(source_directory, destination_directory)
