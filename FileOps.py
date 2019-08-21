import os
def deleteFiles(directory,ext):
	if os.path.exists(directory):
		os.chdir(directory)
		for p in os.listdir(directory):
			if not os.path.isdir(p):
				temp = os.path.splitext(p)
				if temp[1] == ext:
					os.remove(p)
	else:
		print("inval")				
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
def countAllFilesWithOS(link):
	count = 0
	for d,sd,f in os.walk(link):
		count += len(f)
	return count	
def countAllFiles(names,count,line):
		
	if len(names) == 0:
		return count 
	for i in names:
		if os.path.isfile(line+i):
			
			count +=1
		elif os.path.isdir(line+i):
			count = countAllFiles(os.listdir(line+i+"/"),count,line+i+"/")	
			
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

line = "/home/nazrul/experimentals/"
count = 0
print(countAllFiles(os.listdir(line),count,line))
print(countAllFilesWithOS(line))
