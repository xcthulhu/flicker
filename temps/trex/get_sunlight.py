#!/usr/bin/env python

# This script grabs *sunlight data* from the 
# "TRibal Environmental eXchange network":
# http://trexwww.ucc.nau.edu/cgi-bin/daily_average.pl

# We have reverse engineered how this particular perl CGI 
# script functions, which only prints environmental conditions
# for one day at a time to a web interface

# This python script is programmed to acquire all data
# starting from January 1, 2005 to present for stations in southern California

import httplib, urllib, re, os
from time import strptime, gmtime
from calendar import timegm

# We shall be interested in taking data from the following southern California stations:
# # 32: Passamaquoddy Tribe at Pleasant Point
# # 1017: Walker River Paiute Tribe
# # 1018: Lone Pine Paiute-Shoshone Tribe station
# # 1023: Bishop Paiute Tribe EMO
# # 1026: Pyramid Lake Paiute Tribe
# # 1028: Fort Independence Paiute Tribe
# # 1033: Big Pine Band of Owens Valley Paiute Shoshone Indians of the Big Pine Reservation
# # 1036: Tribal Exchange Network
stations = [32, 1017, 1018, 1023, 1026, 1028, 1030, 1033, 1036]

# This dictionary of REs find the various HTML tables in the of internet data 
# corresponding to different stations
table = {}
for s in stations:
    table[s] = re.compile("%i[^^]*%i" % (s,s))

# This RE finds numbers or error codes
# See http://trexwww.ucc.nau.edu/cgi-bin/daily_info.pl?nodata for details
vals = re.compile("-?\d+\.\d+|NA|LST|LIM|PMA|CAL|SPN|SPZ|QAS|QRE|AQI|MAL|NOL|FEW|NEG|MUL|NOD")

# Dictionary of files for all of the stations
fp = {}
for s in stations:
    fp[s] = open("%i_sunlight.tsv" % s, "w")

# Biolerplate for POST calls to the foreign CGI script
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html"}

# Dictionaries we want for our data processing loop
datah = {}
datap = {}

time = timegm(strptime("01 01 2003", "%d %m %Y"))
now = timegm(gmtime())

while (time <= now):
    tm = gmtime(time)
    day, month, year = tm.tm_mday, tm.tm_mon, tm.tm_year

    # These parameters acquire sunlight data for all available stations
    params = urllib.urlencode({'first_look': 'no', 'select_date': 'user', 'user_day': day, 'user_month': month-1, 
                               'user_year': year, 'user_param': 63301, 'time_format': '24hr', 'region_crit': all})

    # Acquire Data
    conn = httplib.HTTPConnection("trexwww.ucc.nau.edu")
    conn.request("POST", "/cgi-bin/daily_average.pl", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    
    # Process Each Station
    for s in stations:
        datah[s] =  table[s].search(data)
        if datah[s] == None: 
            print "%i: %02i/%02i/%02i\tNO DATA" % (s, day,month,year)
            print >>fp[s], "%02i/%02i/%02i\tNO DATA" % (day,month,year)
            fp[s].flush()
        else:
            datap[s] = vals.findall(datah[s].group())[0:24]
            print "%i: %02i/%02i/%02i\t" % (s,day,month,year), "\t".join(datap[s])
            print >>fp[s], "%02i/%02i/%02i\t" % (day,month,year), "\t".join(datap[s])
            fp[s].flush()

    time += 24*60*60

for f in fp:
    f.close()
