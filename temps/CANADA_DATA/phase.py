from sys import argv
from itertools import dropwhile
from numpy import average,max,sin,e,pi
from cmath import phase
import ephem

# Load the station-name to coordinates map
coords = {}
coords_fp = open("COORDS.txt","r")
for s in coords_fp.readlines():
	s_ = s.split()
	coords[" ".join(s_[:-2])] = (s_[-2],"-"+s_[-1])
coords_fp.close()

# Load the station-code to station-name map
stat_names = {}
stat_names_fp = open("STAT_NAMES.txt","r")
for s in stat_names_fp.readlines():
	s_ = s.split()
	stat_names[s_[0]] = " ".join(s_[1:])
stat_names_fp.close()

# Add a data entry value
def add_data(ln, data):
	data.append([
		"%s/%s/%s %s:00" % (ln[6:10],ln[10:12],ln[12:14],ln[14:16]),
		int(ln[91:95])])

# Get sine of sun elevation for an observer
sun = ephem.Sun()
def sun_sin(date, obs):
	obs.date = date
	sun.compute(obs)
	return sin(max([sun.alt,0]))

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
	return phase(temp_dft_comp) - phase(sun_dft_comp)

# A fix for corrupted data entries, which also computes sun altitude
def fix_data(data, obs):
	# drop the first few corrupted entries
	data_ = list(dropwhile(lambda x: x[1] == 9999, data))
	# Find the average of not-corrupted data
	avg = average(filter(lambda x: x != 9999,map(lambda x: x[1],data_)))
	return [[sun_sin(x[0],obs),x[1]] if x[1] != 9999 else
		[sun_sin(x[0],obs),avg] for x in data_]

# calculate and print phase differences for WY2 file
def print_phases(filename):
	# Open the WY2 file for processing
	WY2_fp = open(argv[1],"r")
	# Read the station code from the first line of the file
	fst_ln = WY2_fp.readline()
	obs = ephem.Observer()
	# Obtain the station longitude and lattitude
	obs.lat,obs.long=coords[stat_names[fst_ln[0:5]]]
	data = []
	add_data(fst_ln, data)
	for ln in WY2_fp.readlines():
		add_data(ln, data)
	WY2_fp.close()
	fdata = fix_data(data,obs)
	print fst_ln[0:5],phase_delay(fdata,1/24.)	

if __name__ == "__main__":
	for filename in argv:
		print_phases(filename)
