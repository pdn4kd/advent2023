import numpy as np

#find the 'power' of each game (required number of cubes), then multiply them together
#and sum over all games

#the real input is input02.
#There's also a test02-1.txt, which has powers of 48, 12, 1560, 630, and 36 for a sum of 2286
sum = 0

f = open("input02", "r", encoding="utf-8")
inputline = f.readline()
# need a parser to:
# * get game number, which also gives a star position in the line
# * get red/green/blue counts in each round (keeping in mind that these are variable length)
# * end up getting power

while inputline != "":
	red = 0
	green = 0
	blue = 0
	#check on location of ":" to get game number and start location. This only is implemented for up to 3 digits.
	if inputline[6] == ':':
		game = int(inputline[5])
		location = 8
	elif inputline[7] == ':':
		game = int(inputline[5:7])
		location = 9
	elif inputline[8] == ':':
		game = int(inputline[5:8])
		location = 10
	# dumb parser: just try to get number/color and go to next point
	# smart parser: break out subgames
	
	while inputline[location-2] != '\n':
		# number of cubes, up to 3 digits accepted
		if inputline[location+1] == ' ':
			n = int(inputline[location])
			location += 2
		elif inputline[location+2] == ' ':
			n = int(inputline[location:location+2])
			location += 3
		elif inputline[location+3] == ' ':
			n = int(inputline[location:location+3])
			location += 4
		# color, keep in mind that a ; or comma means , but a \n means new game
		if inputline[location] == 'r': #red
			location += 5
			if red < n:
				red = n
		elif inputline[location] == 'g': #green
			location += 7
			if green < n:
				green = n
		elif inputline[location] == 'b': #blue
			location += 6
			if blue < n:
				blue = n
	power = red * green * blue
	print(power)
	sum += power
	inputline = f.readline()

f.close()
print(sum)
