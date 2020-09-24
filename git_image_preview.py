# decompresser for representaion
from basic import * 
import numpy as np

def git_image_preview(a,dimention):
	# take compressed raw image and its compressed dimentions 
	# a = read_image(a,1)
	if type(a) == np.ndarray:
		a = a.tolist()

	# first we create an empty list of height*dimention and width*dimention amd
	resul = create_empty_array(len(a)*dimention,len(a[0])*dimention)

	# then fill with values accourding to list and gap of dimention 

	for a_h,i in enumerate(range(0,len(resul),dimention)):
		# give index and value of jump (0,0)
		for x in range(i,i+dimention):
			# go in each line one by one of each jump [profit]!! jump provide index for git_img 
			# so x is each line
			for a_w,j in enumerate(range(0,len(resul[0]),dimention)):
				# on each single line width of whole image come with different jumps provide index for git_img
				for y in range(j,j+ dimention):
					# so y is each element
					resul[x][y] = a[a_h][a_w]
					# trying to make white grid for better example

					# if (x in [i+1,j+2,j+3,j+dimention-1,j+dimention-2,j+dimention-3]) and (y in [j+1,j+2,j+3,j+dimention-1,j+dimention-2,j+dimention-3]) :
					# 	resul[x][y] = [255,255,255]
					# else :
					#	 resul[x][y] = a[a_h][a_w]


	print(f'✅ image is Decompressed here by {dimention} times for representaion of future git_img')
	return resul
					
if __name__ == '__main__':
	dimention=57
	a= [
		[[48, 161, 78], [64, 196, 99], [64, 196, 99], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [155, 233, 168], [64, 196, 99], [48, 161, 78]],
		[[33, 110, 57], [48, 161, 78], [64, 196, 99], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [155, 233, 168]], 
		[[48, 161, 78], [64, 196, 99], [255, 255, 255], [255, 255, 255], [64, 196, 99], [255, 255, 255], [255, 255, 255], [155, 233, 168], [64, 196, 99], [48, 161, 78]],
		[[155, 233, 168], [155, 233, 168], [255, 255, 255], [255, 255, 255], [64, 196, 99], [64, 196, 99], [155, 233, 168], [155, 233, 168], [155, 233, 168], [155, 233, 168]], 
		[[64, 196, 99], [64, 196, 99], [155, 233, 168], [155, 233, 168], [64, 196, 99], [48, 161, 78], [48, 161, 78], [64, 196, 99], [64, 196, 99], [155, 233, 168]], 
		[[33, 110, 57], [48, 161, 78], [48, 161, 78], [48, 161, 78], [64, 196, 99], [48, 161, 78], [33, 110, 57], [48, 161, 78], [48, 161, 78], [48, 161, 78]], 
		[[33, 110, 57], [33, 110, 57], [33, 110, 57], [33, 110, 57], [48, 161, 78], [48, 161, 78], [33, 110, 57], [33, 110, 57], [33, 110, 57], [48, 161, 78]]
		]

	show_image(create_readable_image(git_image_preview(a,dimention)))

