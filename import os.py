#The code so far imports a list of all the files in a certain diretory that the user inputs. It then searches for a file that will be put in manually as a part of the workflow.
#This file will be used to store the user inputs for later use. 

import os
import shutil

path = 'Q:\\Lidar\\AUTOMATION\\RAWdata' #Change to Input Folder Destination for LiDAR Data. Right click the foler copy adress as text and paste, MAKE SURE THERES TWO \\'s
files = os.listdir(path)

#print("The length of the list is: ", len(files)) this was just testing that the function worked. 
#The code below is storing the length of the list as an int and using a temp variable to compare itself for verification that the system has loaded in all files. 
int num_files
int temp			 #Old ? -Jack
num_files = len(files)

#Printing out the list of files
for f in files:
	print(f)

#Seeing if the go.txt file is in the list or it will not continue. @Jack make sure every part of the code from now on is properly indented. Moving files.
#Absolute paths

src_path = r"Q:\\Lidar\\AUTOMATION\\RAWdata
dst_path = r"Q:\\Lidar\\AUTOMATION\\HxmapAutomation
input_path = r"Q:\\Lidar\\AUTOMATION\\Userinput

if(files.count("go.txt")>=1) 
	shutil.move(src_path, dst_path)
	shutil.move(src_path, input_path)





	
