from sys import argv
import sys
from itertools import dropwhile
from numpy import average,max,sin,e,pi
from cmath import phase

# Add a data entry value
def add_data(ln, data):
	data.append([int(ln[16:20]), int(ln[91:95])])

### NOTE ###
# The following two lines loop through rather-large arrays several times
# It's all O(n) operations, but even linear stuff adds up and is kind of slow

# A fix for corrupted data entries, which also computes sun altitude
def fix_data(data):
	# drop the first few corrupted entries
	data_ = list(dropwhile(lambda x: x[1] == 9999, data))
	# Find the average of not-corrupted data
	avg = average(filter(lambda x: x != 9999,map(lambda x: x[1],data_)))
	return [[x[0],x[1]] if x[1] != 9999 else
		[x[0],avg] for x in data_]

# Obtain phase delays
def phase_delay(data,freq):
	n = 0
	sun_dft_comp = 0
	temp_dft_comp = 0
	# Obtain the Discrete Fourier Transform components for frequency freq
	for x in data:
		sun_dft_comp += x[0]*e**(-1j*(2*pi*freq*n))
		temp_dft_comp += x[1]*e**(-1j*(2*pi*freq*n))
		n+=1
	# Return the difference in phases
	return (phase(sun_dft_comp/temp_dft_comp)+2*pi) % (2*pi)

# calculate and print phase differences for WY2 file
def print_phases(fname,freq):
	# Open the WY2 file for processing
	WY2_fp = open(fname,"r")
	# Read the station code from the first line of the file
	fst_ln = WY2_fp.readline()
	data = []
	add_data(fst_ln, data)
	for ln in WY2_fp.readlines():
		add_data(ln, data)
	WY2_fp.close()
	fdata = fix_data(data)
	print fst_ln[0:5],phase_delay(fdata,freq)	
	sys.stdout.flush()

if __name__ == "__main__":
	### NOTE ###
	# Using eval here is dangerous!  I should really write a regular 
	# expression to check that argv[1] is safe
	for fname in argv[2:]: print_phases(fname,eval(argv[1]))
