import cv2
import numpy as np

def modify_hsv(image, hue_shift, saturation_scale, value_scale):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    # 调整Hue（色调）
    h = (h + hue_shift) % 180

    # 调整Saturation（饱和度）
    s = np.clip(s * saturation_scale, 0, 255).astype(np.uint8)

    # 调整Value（亮度）
    v = np.clip(v * value_scale, 0, 255).astype(np.uint8)

    modified_hsv_image = cv2.merge((h, s, v))
    modified_image = cv2.cvtColor(modified_hsv_image, cv2.COLOR_HSV2BGR)

    return modified_image


# 读取原始图片
image_path = r'D:\xzy\pycharm-workspace\yolov5-6.0\data\230626_chaoyi_houshijing\images\train\augment_T18_kejihui_2023-04-23-19-34-08_1.jpg'
original_image = cv2.imread(image_path)

# 调整图片大小
resized_image = cv2.resize(original_image, (500, 500))

# 调整HSV值
hue_shift = 20  # 色调偏移量
saturation_scale = 1.5  # 饱和度缩放系数
value_scale = 1.2  # 亮度缩放系数
modified_image = modify_hsv(original_image, hue_shift, saturation_scale, value_scale)

# 展示更改之前和更改之后的图片
cv2.imshow('Original Image', original_image)
cv2.imshow('Modified Image', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
