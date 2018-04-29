import subprocess, glob, os, sys, ntpath
from time import sleep
from random import shuffle

#Target, Scene
appropriate = [('octopus', 'sea2'), ('safetyringX', 'swimmingpool4'), ('hat2', 'dining1'), ('dice2', 'ludoscene1')]
inappropriate_context_similar = [('maiilbox1', 'kitchen1'), ('starfish1', 'christmas4'), ('frenchfries', 'studytable'), ('orange1', 'ballscene2')]
inappropriate_context_different = [('hair1', 'diningtable1'), ('donut1', 'road6'), ('penstand1', 'sky'), ('present3', 'eating2')]
no_context = [('bread4', 'blank'), ('star1', 'blank'),('vlc2', 'blank'), ('tennisball1', 'blank')]

pairings = appropriate + inappropriate_context_different + inappropriate_context_similar + no_context

input_dir = "Images_Final"


#Holder for image process
p = None

def getFileNameFromPath(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def show(filepath):
	global p
	if 'win' in sys.platform:
		p = subprocess.Popen(["start", filepath], shell=True)
	else:
		p = subprocess.Popen(["display", filepath])

def hide(filepath):
	global p
	if 'win' in sys.platform:
		a = "INFO"
		while "SUCCESS" not in a:
			a = subprocess.check_output(['taskkill', '/F', '/FI',' WINDOWTITLE eq ' + getFileNameFromPath(filepath) + '*'])
			a = str(a, 'utf-8')
	else:
		p.kill()

def process(targetfile, scenefile):
	print (targetfile, scenefile)
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
		sys.exit(1)
	show(scenefilepath)	
	sleep(2)
	hide(scenefilepath)	
	sleep(1.3)
	show(targetfilepath)
	# sleep(0.1)
	hide(targetfilepath)
	a = input ("Enter name of object you saw:\n")
	a = input("Give confidence rating out of 5:\n")


shuffle(pairings)

for p in pairings:
	process(p[0], p[1])
