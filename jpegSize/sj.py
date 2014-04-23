import os, imghdr, Image, shutil

#change according to needs
target_directory = "portable"

#assumes that the images are in the form factor 4:3
width, height = 800, 600


def is_jpeg(file):
	head, tail = os.path.split(os.path.abspath(file))
	if len(tail) < 4:
		return False
	if tail[-4] == 'j' or tail[-4] == 'J' or tail[-3] == 'j' or tail[-3] == 'J':
		if (imghdr.what(file) == 'jpeg'):
			return True
	return False
	
def save_smaller(file):
	try:
		head, tail = os.path.split(os.path.abspath(file))
		dir_name = os.path.join(head, target_directory)
		if not os.path.exists(dir_name):
			print "Creating directory " + target_directory
			os.makedirs(dir_name)
		file_name = os.path.join(dir_name, tail)
		print file_name
		if not os.path.exists(file_name):
			im = Image.open(file)
			#if the picture type is portatrait
			iw, ih = im.size
			if iw < ih:
				im = im.resize((height, width))
			else:
				im = im.resize((width, height))
			im.save(file_name, "jpeg")
	except:
		print "Could not open " + file

files = os.listdir(os.getcwd())
for file in files:
	if(is_jpeg(file)):
		save_smaller(file)
print "Operations completed."
