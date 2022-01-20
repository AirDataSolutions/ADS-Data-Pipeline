import os
import subprocess

 #get list of all files and directories and the amount of them
path = "C://Users//DataWing Global//Desktop//Pipeline//input"
dir_list = os.listdir(path)
number_of_elements = len(dir_list)
a_path = 'C://Users//DataWing Global//Desktop//Pipeline//batch//' #Used for stringing file paths together
a_filetype = ".bat"                                               #^^^^^
b_filetype = "dtm.tif"

#Removes .las in filename to be used in path for batch files
lst = [os.path.splitext(x)[0] for x in dir_list]        #idk what x is but stackoverflow probaly did

for i in range(len(lst)):                                         #For loop for cycling arrays to make batch scripts for each .las
    joined_path = os.path.join(a_path, lst[i] + a_filetype)        #combined new path of location
    mybat = open(joined_path,'w+')                                #Creates batch file, Can't comment below so. Root is set to location of batch file to activate pdal in cmd, call batch scipt, activate pdalpy to open evnviroment. go to data input directory, run needed pdal commands
    mybat.write('''set root= C://conda//Scripts
    call %root%//activate.bat
    call activate pdalpy
    cd C://Users//DataWing Global//Desktop//Pipeline//input
    pdal translate {} {} --writers.gdal.resolution=0.5\ \ --writers.gdal.window_size=16'''.format(dir_list[i], lst[i] + b_filetype)) ## {}{} input for file name variables, Window_size fills in 'NO_DATA' holes
    mybat.close()                                                 #IDFK stops the batch shit ig?
    subprocess.call([r'C://Users//DataWing Global//Desktop//Pipeline//batch//{}'.format(lst[i] + a_filetype)]) #runs batch file
    i+1
