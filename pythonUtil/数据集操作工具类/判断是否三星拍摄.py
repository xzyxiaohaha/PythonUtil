# -*- coding = utf-8 -*-
# @Time : 5/6/2023 12:36 AM
# @Author : zyxiao
# @File : 判断是否三星拍摄.py
# @Software : {PyCharm}


import os
from PIL import Image

dir_path = r'F:\pycharm-workspace\zhou\train\images'

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        image_path = os.path.join(dir_path, filename)
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data and 271 in exif_data:
                make = exif_data[271]
                if 'samsung' in make.lower():
                    print(f"{filename} was taken with a Samsung device.============================================================")
            #     else:
            #         print(f"{filename} was not taken with a Samsung device.")
            # else:
            #     print(f"{filename} has no EXIF data.")
