import string
import io

sum = 0

# read in file as strings line by line
# actual file is named input, but a small test one is named test01-1.txt, which should generate lines of 12, 38, 15, and 77, resulting in a sum of 142.
f = open("input01", "r", encoding="utf-8")
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
