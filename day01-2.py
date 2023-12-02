'''a horrible hack that probably can't be expanded well and has some extraneous bits up front'''
import numpy as np
import string
import io

sum = 0

matchnumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# lengths: 3, 3, 5, 4, 4, 3, 5, 5, 4
# contrast with digits, which have a length of 1
# do a search across the string of length 5, then 4, then 3, then 1?
match1 = string.digits
match3 = "one","two","six"
match4 = "four","five","nine"
match5 = "three","seven","eight"

# read in file as strings line by line
#f = open("test01-2.txt", "r", encoding="utf-8")
f = open("input", "r", encoding="utf-8")
inputline = f.readline()

while inputline !="":
	for n in np.arange(len(inputline)-1):
		if len(inputline)-n >= 5:
			if inputline[n:n+5] == "three":
				ones = 3
			if inputline[n:n+5] == "seven":
				ones = 7
			if inputline[n:n+5] == "eight":
				ones = 8
		if len(inputline)-n >= 4:
			if inputline[n:n+4] == "four":
				ones = 4
			if inputline[n:n+4] == "five":
				ones = 5
			if inputline[n:n+4] == "nine":
				ones = 9
		if len(inputline)-n >= 3:
			if inputline[n:n+3] == "one":
				ones = 1
			if inputline[n:n+3] == "two":
				ones = 2
			if inputline[n:n+3] == "six":
				ones = 6
		if len(inputline)-n >= 1:
			for digit in string.digits:
				if inputline[n] == digit:
					ones = int(digit)
	backwards = np.arange(len(inputline)-1)[::-1]
	for n in backwards:
		if len(inputline)-n >= 5:
			if inputline[n:n+5] == "three":
				tens = 3
			if inputline[n:n+5] == "seven":
				tens = 7
			if inputline[n:n+5] == "eight":
				tens = 8
		if len(inputline)-n >= 4:
			if inputline[n:n+4] == "four":
				tens = 4
			if inputline[n:n+4] == "five":
				tens = 5
			if inputline[n:n+4] == "nine":
				tens = 9
		if len(inputline)-n >= 3:
			if inputline[n:n+3] == "one":
				tens = 1
			if inputline[n:n+3] == "two":
				tens = 2
			if inputline[n:n+3] == "six":
				tens = 6
		if len(inputline)-n >= 1:
			for digit in string.digits:
				if inputline[n] == digit:
					tens = int(digit)
	print( (tens * 10) + ones)
	sum += ((tens * 10 ) + ones)
	inputline = f.readline()

f.close()
print(sum)
