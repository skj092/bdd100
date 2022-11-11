# This script will delete all the labels from the yolo labels except car 

import os
import glob
import shutil

# Path to the folder containing the yolo labels
path = 'testval'

# Path to the folder where you want to save the modified labels
save_path = 'testval'

# label code for car
car = 2

for filename in os.listdir(path):
    # continue if the file is classes.txt
    if filename == 'classes.txt':
        continue
    if filename.endswith(".txt"):
        with open(os.path.join(path, filename), 'r') as f:
            lines = f.readlines()
            f.close()
        with open(os.path.join(save_path, filename), 'w') as f:
            for line in lines:
                if int(line.split(' ')[0]) == car:
                    f.write(line)
            f.close()