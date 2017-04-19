#! /usr/bin/python

import fileinput

min = None
for line in fileinput.input():
	line = line.strip()
	num = float(line)
	
	if min == None:
		min = num
	if num < min:
		min =  num
print min

