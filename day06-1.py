import numpy as np
import string
import io

#day 6 challenge 1

#the real input is input06. (or modified as input06b)
#There's also a test06-1 which is used to make sure that the code runs correctly.

#test06-1:
#Time:      7  15   30
#Distance:  9  40  200


mult = 1

races = np.genfromtxt("test06-1b", delimiter=" ")
races = np.genfromtxt("input06b", delimiter=" ")

#trying to be clever with physics knowledge, but it doesn't work
for n in np.arange(1,len(races[0])):
	time = races[0][n]
	distance = races[1][n]
	# min/max time found via quadratic formula
	# then rounded to nearest (milli)second
	mintime = (time/2 - np.sqrt(0.25*time**2 + distance))
	maxtime = (time/2 + np.sqrt(0.25*time**2 + distance))
	ways = maxtime - mintime
	print(time,distance,mintime,maxtime,ways)
	mult *= ways

print(mult)

#alternate, just iterate over every possible time
mult = 1
for n in np.arange(1,len(races[0])):
	time = races[0][n]
	distance = races[1][n]
	ways = 0
	for t in np.arange(time+1):
		x = t*(time-t)
		if x > distance:
			ways += 1
	mult *= ways
	print(time,distance,mintime,maxtime,ways)
print(mult)
