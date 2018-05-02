import os, sys, ntpath
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from time import sleep
from random import shuffle

#Target, Scene
present_pairings = [('tv', 'present', 'aroundtv'), ('blender', 'present', 'kitchen'), ('plant', 'present', 'bookshelf')]
absent_pairings = [('table', 'absent', 'sofa'), ('painting', 'absent', 'bedroomhigh'), ('heater', 'absent', 'bedroomlow')]
blank_pairings = [('rug', 'nopreview', None), ('sideboard', 'nopreview', None), ('stove', 'nopreview', None)]

pairings = present_pairings + absent_pairings + blank_pairings

input_dir = "Images_Final"

plt.switch_backend('TkAgg')

blankfilepath = os.path.join(input_dir,  'blank.jpg')
answerfilepath = os.path.join(input_dir,  'answer.jpg')


def getFileNameFromPath(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def show(filepath, time, close_on_click = False):
	global plt
	if filepath is None:
		return
	image = mpimg.imread(filepath)
	plt.imshow(image, cmap = "gray")
	plt.axis("off")
	mng = plt.get_current_fig_manager()
	if 'win' in sys.platform:
		mng.window.state('zoomed')
	else:
		mng.resize(*mng.window.maxsize())
	if close_on_click:
		cid = None
		def onclick(event):
			plt.gcf().canvas.mpl_disconnect(cid)
			plt.close()
			return
		cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)
		plt.show()
	else:
		plt.show(block = False)
		plt.gcf().canvas.set_window_title("Experiment Window")
		plt.pause(time)


def process(targetfile, previewfile, scenefile):
	targetfilepath = scenefilepath = previewfilepath = None
	if scenefile is not None:
		scenefilepath = os.path.join(input_dir, scenefile + '.jpg')
	previewfilepath = os.path.join(input_dir, previewfile + '.jpg')
	targetfilepath = os.path.join(input_dir, targetfile + '.jpg')
	if scenefilepath is not None and os.path.exists(scenefilepath) is False:
		scenefilepath = scenefilepath.replace("jpg", "jpeg")
	if os.path.exists(previewfilepath) is False:
		previewfilepath = previewfilepath.replace("jpg", "jpeg")
	if os.path.exists(targetfilepath) is False:
		targetfilepath = targetfilepath.replace("jpg", "jpeg")
	if (scenefilepath is not None and os.path.exists(scenefilepath) is False) or os.path.exists(previewfilepath) is False or os.path.exists(targetfilepath) is False:
		print (scenefilepath)
		print (targetfilepath)
		print ("File doesn't exist. Aborting!")
		sleep(2)
		sys.exit(1)
	show(blankfilepath, 1)
	show(scenefilepath, 5) #Original was 20
	show(previewfilepath, 1.2)
	show(targetfilepath, 2.2)
	show(answerfilepath, time = None, close_on_click = True)

shuffle(pairings)

for i in range(len(pairings)):
	p = pairings[i]
	print ("Trial #" + str(i + 1))
	process(p[0], p[1], p[2])
