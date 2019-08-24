#This program checks who you are!
name = ""
while True:
	print("Who are you?")
	name = input()
	if name != "Joe":
		continue
	print("Hello,Joe! What is the password?")
	password = input()
	if password == "sword":
		break
print("access granted")
		
	
