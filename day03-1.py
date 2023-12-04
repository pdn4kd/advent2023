import numpy as np
import string
import io

#day 3 challenge 1

#the real input is input03.
#There's also a test03-1.txt, which is used to make sure that the code runs correctly.
#And a padded test03-1b.txt and input03b
#For that, the numbers we want are 467, 35, 633, 617, 592, 755, 664, and 598
#114 and 58 are not
#the sum is 4361
sum = 0

symbols = "!#$%&()*+,-/:;<=>?@[\]^_`{|}~" #actually includes a lot of extras

#f = open("test03-1b.txt", "r", encoding="utf-8")
f = open("input03b", "r", encoding="utf-8")
currentline = f.readline()
nextline = f.readline()
inputline = f.readline()
# need a parser to:
# * find numbers
# * find if there are any symbols between number start-1 and number end+1
# test input is 10x10 grid
# actual is 140x140
# symbols are effectively not numbers or dots

#main loop, will need to special case beginning/ending lines
#Or I could alter the input to be a 142x142 grid and just search a 140x140 interior portion
#Going with adding padding
while inputline != "": 
	# 'bookkeeping' since we need to keep inputs above/below search line
	position = 1
	prevline = currentline
	currentline = nextline
	nextline = inputline
	# ...
	# search to find numbers on the line
	while position < (len(currentline)-1):
		partnumber = False
		for digit in string.digits:
			if currentline[position] == digit:
				#we have a number! how long is it?
				numberstart = position
				numberend = position
				# run forwards until we run out of digits. numbers are up to 3 digits long
				for digit2 in string.digits:
					if currentline[position+1] == digit2:
						numberend = position+1
						for digit3 in string.digits:
							if currentline[position+2] == digit3:
								numberend = position+2
				number = int(currentline[numberstart:numberend+1])
				#print(number)
				position = numberend+1
				# look for symbols around it, if there are any add it to the sum
				# so at some point partnumber = True
				for n in np.arange(numberstart-1,numberend+2):
					# check symbols in prevline and nextline
					for symbol in symbols:
						if (prevline[n] == symbol) or (nextline[n] == symbol):
							partnumber = True
				#check symbols in currentline at numberstart-1 and numberend+1
				for symbol in symbols:
					if currentline[numberstart-1] == symbol or currentline[numberend+1] == symbol:
						partnumber = True
		#If there was a valid number, sum it up
		if partnumber == True:
			#print("part number")
			sum += number
		position += 1 # will skip the empty space if a number was found, but only advance one if nothing was.
	inputline = f.readline()

f.close()
print(sum)
