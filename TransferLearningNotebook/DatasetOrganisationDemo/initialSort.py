import os
import shutil
import pandas as pd

#Flower names
fNames = [
    'phlox', 'rose', 'calendula', 'iris', 'leucanthemum maximum',
    'bellflower', 'viola', 'rudbeckia laciniata', 'peony', 'aquilegia'
]

#Paths
image_folder = "flower_images/" 
labels_csv = "flower_images/flower_labels.csv" 
output_folder = "sorted_dataset/" 

#Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Load  labels
flower_labels = pd.read_csv(labels_csv)

#Create subfolder for each flower 
for flower in fNames:
    flower_folder = os.path.join(output_folder, flower)
    if not os.path.exists(flower_folder):
        os.makedirs(flower_folder)

#Copy images to folders
for _, row in flower_labels.iterrows():
    file_name = row['file']
    label = row['label']
    fName = fNames[label]
    
    src_path = os.path.join(image_folder, file_name)
    dest_path = os.path.join(output_folder, fName, file_name)
    
    #Copy the files
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)

print("Worked")
