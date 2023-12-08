import numpy as np
import re

#day 7 challenge 2

#the real input is input07.
#There are also test07-1 and test07-2, which are used to make sure that the code runs correctly.
#handstrength: AKQT98765432J
# it's poker, so we have 5 of a kind > 4 of a kind > full house (3,2) >3 >2 pair >pair > high
# difference: for strength in same type, card order matters (33332 > 2AAAA)
# note for here that J are jokers, not jacks. So weakest individual card but for x of a kind always make the hand the best. (so, regex time?)

#test07-1: (hand, bid)
'''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

# need a parser to:
# * get cards
# * sort hands to find rank
# * grab bid column and multiply it out
# hand strength is type, then based on values of cards in it.
# can sort with built in stuff

cards = np.genfromtxt("input07", delimiter=" ", dtype=None, encoding=None)
#cards = np.genfromtxt("test07-1", delimiter=" ", dtype=None, encoding=None)
#hands, an empty array based off of cards, but with with columns of "type", "label", and "rank" (and the same number of rows
hands = np.zeros(len(cards), dtype=[('type','f4'),('label','f8'),('bid','int')])
# going through initial array and getting strength numbers:
for n in np.arange(len(cards)):
	# type:
	if len(re.findall("[AJ]", cards[n][0])) == 5 or len(re.findall("[KJ]", cards[n][0])) == 5 or len(re.findall("[QJ]", cards[n][0])) == 5 or len(re.findall("[TJ]", cards[n][0])) == 5 or len(re.findall("[9J]", cards[n][0])) == 5 or len(re.findall("[8J]", cards[n][0])) == 5 or len(re.findall("[7J]", cards[n][0])) == 5 or len(re.findall("[6J]", cards[n][0])) == 5 or len(re.findall("[5J]", cards[n][0])) == 5 or len(re.findall("[5J]", cards[n][0])) == 5 or len(re.findall("[3J]", cards[n][0])) == 5 or len(re.findall("[2J]", cards[n][0])) == 5:
		hands[n][0] = 5
	elif len(re.findall("[AJ]", cards[n][0])) == 4 or len(re.findall("[KJ]", cards[n][0])) == 4 or len(re.findall("[QJ]", cards[n][0])) == 4 or len(re.findall("[TJ]", cards[n][0])) == 4 or len(re.findall("[9J]", cards[n][0])) == 4 or len(re.findall("[8J]", cards[n][0])) == 4 or len(re.findall("[7J]", cards[n][0])) == 4 or len(re.findall("[6J]", cards[n][0])) == 4 or len(re.findall("[5J]", cards[n][0])) == 4 or len(re.findall("[4J]", cards[n][0])) == 4 or len(re.findall("[3J]", cards[n][0])) == 4 or len(re.findall("[2J]", cards[n][0])) == 4:
		hands[n][0] = 4
	else:
		pairs = (len(re.findall("A", cards[n][0])) == 2) + (len(re.findall("K", cards[n][0])) == 2) + (len(re.findall("Q", cards[n][0])) == 2) + (len(re.findall("T", cards[n][0])) == 2) + (len(re.findall("9", cards[n][0])) == 2) + (len(re.findall("8", cards[n][0])) == 2) + (len(re.findall("7", cards[n][0])) == 2) + (len(re.findall("6", cards[n][0])) == 2) + (len(re.findall("5", cards[n][0])) == 2) + (len(re.findall("4", cards[n][0])) == 2) + (len(re.findall("3", cards[n][0])) == 2) + (len(re.findall("2", cards[n][0])) == 2)
		if len(re.findall("[AJ]", cards[n][0])) == 3 or len(re.findall("[KJ]", cards[n][0])) == 3 or len(re.findall("[QJ]", cards[n][0])) == 3 or len(re.findall("[TJ]", cards[n][0])) == 3 or len(re.findall("[9J]", cards[n][0])) == 3 or len(re.findall("[8J]", cards[n][0])) == 3 or len(re.findall("[7J]", cards[n][0])) == 3 or len(re.findall("[6J]", cards[n][0])) == 3 or len(re.findall("[5J]", cards[n][0])) == 3 or len(re.findall("[4J]", cards[n][0])) == 3 or len(re.findall("[3J]", cards[n][0])) == 3 or len(re.findall("[2J]", cards[n][0])) == 3:
			if pairs == 1:
				hands[n][0] = 3.5 # full house
			else:
				hands[n][0] = 3 # 3 of a kind
		elif pairs == 2:
			hands[n][0] = 2.5 # 2 pair
		elif (pairs == 1) or (len(re.findall("J", cards[n][0])) == 1):
			hands[n][0] = 2
	# high card doesn't need anything changed, since the value is already zero
	# label:
	# it's just a silly regex that will tweak the ascii values 
	# Effectively converting the strings to base 15 numbers:
	foo = re.sub("A", "E", cards[n][0])
	bar = re.sub("K", "D", foo)
	baz = re.sub("Q", "C", bar)
	qux = re.sub("J", "1", baz)
	hands[n][1] = int(re.sub("T", "A", qux), 15)
	# rank:
	hands[n][2] = cards[n][1]

print(hands)
hands.sort()
#alternatively, by hand sorting:
# doesn't work, possibly I need a different data structure
'''
sorted = False
while (sorted == False):
	sorted = True
	for n in np.arange(len(hands)-1):
		if (hands[n][0] > hands[n+1][0]):
			sorted = False
			temp = hands[n]
			hands[n] = hands[n+1]
			hands[n+1] = temp
		elif (hands[n][0] == hands[n+1][0]) and (hands[n][1] > hands[n+1][1]):
			sorted = False
			temp = hands[n]
			hands[n] = hands[n+1]
			hands[n+1] = temp

'''
# finding winnings after everything is sorted:
winnings = 0
for n in np.arange(len(hands)):
	winnings += ((n+1)*hands[n][2])
print(winnings)
print(hands)
#answer is between 254377082 and 254923520

