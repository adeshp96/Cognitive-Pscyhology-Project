from PIL import Image
import subprocess, glob, os, ntpath, cv2, sys
from time import sleep

if os.path.isdir("CPsy Project Images"):
	os.rename("CPsy Project Images", "Images")

output_dir = "Images_Final/"

if os.path.isdir(output_dir) is False:
	os.mkdir(output_dir)

for filepath in glob.glob('Images/*/*.png'):
	img = cv2.imread(filepath)
	print ("Converting PNG to JPG" + filepath)
	cv2.imwrite(filepath[:-3] + 'jpg', img)

for filepath in glob.glob('Images/*/*.gif'):
	print (filepath)
	print ("GIF found! Cannot process it. Please convert it to JPG/PNG manually.")
	sys.exit(1)

def getFileNameFromPath(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

for filepath in glob.glob('Images/*/*.jpg') + glob.glob('Images/*/*.jpeg'):
	if os.path.isfile(filepath):
		print ("Resizing " + filepath)
		im = Image.open(filepath)
		imResize = im.resize((640,480), Image.ANTIALIAS)
		imResize.save(os.path.abspath(output_dir + getFileNameFromPath(filepath)), 'JPEG', quality=100)

