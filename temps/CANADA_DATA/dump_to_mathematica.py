#!/usr/bin/env python

import csv
from sys import argv

data = csv.reader(open(argv[1], 'rb'), delimiter="\t") 

for row in data: 
	print row[0],"\t",\
	      complex(row[1]).real,"\t",complex(row[1]).imag,"\t",\
	      complex(row[2]).real,"\t",complex(row[2]).imag,"\t",\
	      complex(row[3]).real,"\t",complex(row[3]).imag,"\t"
