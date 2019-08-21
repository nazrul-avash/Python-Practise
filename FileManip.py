import os
def countCharacterFreq(fileOb):
	things = {}
	for char in fileOb.read():
		if char in things:
			things[char] +=1
		else:
			things[char] =1	 
	for i , j in sorted(things.items()):
		print(i+" "+str(j))
def countLines(fileOb):
	count = 0
	lines = fileOb.readlines()
	print(len(lines))
	return len(lines)
fileOb = open("sample.txt")
#fileOb = "Md. Nazrul Islam"
countCharacterFreq(fileOb)