# -*- coding = utf-8 -*-
# @Time : 5/5/2023 7:49 PM
# @Author : zyxiao
# @File : 计算均值和方差.py
# @Software : {PyCharm}
import torch
from torchvision.datasets import ImageFolder


# def getStat(train_data):
#     '''
#     Compute mean and variance for training data
#     :param train_data: 自定义类Dataset(或ImageFolder即可)
#     :return: (mean, std)
#     '''
#     print('Compute mean and variance for training data.')
#     print(len(train_data))
#     train_loader = torch.utils.data.DataLoader(
#         train_data, batch_size=1, shuffle=False, num_workers=0,
#         pin_memory=True)
#     mean = torch.zeros(3)
#     std = torch.zeros(3)
#     for X, _ in train_loader:
#         for d in range(3):
#             mean[d] += X[:, d, :, :].mean()
#             std[d] += X[:, d, :, :].std()
#     mean.div_(len(train_data))
#     std.div_(len(train_data))
#     return list(mean.numpy()), list(std.numpy())
#
#
# if __name__ == '__main__':
#     train_dataset = ImageFolder(root=r'D:\cifar10_images\test')
#     print(getStat(train_dataset))




import os
import numpy as np
import cv2

files_dir = r'F:\pycharm-workspace\selfCreateDataset\images/'
files = os.listdir(files_dir)

R = 0.
G = 0.
B = 0.
R_2 = 0.
G_2 = 0.
B_2 = 0.
N = 0

for file in files:
    img = cv2.imread(files_dir+file)
    print(files_dir+file+" is calculate")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img)
    h, w, c = img.shape
    N += h*w

    R_t = img[:, :, 0]
    R += np.sum(R_t)
    R_2 += np.sum(np.power(R_t, 2.0))

    G_t = img[:, :, 1]
    G += np.sum(G_t)
    G_2 += np.sum(np.power(G_t, 2.0))

    B_t = img[:, :, 2]
    B += np.sum(B_t)
    B_2 += np.sum(np.power(B_t, 2.0))

R_mean = R/N
G_mean = G/N
B_mean = B/N

R_std = np.sqrt(R_2/N - R_mean*R_mean)
G_std = np.sqrt(G_2/N - G_mean*G_mean)
B_std = np.sqrt(B_2/N - B_mean*B_mean)

print("R_mean: %f, G_mean: %f, B_mean: %f" % (R_mean, G_mean, B_mean))
print("R_std: %f, G_std: %f, B_std: %f" % (R_std, G_std, B_std))


# R_mean: 113.414338, G_mean: 104.663787, B_mean: 90.194004
# R_std: 71.098730, G_std: 67.739814, B_std: 69.458805