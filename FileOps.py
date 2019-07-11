import os
line = "/home/nazrul/"
genList =[]
genList = os.listdir("/home/nazrul")
for i in genList:
	if os.path.isdir(line+i):
		print("**** "+i+"  "+ str(int(os.path.getsize(line+i))//8) )
	else:
		print(".... "+i+"  "+ str(int(os.path.getsize(line+i))//8))	
