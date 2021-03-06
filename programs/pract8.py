import string

def checkPan(vals):
	for val in vals:
		if (val < 1):
			return False
	return True

chars = 'abcdefghijklmnopqrstuvwxyz'# list of all lowercase letterss
alphabet = {}

# this loop fills the alphabet dictionary with letters as keys and zeros as values
for char in chars:
	alphabet[char] = 0

inpStr = input("Please enter the string you wanna check \n")
# inpStr = "the quick brown fox jumps over the lazy dog"

# analyze the input string after switching all of its letters to lowercase
for c in inpStr.lower():
	if c in chars:
		alphabet[c] += 1

vals = alphabet.values()

# call the check function and pass the list of values to it
check = checkPan(vals)

if (check):
	print ("it's a pangram")
else:
	print ("not a pangram")