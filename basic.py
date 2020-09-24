''' cointain all of the funtions need to run program'''
import cv2 
import sys
import numpy as np
import math
import random
import os

def read_image(image_path,image_shade = 0):
	# taking image as black & white return as array format
	return cv2.imread(image_path,image_shade)

def make_dir_if_not_exist(name='server-files') :
	if os.getcwd().split('\\')[-1] != name :
		try :
			os.mkdir(name)
		except:
			pass
		finally :
			os.chdir(name)
	else :
		pass

def back_to_dir(name='server-files') :
	if os.getcwd().split('\\')[-1] == name :
		os.chdir("..")
	else :
		pass

def write_image(img):
	if type(img) != np.ndarray :
		img =create_readable_image(img)

	make_dir_if_not_exist()
	filename = f'{random.randint(10000,99999)}rishi.png'
	cv2.imwrite(filename, img)
	print(f'✅ image is saved as {filename} ')
	back_to_dir()

def image_size(img):
	# return image dimentions in pixles height and length respectivly
	return (len(img),len(img[0]))

def check_image_size_ratio(image):
	if (type(image) is np.ndarray): 
		img = image
	else:
		img = read_image(image)

	height = len(img)
	length = len(img[0])
	# IF YOU WANNA set any limit of time 
	# example image shouls be grater then or wqul to on eweek 
		# if (length/height) >= 1:
		# 	print("✅ great This image have Length by Height ratio of :", round(length/height,2))
		# 	return 
		# else:
		# 	raise Exception('Image should be of proper size use "square" or "long side down rectagle" images : ')
	print("✅ great This image have Length by Height ratio of :", round(length/height,2))
 
		# 

def show_image(img,win_name="Your Image"):
	# show image ESC to exit
	cv2.imshow(win_name,img)
	cv2.waitKey(0)

def create_empty_array(height ,width,dimention=1) :
	# creating empty list of zeros:
	a = np.zeros((int(height/dimention),int(width/dimention))).tolist()
	for i in a:
		for x,j in enumerate(i):
			i[x] = int(j)
	return a

def create_readable_image(img):
	'''convert numpy image to read by cv2 '''
	return np.array(img,dtype ='uint8')

def git_commit_file_for_server(git_im):
	''' create a file which cointain count of commit for daily 
	can be a json file with date {good idea do it !} 
	currently creating txt file '''
	make_dir_if_not_exist()

	if type(git_im) != np.ndarray : 
		git_im = create_readable_image(git_im)
	# returning a transpose of the matrix
	git_im = git_im.transpose()
	# convert it into list 
	git_im = git_im.tolist()

	# provide file with numbers of commit daily  
	with open('git_commits_by_server.txt','w') as file :
		for i in git_im :
			for j in i :
				file.writelines(f'{j}\n')
	file.close()

	print(f'✅ provide a file with numbers of commits for each day ')
	back_to_dir()


# list converting or re arrange it for code providing
def consecutive_list(a):
	'''check if list is consecutive if true return percentage of consecutiveness '''
	count = 1
	for i in range(len(a)) :
		if (i != (len(a)-1)):
			if (a[i] == a[i+1]) :
				# print('same')
				count += 1

	return int((count/len(a))*100)

def same_ele_list(a):
	'''check if image if completely of same colours return percentage of same colour in it'''
	count = 1
	for i in range(len(a)) :
		if i != len(a)-1:
			if (a[i] == a[i+1]) :
				count += 1

	return int((count/len(a))*100)

def other_sorting(l) :
	'''check the real format of the list rather than consecutive_list or same_ele_list
	and provide the sorted list'''

	# check if the list consists of consicutive numbers
	# round numbere of elements give same colours 
	list_len = math.ceil(len(l)/5)

	# create a list to save all the completed temp list 
	result_dict = []
	# create a temp list of elements list of elements  
	temp_list = []
	# remains contain all the remaining elements from the real list
	remain_ele = []

	# making bundles of elements for providing colour code later
	for i in range(len(l)):
		if i != (len(l) -1) :
			# check if we can make a bundle of elements for our requirements
			if abs(l[i] - l[i+1]) <= list_len :
				# check if element is in temp list or in last element of result_dict
				# we may have problem that result_dict is empty	which can be solve by ( (l[i] not in result_dict[-1]) if len(result_dict) != 0 else True )
				if (l[i] not in temp_list) and ( (l[i] not in result_dict[-1]) if len(result_dict) != 0 else True ):
					temp_list.append(l[i])
				# because it already make connection in realative to difference it should be have on list
				temp_list.append(l[i+1])

				# why we using list_len to divide elements bungles
				# because we have only five colour in git 
				if len(temp_list) >= list_len : 
					# clearing the temp list if it is full of length = list_len
					result_dict.append(temp_list)
					temp_list = []

			else: 
				# is element have no neighbours then save him in 
				if (l[i] not in temp_list) and ( (l[i] not in result_dict[-1]) if len(result_dict) != 0 else True ):
					remain_ele.append(l[i])
				# result_dict.append(temp_list)
				# temp_list = []

		else :
			# value is stored in temp_list but not updated in result_dict so we have to update it at last
			if temp_list != []:
				result_dict.append(temp_list)
				temp_list=[]

			if l[i] not in result_dict[-1]:
				result_dict.append([l[i]])


	# now we have to fix or set remaining ele (remain_ele) if any
	if remain_ele != []:
		# run is there is any ele in remain_ele

		# update for if total elements are not much len of result_dict is less then 5 then 
		# get min element and max elements of the list and make them if len is not more then 5
		if (len(result_dict) < 4 ):
			# make list of len 5 
			result_dict = less_len_or_single_ele_list(l)
			remain_ele = []

		else :
			for ele in remain_ele :			
				# for each ele in remain_ele
				store = {}
				for i in range(len(result_dict)) :
					# for each list result_dict
					for j in result_dict[i]:
						if 0 < abs(j-ele) < 50:
							# print(f'element is updated in index of {i}')
							try :
								# check if the dict element have better results before if not update it
								# if give error in comparing that mean it is not there yet create a elemenet
								if abs(j-ele) < list(store.values())[0]:
									# replace first element from the new one
									store[i] = store.pop(list(store.keys())[0]) 
									# store[i] = store[list(store.values())[0]] 
									store[i] = abs(j-ele)

							except :
								# creating first element beacause it fails in compairing in try
								store[i] = abs(j-ele)
				else :
					# if ele have no place arround then it goes in the last element of result_dict
					if store == {}:
						result_dict[-1].append(ele)
						
					else:
						result_dict[list(store.keys())[0]].append(ele)

			remain_ele = []

	# now we have to sort the list according to the nearby elements and murge it 
	if len(result_dict) != 5 :
		# result_dict is not of diserable length 
		if len(result_dict) < 5 :
			# it is possible is of only one len if all the element are of so nearby difference 
			# we can do first that  
			if len(result_dict) == 4 :
				# divide last element of list at index 3  
				result_dict.append([result_dict[-1].pop(-1)])
		
		elif len(result_dict) > 5 :
			# here we have to murge the elements list()
			print(list_len)
			all_len = []
			for i in result_dict :
				if len(i) not in all_len :
					all_len.append(len(i))

			all_len.sort()
			for i in range(len(result_dict)) :
				# there shoud be no interaction with first and last ele at all beacause they are the most light amd dark colours of page 
				if ( i != 0 ) and (i != len(result_dict) -1)  : # beacause it is compairing to itself and next element
					# joining the max and min elements
					if  (i != len(result_dict) -2 ) and ( len(result_dict[i]) == min(all_len)) and ( len(result_dict[i+1]) == max(all_len) ) or ( len(result_dict[i]) == max(all_len)) and ( len(result_dict[i+1]) == min(all_len)) :
						# if of smallest len amd largerst len are placed together
						result_dict.insert(i,result_dict.pop(i+1) + result_dict.pop(i))
						break

					elif (i != len(result_dict) -2 ) and ((len(result_dict[i]) == min(all_len)) and (len(result_dict[i+ 1]) == min(all_len)) ):
						# if min are nearby
						result_dict.insert(i,result_dict.pop(i+1) + result_dict.pop(i))
						break
					
					elif (i != len(result_dict) -2 ):
						if ( len(result_dict[i]) + len(result_dict[i+1]) ) <= (min(all_len)+max(all_len)) :
							result_dict.insert(i,result_dict.pop(i+1) + result_dict.pop(i))
							break

	# print('reallist',l)
	return result_dict

def less_len_or_single_ele_list(a):
	# create_empty_array of all elements 
	return_list = [[],[],[],[],[]]
	# for each element one by one store in return list according to their colour
	for i in a :
		if 0 <= i <= 50:
			return_list[4].append(i) 
		elif 51 <= i <= 100 :
			return_list[3].append(i) 
		elif 101 <= i <= 158 :
			return_list[2].append(i) 
		elif 151 <= i <= 200 :
			return_list[1].append(i) 
		elif 201 <= i <= 255:
			return_list[0].append(i) 

	return return_list




if __name__ == "__main__":
	# python filename.py <image path>
	img = read_image(sys.argv[1])
	print('Dimentions of image is :',image_size(img))
	check_image_size_ratio(img)
	show_image(img)
