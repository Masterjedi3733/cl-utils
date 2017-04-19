#! /usr/bin/python

import fileinput

lines = []

for line in fileinput.input():
	lines.append(line)

numlines = len(lines)

for i in range(numlines-10,numlines):
	print lines[i].strip()
