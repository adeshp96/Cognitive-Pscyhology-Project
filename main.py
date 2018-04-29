import subprocess, glob, os, sys, ntpath
from time import sleep
# import resize

def getFileNameFromPath(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

for filepath in glob.glob(os.path.join('Images_Final', '*.jpg'))  + glob.glob(os.path.join('Images_Final', '*.jpeg')):
	if os.path.isfile(filepath):
		print (filepath)
		if 'win' in sys.platform:
			p = subprocess.Popen(["start", filepath], shell=True)
		else:
			p = subprocess.Popen(["display", filepath])
		sleep(1)
		if 'win' in sys.platform:
			subprocess.call(['taskkill', '/F', '/FI',' WINDOWTITLE eq ' + getFileNameFromPath(filepath) + '*'])
		else:
			p.kill()