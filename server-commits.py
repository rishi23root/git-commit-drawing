# gitfile reader
import time

# reaming

# create a file to commit in github 
# sort out a way to commit in github threw commendline without any human intrection



# read image from 
file_name='git_commits_by_server.txt'
with open(file_name) as file :
	# read file and store data in a list which will use in a loop 
	list1 =	[int(i.replace('\n','')) for i in  file.readlines()]
	# close the file
	file.close()

# if list is not empty
if list1 != []:
	for i in list1:
		for commit in range(i):
			# one commit to system 
			# create a file to just commit on git 
			print(commit)
		time.sleep(1) # CHANGE TO 24*60*60 FOR A DAY LONG SLEEP 

else :
	raise Exception(f'wrong file : check the file or re-right the file {file_name} ')
