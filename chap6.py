# Enter your answrs for chapter 6 here
# Name: Michael Krieger


# Ex. 6.6

def first (word):
	return word[0]

def last (word):
	return word[-1]

def middle (word):
	return word[1:-1]


>>> middle('ab')
''
>>> middle('a')
''
>>> middle(' ')
''




def first (word):
	return word[0]

def last (word):
	return word[-1]

def middle (word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))


	# Ex. 6.7
import math
def is_power(a, b):
	if (b) == 1 and (a) !=1: return False
	if (b) == 1 and (a) ==1: return True
	if (b) == 0 and (a) !=1: return False
	power = int (math.log (a, b) +0.5)
	return b ** power == a