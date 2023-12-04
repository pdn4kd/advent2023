import numpy as np
import string
import io

#day 4 challenge 1

#the real input is input04.
#There's also a test04-1.txt, which is used to make sure that the code runs correctly.
'''
	card 1 has four winning numbers (41, 48, 83, 86, 17), so is worth 8 points.
    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.
'''
# test array has 5 winning, 8 yours per line to match
# actual input has 10 winning, 25 yours per line to match
# so what if I just had a giant array and on each line matched 0-9 with 10-24?
sum = 0
cards = np.genfromtxt("input04-1c", dtype=None, delimiter=',')
for card in cards:
	winnings = card[0:10]
	yours = card[10:36]
	matches = 0
	for winning in winnings:
		for you in yours:
			if winning == you:
				matches +=1
	if matches > 0:
		sum += 2**(matches-1)

'''
f = open("input04", "r", encoding="utf-8")
inputline = f.readline()
# need a parser to:

while inputline != "":
	# ...
	inputline = f.readline()

f.close()
'''
print(sum)
sum = 0
cards = np.genfromtxt("test04-1c", dtype=None, delimiter=',')
for card in cards:
	winnings = card[0:5]
	yours = card[5:]
	matches = 0
	for winning in winnings:
		for you in yours:
			if winning == you:
				matches +=1
	if matches > 0:
		sum += 2**(matches-1)
print(sum)
