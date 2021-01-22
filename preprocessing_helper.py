import os
import sys
import os.path
from PIL import Image

import numpy as np

def split_name(file_name):
    return file_name.rsplit('.',1)

def imread(path, is_grayscale = False):
    if (is_grayscale):
        return scipy.misc.imread(path, flatten = True).astype(np.float)
    else:
        return scipy.misc.imread(path).astype(np.float)
        
def convert_img_type(base_directory, path):
    file_path =  base_directory + '/' + path
    new_file_name = ""
    im = Image.open(file_path)
    new_file_name = split_name(path)[0] + ".jpg"
    new_file_path = base_directory + '/' + new_file_name
    
    im.convert("RGB").save(new_file_path)
    im.close()
    os.remove(file_path)
    return new_file_name

def convert_to_jpg(base_directory):
    print ("In progress: File type conversion for folder " + base_directory)
    for path in os.listdir(base_directory):
    
        old_name = base_directory + '/' + path
        
        #convert file to jpg format
        if os.path.isfile(old_name):
            if(split_name(path)[1]).lower() in ['jpg', 'jpeg', 'png', 'jfif']:
                if(split_name(path)[1] != "jpg"):
                    path = convert_img_type(base_directory, path)
            else:
                print("Deleting file " + old_name)
                os.remove(old_name)
        
        else:
           #If it's a subfolder, recursively call rename files on that directory.
           print("Recursing: " + old_name)
           convert_to_jpg(old_name)
    print ("Done: File type conversion for folder " + base_directory)

        
        
def rename_files(base_directory, num):

    print("In progress: File renaming for folder " + base_directory)
    #Get the folder name for base_directory (c:\users\foobar => foobar)
    directory_name = os.path.basename(base_directory)
    #List the files in base_directory
    for path in os.listdir(base_directory):
    
        old_name = base_directory + '/' + path
        
        #If the path points to a file, rename it directory name + '.' + extension
        if os.path.isfile(old_name):
            new_name = base_directory + '/' + directory_name + '_' + str(num) + '.' + split_name(path)[1]
            if not os.path.exists(new_name):
                os.rename(old_name,new_name)
                num = num + 1
            else:
                print("ERROR:"+new_name+" exists")
            
        else:
           #If it's a subfolder, recursively call rename files on that directory.
           print("Recursing: " + old_name)
           rename_files(old_name, 0)
    print("Done: File renaming for folder" + base_directory)

           
if __name__ == '__main__':
    #dataset_path = '/Users/neerajmenon/Documents/Proj/gan/Dataset1'
    dataset_path = sys.argv[1]
    convert_to_jpg(dataset_path)
    rename_files(dataset_path, 0)
