from basic import *
from chiseler import chiseler
from compresser import compresser
from color_provider import color_provider
from git_image_preview import git_image_preview
import sys



def test(img):
	check_image_size_ratio(img)
	dimention,image =compresser(img)
	print(image)
	git_im,image = color_provider(image)

	# make image of a size
	image = git_image_preview(image,dimention)
	# save image of Results of future commits on git
	write_image(image)
	# save git file for reading later
	git_commit_file_for_server(git_im)

	# show image
	show_image(read_image(img),'real_image press ESC ')
	show_image(create_readable_image(image),'Results press ESC ')

	print()
	print('your files are saved in folder name server-files upload them to your server and run it in background ')
	print()

if __name__ == '__main__':
	test(sys.argv[1])
	# test(im6)
