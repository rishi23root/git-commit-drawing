import time
import threading
import datetime
from git_push import runner 

# read server_commit file to make commit 
def file_reader(filename,username,password):

	with open(filename) as file :
		# read file and store data in a list which will use in a loop 
		list1 =	[int(i.replace('\n','')) for i in  file.readlines()]
		# close the file
		file.close()

	# if list is not empty
	if list1 != []:
		print(f'{len(list1)} days will be required to complete task ')
		opi = input('Type [y/n] to continue :')
		if opi.capitalize() != 'Y':
			return

		loging = open('datetimelog.txt','a')

		for i in list1:
			# loging all activity
			date = datetime.datetime.now()     
			day = date.strftime("%A")          
			loging.writelines(f'making {i} commits on Day:{day} Date:{date.day}/{str(date.now().month).zfill(2)}/{date.now().year} \n')
			for commit in range(i):
			    runner(username,password)

			print('ON sleep for next 24h')
			time.sleep(24*60*60) # CHANGE TO 24*60*60 FOR A DAY LONG SLEEP 

		loging.close()
	else :
		raise Exception(f'wrong file : check the file or re-right the file {file_name} ')



file_name='git_commits_by_server.txt'

# create a file to commit in github 
# sort out a way to commit in github threw commendline without any human intrection
username = input('Enter your github account username :')
password = input('Enter your github account password :')

file_reader(file_name,username,password)