import re,pyperclip
s= "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
regx = r"^[a-z]|[A-Z]$"
newStr=""
seed = 97
for i in s:
	if re.fullmatch(regx,i) :
		val = (((ord(i)+2)-97)%26) + seed
		print(chr(val), end = "")
		newStr += chr(val)
	else:
		print(i,end ="")
		newStr += i
pyperclip.copy(newStr)
print()
