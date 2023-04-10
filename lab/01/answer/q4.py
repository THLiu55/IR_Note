#!/usr/bin/env python3

# dictionary to store word frequencies
#   key: word
#   value: frequency
allwords = {}

with open( 'words.txt', 'r' ) as f:
	for line in f:
		words = line.split();
		for word in words:
			# convert the word to lowercase
			word = word.lower()

			# this word has never been seen before
			# ... so it is not contained in allwords
			if word not in allwords:
				allwords[word] = 1
			# this is not a new word, so count that we found it again
			else:
				allwords[word] += 1

# print the words and frequencies
# (note that dictionaries do not have any particular order)
for w in allwords:
	print( '{}: {}'.format( allwords[w], w ) )