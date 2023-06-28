# -*- coding = utf-8 -*-
# @Time : 5/4/2023 9:47 AM
# @Author : zyxiao
# @File : SOS (Start of Scan).py
# @Software : {PyCharm}


# from PIL import Image
# import os
#
# dir_path = r'F:\pycharm-workspace\自制火灾数据集\images'
#
# for filename in os.listdir(dir_path):
#     if filename.endswith('.jpg') or filename.endswith('.jpeg'):
#         try:
#             with Image.open(os.path.join(dir_path, filename)) as img:
#                 if(img.verify()==None):
#                     print(f"{filename} is ok!")
#                 else:
#                     print(f"{filename} is invalid: {e}==================================")
#         except Exception as e:
#             print(f"{filename} is invalid: {e}==================================")



from PIL import Image
# import os
# import numpy as np
# path = "F:\pycharm-workspace\自制火灾数据集\images"
#
# for filename in os.listdir(path):
#     try:
#         img = Image.open(os.path.join(path, filename))
#         img_arr = np.array(img)
#         img_from_arr = Image.fromarray(img_arr)
#         img_from_arr.save(os.path.join(path, f"{filename[:-4]}_new.jpg"))
#     except Exception as e:
#         print(f"{filename} is invalid: {e}")


# from PIL import Image
# import os
# import numpy as np
# path = r"F:\pycharm-workspace\自制火灾数据集\images\0003495.jpg"
# img = Image.open(path)
# img_arr = np.array(img)
# img_from_arr = Image.fromarray(img_arr)
# img_from_arr.save(os.path.join(path, f"{path}_new.jpg"))



# import cv2
# import os
#
# def check_image(path):
#     try:
#         img = cv2.imread(path)
#         if img is None:
#             return False
#         else:
#             return True
#     except:
#         print(f"{path} invalid ===============================")
#         return False
#
# if __name__ == '__main__':
#     folder_path = r"F:\HomemadeFireData_coco\train"
#     num = 0
#     for filename in os.listdir(folder_path):
#         if filename.endswith('.jpg') or filename.endswith('.png'):
#             path = os.path.join(folder_path, filename)
#             if check_image(path):
#                 print(f"{filename} is a valid image.")
#                 num += 1
#             else:
#                 print(f"{filename} is an invalid image.=============================")
#                 num += 1
#     print(num)






# from PIL import Image
# import os
# import numpy as np
# path = r"F:\HomemadeFireData_coco\train"
#
# for filename in os.listdir(path):
#     try:
#         img = Image.open(os.path.join(path, filename))
#         img.load()
#         print("valid image file:" + filename)
#     except IOError:
#         print("Invalid image file:================="+filename)


import cv2
import os

folder_path = r"F:\pycharm-workspace\fireDataset\NormalImage"  # 图片文件夹路径

for file_name in os.listdir(folder_path):
    try:
        img = cv2.imread(os.path.join(folder_path, file_name))
        print(f"{file_name} valid ")
        # 在这里加入对图片的处理代码
    except cv2.error:
        print(f"{file_name} is not a valid JPEG image.================")
