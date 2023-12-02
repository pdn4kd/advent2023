'''Takes the wrong approach by using an input file that I manually ran regexen on to convert the number names into numbers'''
import string
import io

sum = 0

# read in file as strings line by line
f = open("input-wrong.txt", "r", encoding="utf-8")
f = open("test01-2-wrong.txt", "r", encoding="utf-8")
inputline = f.readline()

while inputline != "":
	# read through a line to find the ones digit (ends up at the last number character)
	for character in inputline:
		for digit in string.digits:
			if character == digit:
				ones = int(digit)
	# flip string
	inputline = inputline[::-1]
	# read through a line to find the tens digit (ends up at the last number character in the flipped string)
	for character in inputline:
		for digit in string.digits:
			if character == digit:
				tens = int(digit)
	print( (tens * 10) + ones)
	sum += ((tens * 10 ) + ones)
	inputline = f.readline()
f.close()
print(sum)
