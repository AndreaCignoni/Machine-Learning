import os
import shutil
from sklearn.model_selection import train_test_split

#Paths
input_folder = "sorted_dataset/"  #Path to sorted dataset (sorted from initialSort.py)
output_folder = "split_dataset/"  #Path to store train/val/test splits

#Split ratios
train_ratio = 0.6
val_ratio = 0.2
test_ratio = 0.2

#Create train/val/test folder
for split in ["train", "val", "test"]:
    split_path = os.path.join(output_folder, split)   #Make the dir if it doesn't exist
    if not os.path.exists(split_path):
        os.makedirs(split_path)

#For each flower folder
for flower in os.listdir(input_folder):
    flower_path = os.path.join(input_folder, flower)
    if not os.path.isdir(flower_path):
        continue
    
    images = os.listdir(flower_path)    #get the images from each flower folder
    
    #Split the data
    train, temp = train_test_split(images, test_size=(1 - train_ratio), random_state=42)
    val, test = train_test_split(temp, test_size=(test_ratio / (val_ratio + test_ratio)), random_state=42)
    
    #Copy files into respective folders
    for split, split_images in zip(["train", "val", "test"], [train, val, test]):
        split_flower_folder = os.path.join(output_folder, split, flower)    #Make the dir if it doesn't exist
        if not os.path.exists(split_flower_folder):
            os.makedirs(split_flower_folder)
        
        for image in split_images:
            src_path = os.path.join(flower_path, image)
            dest_path = os.path.join(split_flower_folder, image)
            shutil.copy(src_path, dest_path)

print("Worked")
