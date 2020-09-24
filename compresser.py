from basic import *
from chiseler import chiseler
import numpy as np
import cv2
import sys

def compresser(img):
	# this file will compress big file in to small one
	dimention ,image = chiseler(img)

	image = image.tolist()
	height,width =image_size(image)

	# array of zeros of requirment dimentions 
	git_image = create_empty_array(height,width,dimention)

	# adding data to git image
	for git_h,i in enumerate(range(0,height,dimention)):
		# give index and value of jump (0,0)
		for x in range(i,i+dimention):
			# go in each line one by one of each jump [profit]!! jump provide index for git_img 
			# so x is each line
			for git_w,j in enumerate(range(0,width,dimention)):
				# on each single line width of whole image come with different jumps provide index for git_img
				for y in range(j,j+ dimention):
					# so y is each element
					# adding color code to the elements 
					git_image[git_h][git_w] += image[x][y] 


	# so there for each element it is the sum of dimention**2 pixles colours 
	# to take the average of all the if =sum of all the number /numbers of numbers

	for i in range(len(git_image)):
		for j in range(len(git_image[i])) :
			git_image[i][j] = round((git_image[i][j])/(dimention**2))

	print( f'✅ image is compressed here by {dimention} times')

	return (dimention,git_image)


if __name__ == "__main__" :
	im = 'img/1.jpeg'
	a=compresser(im)
	# print(a)