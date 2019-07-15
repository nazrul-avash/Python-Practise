import os
def writeFiles(track):
	fileOb = open(track,"a")
	text = "assholes are closer than they appear"
	fileOb.write(text)
	fileOb.close()
def readFiles(track):
	if os.path.exists(track):
		fileOb = open(track)
		content = fileOb.readlines()
		for p in content:
			print(p)
		print(type(content))
		fileOb.close()
def renameAllFiles(presentPath):
	if os.path.exists(presentPath):
		print("Correct directoryName, renaming files.....")
		names = os.listdir(presentPath)
		os.chdir(presentPath)
		for g in names:
			if os.path.isfile(g):
				temp = g + "2019"
				os.rename(g, temp)
				print(g)
	else:
		print("Incorrect directoryName")	
def renameFiles(presentName, wouldBeName):
	if os.path.exists(presentName):
		os.rename(presentName, wouldBeName)
	else:
		print("file not fouond")	
def countAllFiles(names,count,line):
	print(count)	
	if len(names) == 0:
		return count 
	for i in names:
		if os.path.isfile(line+i):
			
			count +=1
		elif os.path.isdir(line+i):
			count = countAllFiles(os.listdir(line+i+"/"),count,line+i+"/")	
			print(count)
	return count 		
def countFile(directoryName):
	genList = []
	count = 0
	if os.path.exists(directoryName) and os.path.isdir(directoryName):
		genList = os.listdir(directoryName)
		count = len(genList)
	elif os.path.isfile(directoryName):
		 count =1
	return count	 	

line = "/home/nazrul/experimentals/iso.txt"
writeFiles(line)
readFiles(line)