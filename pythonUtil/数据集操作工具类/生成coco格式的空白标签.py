import os
import json

img_dir = r'F:\pycharm-workspace\zhou\valid\images_null'
json_file = r'F:\pycharm-workspace\zhou\valid\instances_valid_null.json'

# data = {'images': [], 'annotations': [], 'categories': []}
data = {'images': []}

# Define your categories here

import cv2
# Loop over all images in the directory
for img_filename in os.listdir(img_dir):
    if img_filename.endswith('.jpg'):
        # Add image information to the data dictionary
        img = cv2.imread(img_dir+'/'+img_filename)
        Pheight, Pwidth, Pdepth = img.shape
        img_id = len(data['images']) + 1
        img_dict = {'id': img_id, 'file_name': img_filename,'width':Pwidth,'height':Pheight}
        data['images'].append(img_dict)

        # Add dummy annotation information to the data dictionary
        # (you'll need to replace this with your actual annotation data)

# Save the data to a json file
with open(json_file, 'w') as f:
    json.dump(data, f)
