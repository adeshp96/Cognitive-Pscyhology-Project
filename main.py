import subprocess, glob, os, sys, ntpath
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from time import sleep
from random import shuffle

#Target, Scene
appropriate = [('octopus', 'sea2'), ('safetyringX', 'swimmingpool4'), ('hat2', 'dining1'), ('dice2', 'ludoscene1')]
inappropriate_context_similar = [('maiilbox1', 'kitchen1'), ('starfish1', 'christmas4'), ('frenchfries', 'studytable'), ('orange1', 'ballscene2')]
inappropriate_context_different = [('hair1', 'diningtable1'), ('donut1', 'road6'), ('penstand1', 'sky'), ('present3', 'eating2')]
no_context = [('bread4', 'blank'), ('star1', 'blank'),('vlc2', 'blank'), ('tennisball1', 'blank')]

pairings = appropriate + inappropriate_context_different + inappropriate_context_similar + no_context

input_dir = "Images_Final"

blankfilepath = os.path.join(input_dir,  'blank.jpg')

if sys.version_info < (3, 0):
	input = raw_input

def getFileNameFromPath(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def show(filepath, time):
	global plt
	image = mpimg.imread(filepath)
	plt.imshow(image, cmap = "gray")
	plt.axis("off")
	plt.show(block = False)
	plt.pause(time)


def process(targetfile, scenefile):
	# print (targetfile, scenefile)
	scenefilepath = os.path.join(input_dir, scenefile + '.jpg')
	targetfilepath = os.path.join(input_dir, targetfile + '.jpg')
	if os.path.exists(scenefilepath) is False:
		scenefilepath = scenefilepath.replace("jpg", "jpeg")
	if os.path.exists(targetfilepath) is False:
		targetfilepath = targetfilepath.replace("jpg", "jpeg")
	if os.path.exists(scenefilepath) is False or os.path.exists(targetfilepath) is False:
		print (scenefilepath)
		print (targetfilepath)
		print ("File doesn't exist. Aborting!")
		sleep(2)
		sys.exit(1)
	show(scenefilepath, 2)
	show(blankfilepath, 1.3)
	show(targetfilepath, 0.02) #Choose from 0.02, 0.04, 0.06 or 0.12
	plt.close()
	a = input ("Enter name of object you saw:\n")
	a = input("Give confidence rating out of 5:\n")

shuffle(pairings)

# for filepath in glob.glob(os.path.join('Images_Final', '*.jpg'))  + glob.glob(os.path.join('Images_Final', '*.jpeg')):
	# if os.path.isfile(filepath):
		# print (filepath)
		# show(filepath, 0.1)

for i in range(len(pairings)):
	p = pairings[i]
	print ("Trial #"+str(i + 1))
	process(p[0], p[1])
