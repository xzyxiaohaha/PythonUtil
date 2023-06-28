import os
import shutil

# 定义源文件夹路径
src_jpg_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230619_chaoyi_dangshui_data\dangshuitiao-huizong"
src_xml_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230615_chaoyi_houshijing\0615finall\labels-xml\huizong"

# 定义目标文件夹路径
dst_dir = r"D:\xzy\pycharm-workspace\yolov5-6.0\data\230619_chaoyi_dangshui_data\dangshuitiao-huizong-xml"

# 遍历jpg文件夹
for file_name in os.listdir(src_jpg_dir):
    # 检查文件是否是jpg格式
    if file_name.endswith(".jpg"):
        # 构造xml文件路径
        xml_file_name = os.path.splitext(file_name)[0] + ".xml"
        xml_file_path = os.path.join(src_xml_dir, xml_file_name)
        # 如果xml文件存在，复制jpg和xml文件到目标文件夹
        if os.path.isfile(xml_file_path):
            jpg_file_path = os.path.join(src_jpg_dir, file_name)
            dst_jpg_file_path = os.path.join(dst_dir, file_name)
            dst_xml_file_path = os.path.join(dst_dir, xml_file_name)
            shutil.copyfile(jpg_file_path, dst_jpg_file_path)
            shutil.copyfile(xml_file_path, dst_xml_file_path)
