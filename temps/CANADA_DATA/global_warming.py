from sys import argv
import sys
from itertools import dropwhile
from numpy import average
from time import strptime,strftime

# Can we observe global warming in the CWEEDS data?
# Here's a little script which combs through all of
# the data to investigate this question

# Add a data entry value
def add_data(ln, data):
	# Canadians meteorologists believe "24:00" is a time
	# while python people do not, so here's a fix
        tm = strptime(ln[6:14] + "%02i" % (int(ln[14:16]) % 24), "%Y%m%d%H")
        doy = int(strftime("%j", tm))-1
        # this is the year in "decimal" form
        date = tm.tm_year + (doy*24+(tm.tm_hour-1))/(365.*24)
        data.append([date, int(ln[91:95])])

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

# moving average calculation for data 
# with wsize window size and wstep window step
def moving_average(data,wsize,wstep):
	n = 0
	while n+wsize < len(data):
		avg_time = average(map(lambda x: x[0],data[n:n+wsize]))
		avg_temp = average(map(lambda x: x[1],data[n:n+wsize]))
		yield((avg_time, avg_temp))
		n += wstep

def get_moving_average(fname):
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
	mavg_fp = open("./global_warming/"+fst_ln[:16]+".tsv",'w')
	for avg in moving_average(fdata,364*24,28*24):
		print >>mavg_fp, avg[0],"\t",avg[1]
		mavg_fp.flush()
	mavg_fp.close()

if __name__ == "__main__":
	for fname in argv[1:]: get_moving_average(fname)
