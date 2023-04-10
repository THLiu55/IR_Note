#!/usr/bin/env python3

# open file for reading line-by-line
with open( 'words.txt', 'r' ) as f:
    # iterate through the lines
    for line in f:
        # print the line (after removing the newline at the end)
        print( line.strip() )

# the file is closed automatically once the 'with' block is ended