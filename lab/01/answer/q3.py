#!/usr/bin/env python3

with open( 'words.txt', 'r' ) as f:
	for line in f:
		words = line.split();
		for word in words:
			# convert the word to lowercase as we print it
			print( '({})'.format( word.lower() ), end='' )
		print()