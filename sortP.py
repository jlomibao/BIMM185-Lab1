#File Name : sortP.py
#Author    : John Francis Lomibao
#PID       : A11591509

import sys
import csv
import re

#Variables
N = 2000
p_list = []
c_list = []
c2_list = []
count = 0
uniq = None

#functions

def sort_alphanum( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

#main

with open(sys.argv[1], 'r') as f:
	#get first 2000 lines
	for i in range(0,N):
		#get 1st column only
		line = f.readline().strip('\n').split()[0]
		p_list.append(line)
	#sort by name
	p_list.sort()

#count repeats and put into new list
for i in p_list:
	if i not in c_list:
		if uniq != None:
			c2_list.append(str(count)+" "+uniq)
		c_list.append(i)
		count = 1
		uniq = i
	else:
		count = count + 1
c2_list.append(str(count)+" "+uniq)

#sort alphanumerically in descending order and print
for i in reversed(sort_alphanum(c2_list)):
	print i
