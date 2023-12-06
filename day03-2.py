import numpy as np
import string
import io

#day 3 challenge 2

#the real input is input03.
#There's also a test03-1.txt, which is used to make sure that the code runs correctly.
#And a padded test03-1b.txt and input03b
#test03-1c.txt and test03-1d.txt were purely for testing to make sure that the (messy)
#functions worked well.
#For that, the numbers we want are 467*35=16345, 755*598=451490
#the sum is 467835
sum = 0

#f = open("test03-1b.txt", "r", encoding="utf-8")
f = open("input03b", "r", encoding="utf-8")
#f = open("test03-1d.txt", "r", encoding="utf-8")
currentline = f.readline()
nextline = f.readline()
inputline = f.readline()
# need a parser to:
# * find stars ("gears")
# * find if there are two numbers within ±1 of them
# * what those numbers are
# * and multiply them together & add to the sum
# test input is 10x10 grid, actual is 140x140
# both were padded out to 12x12 and 142x142 (hence the b)

while inputline != "": 
	position = 1
	prevline = currentline
	currentline = nextline
	nextline = inputline
	# search to find gears on the line
	while position < (len(currentline)-1):
		if currentline[position] == '*':
			# look for numbers
			# backwards and forwards are easy, but above/below may present problems. Unsure if the pathological case exists where there are two numbers on the same line above/below a *. Search needs to not stop at two, but see if there's a third.
			# Current plan is to just multiply everything the search finds, but note how many numbers were found.
			# 'backwards':
			gearnumbers = 0
			gearratio = 1
			n = position-1
			for digit1 in string.digits:
				if digit1 == currentline[n]:
					gearnumbers += 1
					numberend = n
					numberstart = n
					for digit2 in string.digits:
						if digit2 == currentline[n-1]:
							numberstart = n-1
							for digit3 in string.digits:
								if digit3 == currentline[n-2]:
									numberstart = n-2
					gearratio *= int(currentline[numberstart:numberend+1])
			# look forward
			n = position+1
			for digit1 in string.digits:
				if digit1 == currentline[n]:
					gearnumbers += 1
					numberend = n
					numberstart = n
					for digit2 in string.digits:
						if digit2 == currentline[n+1]:
							numberend = n+1
							for digit3 in string.digits:
								if digit3 == currentline[n+2]:
									numberend = n+2
					gearratio *= int(currentline[numberstart:numberend+1])
			# diagonals are fraught
			# need to look backwards from top/bottom left, then forwards if needed
			# up and back diagonal:
			n = position-1
			offset = n
			for digit1 in string.digits:
				if digit1 == prevline[n]:
					gearnumbers += 1
					numberend = n
					numberstart = n
					for digit2 in string.digits:
						if digit2 == prevline[n-1]:
							numberstart = n-1
							for digit3 in string.digits:
								if digit3 == prevline[n-2]:
									numberstart = n-2
							for digit3 in string.digits:
								if digit3 == prevline[n+1]:
									numberend = n+1
					for digit2 in string.digits:
						if digit2 == prevline[n+1]:
							numberend = n+1
							for digit3 in string.digits:
								if digit3 == prevline[n+2]:
									numberend = n+2
					gearratio *= int(prevline[numberstart:numberend+1])
					offset = numberend
			# look up center (or up and right)
			n = offset+1
			offset = n
			if n == position or n == position+1:
				for digit1 in string.digits:
					if digit1 == prevline[n]:
						gearnumbers += 1
						numberend = n
						numberstart = n
						for digit2 in string.digits:
							if digit2 == prevline[n+1]:
								numberend = n+1
								for digit3 in string.digits:
									if digit3 == prevline[n+2]:
										numberend = n+2
						gearratio *= int(prevline[numberstart:numberend+1])
						offset = numberend
			# look up and right diagonal
			n = offset+1
			if n == position+1:
				for digit1 in string.digits:
					if digit1 == prevline[n]:
						gearnumbers += 1
						numberend = n
						numberstart = n
						for digit2 in string.digits:
							if digit2 == prevline[n+1]:
								numberend = n+1
								for digit3 in string.digits:
									if digit3 == prevline[n+2]:
										numberend = n+2
						gearratio *= int(prevline[numberstart:numberend+1])
			# down and back diagonal
			n = position-1
			offset = n
			for digit1 in string.digits:
				if digit1 == nextline[n]:
					gearnumbers += 1
					numberend = n
					numberstart = n
					for digit2 in string.digits:
						if digit2 == nextline[n-1]:
							numberstart = n-1
							for digit3 in string.digits:
								if digit3 == nextline[n-2]:
									numberstart = n-2
							for digit3 in string.digits:
								if digit3 == nextline[n+1]:
									numberend = n+1
					for digit2 in string.digits:
						if digit2 == nextline[n+1]:
							numberend = n+1
							for digit3 in string.digits:
								if digit3 == nextline[n+2]:
									numberend = n+2
					gearratio *= int(nextline[numberstart:numberend+1])
					offset = numberend
			# forward search from directly below (or right)
			n = offset+1
			offset = n
			if n == position or n == position+1:
				for digit1 in string.digits:
					if digit1 == nextline[n]:
						gearnumbers += 1
						numberend = n
						numberstart = n
						for digit2 in string.digits:
							if digit2 == nextline[n+1]:
								numberend = n+1
								for digit3 in string.digits:
									if digit3 == nextline[n+2]:
										numberend = n+2
						gearratio *= int(nextline[numberstart:numberend+1])
						offset = numberend
			# forward search from below and to the right
			n = offset+1
			if n == position+1:
				for digit1 in string.digits:
					if digit1 == nextline[n]:
						gearnumbers += 1
						numberend = n
						numberstart = n
						for digit2 in string.digits:
							if digit2 == nextline[n+1]:
								numberend = n+1
								for digit3 in string.digits:
									if digit3 == nextline[n+2]:
										numberend = n+2
						gearratio *= int(nextline[numberstart:numberend+1])
			# ...
			print("per star:",gearnumbers,gearratio)
			if gearnumbers == 2:
				sum += gearratio
		position += 1 #since '**' never appears, there's a chance I could also move forwards another 1 if there's a hit.
	inputline = f.readline()
f.close()
print(sum)
