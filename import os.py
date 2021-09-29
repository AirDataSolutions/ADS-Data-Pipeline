import os

path = 'c:\\temp\\elevation\\lidar_laz' #Change to Input Folder Destination for LiDAR Data. 
										#Right click the foler copy adress as text and paste, MAKE SURE THERES TWO \\'s
files = os.listdir(path)

print("The length of the list is: ", len(files))
for f in files:
	print(f)

	#For loop needed to compare the length of the list every few seconds until they equal eachother a required number of times
	#to ensure all files have been placed and are ready to be processed together
	#Alternative: have an empty .txt file called Go.txt and when that file is seen in the list the rest of the process will continue 
	#This could be valuable in future development in case we need input data for project to project it could be placed there.
