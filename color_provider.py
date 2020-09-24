from basic import *
import cv2

def color_provider(im):
	# provide image array in two formats 1st git_im and second real image 
	git_im = create_empty_array(len(im),len(im[0]))
	# make list of all possible colours pixles
	al_poss = [] # saving all possible pixle colours in here 
	for i in im:
		for j in i:
			if j not in al_poss:
				al_poss.append(j)

	al_poss.sort(reverse= True) # short them according to their shade  
	# more small the pixle more darker it is and more dark mean more commits

	# divide all the sepeate list for giving same colour code to each list and return shorted_list
	if len(al_poss) == 1:
		# mean image have only one colour there fore on the bases of its pixle colour give it of green index
		sorted_list = less_len_or_single_ele_list(al_poss)

	elif 1 < len(al_poss) <= 5 :
		# len is some where between 1 and 5 them give colour code accouring to previous codes  
		sorted_list =  less_len_or_single_ele_list(al_poss)

	elif len(al_poss) > 5 :
		# check if list is consicutive if not else pass
		sorted_list = other_sorting(al_poss)


	commit_colours = [
	[255,255,255], # 0
	[155,233,168], # 1
	[64,196,99],   # 2
	[48,161,78],   # 3
	[33,110,57]    # 4
	]


	# for each element in img compare it from the sorted list if true then give it the key value of the list and from the key value it can be updated
	# [print(i,j) for i,j in enumerate(sorted_list) ]

	# for each element in im 
	for lis in range(len(im)) :
		for i in range(len(im[lis])) :
			# giving each element one by one
			for ele in range(len(sorted_list)) :
				if im[lis][i] in sorted_list[ele] :
					git_im[lis][i] = ele

					im[lis][i] = commit_colours[ele]
					
					break

	print(f'✅ image is provided git colors and created 2 seperated images for server and respresentation')

	
	# therefolour image cointains list of RBG of the pixles 
	# so on the bases of the number of the pixle it get provide it the RGB list of pixle 
	# but cv2 take format of BGR so after giving colour code we
	# have to the color code for cv2 to under stand it properly 
	# by [cv2.cvtColor(img, cv2.COLOR_RGB2BGR)] 

	return (git_im,cv2.cvtColor(create_readable_image(im), cv2.COLOR_RGB2BGR))


if __name__ == '__main__':
	im = 'img/1.jpeg'

	image = read_image(im5).tolist()
	git_im,image = color_provider(image)
	# TEST ONLY
	# show_image(cv2.cvtColor(create_readable_image(image), cv2.COLOR_RGB2BGR))

	# print(git_im)
	# print(im)