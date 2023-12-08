import numpy as np
import string
import io
import re

#day 8 challenge 1
#the real input is input08.
#There's also a test08-1, which is used to make sure that the code runs correctly.

# need a parser to:
# * load up directions
# * load up map (should these by seperate files?)
# * cycle through directions, while counting steps
# * move through map, following directions

f = open("input08-rl", "r", encoding="utf-8")
#f = open("test08-rl", "r", encoding="utf-8")
directions = f.readline()
f.close()

n = -1 # pointer to where we are in the directions
step = 0 # step counter
# making the R/L thing positions in the desertmap array
directions = re.sub("R", "2", directions)
directions = re.sub("L", "1", directions)

#load map as a 3 column array or something
desertmap = np.genfromtxt("input08-map", delimiter=',', dtype=None, encoding=None)
#desertmap = np.genfromtxt("test08-map", delimiter=',', dtype=None, encoding=None)
position = desertmap[0]
while(position[0] != 'ZZZ' and step < 1000000000):
	#print(position)
	step += 1
	n = (n+1) % (len(directions)-1)
	target = position[int(directions[n])]
	for line in desertmap:
		if line[0] == target:
			position = line

print(step)
	

'''
sum = 0
f = open("input08", "r", encoding="utf-8")
inputline = f.readline()

while inputline != "":
	# ...
	inputline = f.readline()

f.close()
print(sum)
'''
