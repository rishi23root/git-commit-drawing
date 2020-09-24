from tkinter import *
from tkinter import messagebox
import time
from basic import *
import numpy as np
from git_image_preview import git_image_preview


# color codes 
color_value0 = '#ffffff'	# [255.255.255]
color_value1 = '#9be9a8'	# [155,233,168]
color_value2 = '#40c463'	# [64,196,99]
color_value3 = '#30a14e'	# [48,161,78]
color_value4 = '#216e39'	# [33,110,57]

height = 1000
width = 500   			# idk but here heigth and width is interchanged

# create window
root = Tk()
# set tittle and geometry or size
root.title('Drawing palette')
root.geometry(f"{height}x{width}")

# this is cointain of two parts 
	# 1 pixle boxes - pixle rows and del button in end  
pixle_cointainer = Label(root,bg= '#ffffff')
pixle_cointainer.place(height = 390,width = height)


def pixles_list(master):
	# empty list

	possi = 0
	for _ in range(18):
		pixle_list = Label(master)
		pixle_list.place(x = possi,rely=0.0,relheight=1,width = 55)
		possi += 55
		space_btw=5
		height=50
		width=50
		current = 0
		for i in range(7):
			current += space_btw
			e=Button(pixle_list,borderwidth=2,relief= 'groove',bg=color_value0  )
			e.place(width=width,height=height,y=current)
			e.bind("<Button-1>", mouse_click)
			current += height

def mouse_click(event):
	event.widget.configure(bg = brush_color['bg'])


pixles_list(pixle_cointainer)



def clear_screen():
	# pixle_cointainer cointain all the list of pixle 
	for i in pixle_cointainer.winfo_children():
		for j in i.winfo_children() :
			j.configure(bg = color_value0)
	print('canvas cleared')

def save_image():
	# check is canval is empty
	count = 0
	for i in pixle_cointainer.winfo_children():
		for j in i.winfo_children() :
			if j['bg'] == color_value0 :
				count+=1
	if count == 18*7 :  #total elements
		messagebox.showinfo("Alert","There is no Data to save here ")
		print('saving fail')
		return

	
	# create nested loop now of list
	result = []
	for i in pixle_cointainer.winfo_children():
		result.append([j['bg'] for j in i.winfo_children()])
	

	# ok now check if there is any empty row in series if then remove it out
	for i in range(len(result)):
		# print(consecutive_list(result[0]))
		if consecutive_list(result[0]) == 100:
			result.pop(0)
		if consecutive_list(result[-1]) == 100:
			result.pop(-1)


	result = np.transpose(result).tolist()


	# convert into the readable format
	# [255,255,255], # #ffffff
	# [155,233,168], # #9be9a8
	# [64,196,99],   # #40c463
	# [48,161,78],   # #30a14e
	# [33,110,57]    # #216e39

	for i in range(len(result)) :
		for j in range(len(result[i])) :
			if result[i][j] == '#ffffff' :
				result[i][j] = [255,255,255]
			
			elif result[i][j] == '#9be9a8' :
				result[i][j] = [155,233,168]
			
			elif result[i][j] == '#40c463' :
				result[i][j] = [64,196,99]
			
			elif result[i][j] == '#30a14e' :
				result[i][j] = [48,161,78]
			
			elif result[i][j] == '#216e39' :
				result[i][j] = [33,110,57] 
			


	commit_colours = [
	[255,255,255], # 0
	[155,233,168], # 1
	[64,196,99],   # 2
	[48,161,78],   # 3
	[33,110,57]    # 4
	]

	git_im = create_empty_array(len(result),len(result[0]))


	# for each element in img compare it from the sorted list if true then give it the key value of the list and from the key value it can be updated
	# [print(i,j) for i,j in enumerate(sorted_list) ]

	# for each element in im 
	for lis in range(len(result)) :
		for i in range(len(result[lis])) :
			# giving each element one by one
			git_im[lis][i] = commit_colours.index(result[lis][i])


	print(f'✅ image is provided git colors and created 2 seperated images for server and respresentation')
	
	result = cv2.cvtColor(create_readable_image(result), cv2.COLOR_RGB2BGR)
	# git_im,result file 
	
	result = git_image_preview(result,57)

	# save image of Results of future commits on git
	write_image(result)
	# save git file for reading later
	git_commit_file_for_server(git_im)

	messagebox.showinfo("success","file is save in server files folder ")


	print('file saved')











	# 2 botton box
button_cointainer = Label(root ,borderwidth=2, relief="groove")
button_cointainer.place(height = 110,width = height,y = 390)

clear = Button(button_cointainer, text = 'Clear All',bg='#d9d9d9',font= ('arial',20, 'bold') ,justify= 'center',command= lambda : clear_screen())
clear.place(relx =0.01,rely=0.2,relheight=0.5,relwidth=0.15)

save = Button(button_cointainer, text = 'Save Image',bg='#d9d9d9',font= ('arial',15, 'bold') ,justify= 'center',command= lambda : save_image())
save.place(relx =0.2,rely=0.2,relheight=0.5,relwidth=0.15)


#########################################################################################
# cointain all color related stuff brush color ,select color current color can be get by brush_color['bg']

all_color_related = Label(button_cointainer)
all_color_related.place(relx =0.594,rely=0.003,relheight=1,relwidth=0.5)

current_color = Label(all_color_related ,text = 'test', borderwidth=2,relief="groove")
current_color.place(height=100,width= 100)

color_picker = Label(all_color_related , borderwidth=2,relief="groove")
color_picker.place(height = 100 ,width = 300,x=100)

# brush color
brush_color = Label(current_color,borderwidth=2,relief = 'groove',bg = color_value4)
brush_color.place(relx =0.15,rely=0.15,relheight=0.70,relwidth=0.7)

# label for color button
color_label = Label(color_picker,text= 'Select color ',justify='center', bd=3 ,font=('Arial',20,'bold'))
color_label.place(relx =0.0,rely=0.0,relheight=0.5,relwidth=1)

# label to cointain all the color button
color_box = Frame(color_picker)
color_box.place(relx =0.0,rely=0.5,relheight=0.5,relwidth=1)

# color buttons with unique colors
color0 = Button(color_box,bg=color_value0 ,bd=2 , command = lambda : update_brush(color_value0) )
color0.place(relx =0.03,rely=0.1,relheight=0.8,relwidth=0.15)	

color1 = Button(color_box,bg=color_value1 ,bd=2 , command = lambda : update_brush(color_value1) )
color1.place(relx =0.23,rely=0.1,relheight=0.8,relwidth=0.15)	

color2 = Button(color_box,bg=color_value2 ,bd=2 , command = lambda : update_brush(color_value2) )
color2.place(relx =0.43,rely=0.1,relheight=0.8,relwidth=0.15)	

color3 = Button(color_box,bg=color_value3 ,bd=2 , command = lambda : update_brush(color_value3) )
color3.place(relx =0.63,rely=0.1,relheight=0.8,relwidth=0.15)	

color4 = Button(color_box,bg=color_value4,bd=2 , command = lambda : update_brush(color_value4) )
color4.place(relx =0.83,rely=0.1,relheight=0.8,relwidth=0.15)	

def update_brush(val):
	# update the brush color when called
	brush_color.configure(bg = val)
	# print(brush_color['bg'])
 
####################################################################################



root.mainloop()
