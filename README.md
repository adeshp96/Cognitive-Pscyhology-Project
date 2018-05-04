# Cognitive-Pscyhology-Project
> cd expt1 <br/>
> pyinstaller --onefile --noconsole .\main.py <br/>
> cd expt2 <br/>
> pyinstaller --onefile --noconsole .\main.py <br/>
This creates a standalone executable for whichever operating system you're currently working on. Note that loading modules takes time (especially for expt2). <br/>
The main.exe created also require the images in Images_Final directory. To package both of them together, you can use SFX to archieve them in self extracting exe, silently install in a temporary directory and run main.exe automatically. <br/>
