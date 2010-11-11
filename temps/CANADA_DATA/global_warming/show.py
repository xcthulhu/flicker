#!/usr/bin/env python
import pylab
import csv
from sys import argv
from matplotlib.colors import rgb2hex

def hue(x):
	x = x % 1
	if 0 <= x and x <= 1/3. :
		return rgb2hex((1-(x*3), x*3, 0))
	if 1/3. < x and x <= 2/3. :
		return rgb2hex((0, 2-(x*3), (x*3)-1))
	if 2/3. < x and x < 1:
		return rgb2hex(((x*3)-2, 0, 3-(x*3)))

data = csv.reader(open(argv[1], 'rb'), delimiter="\t") 

t,s = [],[]
for x in data:
	t.append(x[0])
	s.append(x[1])

pylab.plot(t,s,hue(0))
pylab.show()
