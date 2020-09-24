from basic import *
import numpy as np
import math
import sys


def chiseler(image_name):
	# changing the image pixle for git hub format
	'''
	this will convert the image in the format such that required
	and return block dimention amd image 
	''' 

	#first reading height if it is divisible by week if not
	#if remender of the the height by week is odd then just leave down pixle of image and 
	#devide it into 7 parts 

	img = read_image(image_name)
	# convert image into list format for chisel
	img = img.tolist()
	height, width = image_size(img)
	Initial = f'\t-Initial dimentions : Height -{height}  Width -{width} '

	##########################################################################################
	# height chiseling

	# check if there is any extra pixle line there 
	extra_height_pixle = height % 7

	if extra_height_pixle != 0:
		print('✅ chisel some pixles here')
		# print(extra_height_pixle)
		# check if the extra pixle is odd or even 
		if extra_height_pixle % 2 == 0:
			# divide them equaly to top and bottom
			removeable_lines = int(extra_height_pixle / 2)
			extra_top = removeable_lines
			extra_bottom = removeable_lines
			print('\t-even height chiseling ->','extra_top',extra_top,' extra_bottom',extra_bottom)
			for _ in range(extra_bottom): # or extra_top or removeable_lines
				# always remove the first and last element of code
				img.remove(img[0])
				img.remove(img[-1])

		else:
			# divide them by giving one more to bottom line therefore it remove one extra line from the bottom
			# the use of math.ceil is to always get proceding number 
			removeable_lines = math.ceil(extra_height_pixle/2)
			if removeable_lines != 1:
				extra_top = removeable_lines - 1  
				extra_bottom = removeable_lines
			else:
				extra_top = 0
				extra_bottom = removeable_lines

			print('\t-odd height chiseling ->','extra_top',extra_top,' extra_bottom',extra_bottom)
			# real chiseling here
			for i in range(extra_bottom): # here it should be extra_bottom because extra_top can be 0 here
				# extra_bottom consist of equaly to "extra_top" + 1
				# so one time of extra we wanna be delete only one ok last line and all the other cases we wanna delete both 
				if i == 0:
					img.remove(img[-1]) # wanna remove down most element here
				if i != 0:
					img.remove(img[0])		
					img.remove(img[-1])		

	else:
		pass


	#############################################################################################

	# updating height and width variables
	height, width = image_size(img)
	# print(height,width)

	# dimentions of that block
	dimnention = height/7

	############################################################################################
	extra_width_pixle = width%dimnention

	if extra_width_pixle != 0:
		# check if there is any extra pixle then require
		if extra_width_pixle%2 == 0 :
			# check if it is even then divide them equally amd remove them from the list 
			removeable_element = int(extra_width_pixle/2)
			extra_right = removeable_element
			extra_left = removeable_element

			print('\t-even width chiseling ->','extra_right',extra_right,' extra_left',extra_left)

			for i in img :
				for _ in range(extra_left) : # can be removeable_element or extra_right because it even condition 
					# removeing element from the the list 
					i.remove(i[-1])
					i.remove(i[0])

		else:
			# check if it is odd then divide them equally and give remaing one to left amd remove them from the list 
			removeable_element = math.ceil(extra_width_pixle/2)
			if removeable_element != 1:
				extra_right = removeable_element - 1
				extra_left = removeable_element
			else:
				extra_right = 0
				extra_left = removeable_element
			print('\t-odd width chiseling ->','extra_right',extra_right,' extra_left',extra_left)

			# print((img))

			for i in img :
				for j in range(extra_left) : # odd so it has to be extra_left  
					# removeing element from the the list 
					if j == 0:
						i.remove(i[0]) # wanna remove left most element here
					if j != 0 :
						i.remove(i[-1])
						i.remove(i[0])

	# updating after width chiseler 
	height, width = image_size(img)
	print(Initial)
	print('\t-Ending dimentions : Height -',height,'Width -',width)


	img = np.array(img,dtype ='uint8')

	return (int(dimnention) ,img )


# chiseler('1.jpeg')

if __name__ == '__main__':
	# example to run
	'''python confirm.py <image name>'''
	'''python confirm.py 3.jpeg'''
	chiseler(sys.argv[1])