import re
numberlist = []
file = open('mbox-short.txt')
for line in file:
	line = line.rstrip()
	curlist = re.findall('^From.*', line)
	if len(curlist) != 1 : continue
	numberlist.append(curlist)
	print(curlist)
	curlist2 = re.findall('[0-9]+', line)
	print(curlist2)
	curlist3 = re.findall('From: (.*)@', line)
	print(curlist3)