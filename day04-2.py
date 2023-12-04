import numpy as np
import string
import io

#day 4 challenge 2

#the real input is input04.
#There's also a test04-1.txt, which is used to make sure that the code runs correctly.
# test array has 5 winning, 8 yours per line to match
# actual input has 10 winning, 25 yours per line to match

cards = np.genfromtxt("input04-1c", dtype=None, delimiter=',')
sum = len(cards) #209
cardcount = np.ones(len(cards))
for cardpos in np.arange(len(cards)):
	winnings = cards[cardpos][0:10]
	yours = cards[cardpos][10:36]
	matches = 0
	for winning in winnings:
		for you in yours:
			if winning == you:
				matches +=1
	if matches > 0:
		for n in np.arange(matches):
			cardcount[cardpos+n+1] += cardcount[cardpos]
print(np.sum(cardcount))

cards = np.genfromtxt("test04-1c", dtype=None, delimiter=',')
sum = len(cards) #6
cardcount = np.ones(len(cards))
for cardpos in np.arange(len(cards)):
	winnings = cards[cardpos][0:5]
	yours = cards[cardpos][5:14]
	matches = 0
	for winning in winnings:
		for you in yours:
			if winning == you:
				matches +=1
	if matches > 0:
		for n in np.arange(matches):
			cardcount[cardpos+n+1] += cardcount[cardpos]
print(np.sum(cardcount))

#should end up as 30
