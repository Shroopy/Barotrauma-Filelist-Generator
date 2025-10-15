from pathlib import Path

# targetDir = input("Target directory to scan: ")

filelist = ""

for root, dirs, files in Path(r"C:\Users\Delyth Rauenzahn\Programming\Barotrauma 40k Reworked").walk():
	dirs[:] = [d for d in dirs if not d.startswith('.')]
	for file in files:
		filelist += file + "\n"

with open("filelist.txt", "w") as f:
	f.write(filelist)
		