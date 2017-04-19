#! /usr/bin/python

import fileinput
max = None 
for line in fileinput.input():
	line = line.strip()
	num = float(line)
	
	if max == None:
		max = num
	if num > max :
		max = num
		
print max
