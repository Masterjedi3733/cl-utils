#! /usr/bin/python
import fileinput

for line in fileinput.input():
        line = line.strip()
        num = float(line)

        if num < 0 :
                num = num * -1
		print num
	else:
		print num
