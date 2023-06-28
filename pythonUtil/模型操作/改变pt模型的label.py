
import torch
from copy import deepcopy
from models.experimental import attempt_load
from utils.torch_utils import de_parallel
torch_device = torch.device('cuda')
# todo 是否改标签并保存的开关
# change_and_save = True
change_and_save = False
# todo 原始pt路径
original_weights = r'weights/牌照_格栅_尾喉_前logo.pt'
# todo 改标签pt保存路径
# save_weights = r"weights/新中心盖.pt"
# save_weights = r"weights/新轮毂.pt"
save_weights = r"weights/新轮胎.pt"
# save_weights = r"weights/新轮眉.pt"
# save_weights = r"weights/新卡钳.pt"
model = attempt_load(original_weights, map_location=torch_device)
print("原始模型标签为")
print(model.names)# ['SilverShort', 'SilverLong', 'RedShort', 'RedLong']
                  # ['LunguAF', 'LunguM', 'LunguAJ']
                  # ['Chery', 'Kong', 'EXEED']
                  # ['COOPER', 'ATLAS', 'MICHELIN']
                  # ['LunmeiA', 'Kong']
if change_and_save:
    # todo 新标签
    # new_label = ['LunguAD', 'LunguAE', 'LunguAF', '203000262AA']
    # new_label = ['203000111AA', 'Kong', 'EXEED']
    new_label = ['203000195AA', 'ATLAS', '203000387AA']
    # new_label = ['609000643AA', 'Kong']

    if len(new_label)==len(model.names):
        model.names = new_label
        ckpt = {'model': deepcopy(de_parallel(model)).half()}
        torch.save(ckpt, save_weights)
        print("尝试载入改标签模型")
        model_rename = attempt_load(save_weights, map_location=torch_device)
        print("改名模型标签为")
        print(model_rename.names)
    else:
        print("标签数量不一致")