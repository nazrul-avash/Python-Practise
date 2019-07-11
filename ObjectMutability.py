import re
def isSame(text,text2):
	print(type(text))
	if text is text2:
		print("same object/box")
	else:
		print("different object/box")	
	print(id(text))
	print(id(text2))	
text = "abc"
text2 = text
text2 = text2+ "x"
things = [1,2]
things2 = things 
things2[0] = 3
isSame(text,text2)
isSame(things,things2)
st = str(type(text))
regx = r"'[a-zA-Z]+'"
st = re.search(regx,st)
print(len(st.group(0)))