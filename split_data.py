# This script will split the data into training and validation sets

import os
import random
import shutil
from glob import glob
from tqdm import tqdm

# creating folder for training and validation
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('valid'):
    os.makedirs('valid')

# creading folder for images and labels
if not os.path.exists('train/images'):
    os.makedirs('train/images')
if not os.path.exists('train/labels'):
    os.makedirs('train/labels')

# Creating partitions of the data after shuffeling
# Get the list of all images
image_path_list = glob('valids/*.jpg')
label_path_list = glob('valids/*.txt')

print('number of images: ', len(image_path_list))
print('number of labels: ', len(label_path_list))

# Shuffle the images
random.shuffle(image_path_list)
random.shuffle(label_path_list)

# Calculate the split size
train_size = int(0.9 * len(image_path_list))
valid_size = int(0.1 * len(image_path_list))

# Copy-pasting images
train_image_list = image_path_list[:train_size]
valid_image_list = image_path_list[train_size:train_size+valid_size]

train_label_list = label_path_list[:train_size]
valid_label_list = label_path_list[train_size:train_size+valid_size]

# Train
for image_path in tqdm(train_image_list):
    shutil.copy(image_path, 'train/images')

for label_path in tqdm(train_label_list):
    shutil.copy(label_path, 'train/labels')

# Validation
for image_path in tqdm(valid_image_list):
    shutil.copy(image_path, 'valid/images')


# # Path: train.py