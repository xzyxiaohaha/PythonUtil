import cv2
import os

# 打开本地视频
cap = cv2.VideoCapture(r'D:\vott\230524\source\test.mp4')

# 获取视频帧率
fps = cap.get(cv2.CAP_PROP_FPS)

# 定义计数器
count = 0

# 指定保存图片的目录
save_dir = r'D:\vott\230524\source\frames'

# 创建保存图片的文件夹
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 逐帧读取视频
while cap.isOpened():
    ret, frame = cap.read()

    # 如果读取失败，退出循环
    if not ret:
        break

    # 将每一帧保存成图片
    filename = f'{os.path.splitext(os.path.basename("test.mp4"))[0]}_{int(count // fps)}_{count % int(fps)}.jpg'
    filepath = os.path.join(save_dir, filename)
    cv2.imwrite(filepath, frame)
    print(f'Saved {filename}')

    # 更新计数器
    count += 1

# 释放视频对象
cap.release()
