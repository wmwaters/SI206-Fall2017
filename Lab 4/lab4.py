import re
numberlist = []
file = open('mbox-short.txt')
for line in file:
	line = line.rstrip()
	curlist = re.findall('^From.*', line)
	if len(curlist) != 1 : continue
	print(curlist)