import os
import shutil

folder_t = "folder_T"
folder_v = "folder_V"

if not os.path.exists(folder_t):
    os.makedirs(folder_t)
if not os.path.exists(folder_v):
    os.makedirs(folder_v)

source_folder = "DJI_202405071327_004_Site-H1"

for filename in os.listdir(source_folder):
    file_name, file_extension = os.path.splitext(filename)
    # print(filename);
    print(file_name);
    # print(file_extension);
    if  file_name.endswith == "T":
        shutil.move(os.path.join(source_folder, filename), os.path.join(folder_t, filename))
    elif file_name.endswith == "V":
        shutil.move(os.path.join(source_folder, filename), os.path.join(folder_v, filename))
