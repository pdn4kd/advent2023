import numpy as np
import string
import io

#day 6 challenge 2

#the real input is input06. (or modified as input06b)
#There's also a test06-1 which is used to make sure that the code runs correctly.

#test06-1:
#Time:      7  15   30
#Distance:  9  40  200


mult = 1

races = np.genfromtxt("test06-2b", delimiter=":")
races = np.genfromtxt("input06b-2", delimiter=":")

#just iterate over every possible time
#will give the wrong answer if there are 0 ways to win. Though since there's only 1 race, that is trivially sovleable.
#Also sort of slow, but one race so doing almost a million iterations doesn't matter
mult = 1
time = races[0][1]
distance = races[1][1]
ways = 0
for t in np.arange(time+1):
	x = t*(time-t)
	if x > distance:
		ways += 1
mult *= ways
print(time,distance,ways)
print(mult)
