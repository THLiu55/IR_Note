#!/usr/bin/env python3


with open( 'words.txt', 'r' ) as f:
	for line in f:
		# remove the newline from the line
		line = line.strip()

		# divide the line into words (split on spaces by default)
		words = line.split()

		# iterate through the words
		for word in words:
			# print a word with parentheses around it (no newline)
			print( '({})'.format( word ), end='' )

		# print a newline for the end of this line
		print()