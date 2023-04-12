#!/usr/bin/env python3
##
# Sample solution to Worksheet 5.
# 
# Runs a query against 3 simple short documents using vector model with binary weights.
#
# This approach follows the mathematical definitions
#   (i.e. it actually creates a vector of length N for every document,
#     where N is the number of distinct terms in the whole collection)
# This is **not** a very efficient approach and will not scale well.
# However, it should give the correct cosine similarity for these documents.
##

from math import sqrt
import porter

documents = {
	'd1':['Shipment', 'of', 'gold', 'damaged', 'in', 'a', 'fire'],
	'd2':['Delivery', 'of', 'silver', 'arrived', 'in', 'a', 'silver', 'truck'],
	'd3':['Shipment', 'of', 'gold', 'arrived', 'in', 'a', 'large', 'truck']
	}
query = ['gold', 'silver', 'truck']

# load stopwords into appropriate data structure
stopwords = set()
with open( 'stopwords.txt', 'r' ) as f:
	for line in f:
		stopwords.add(line.rstrip())

# load the porter stemmer
stemmer = porter.PorterStemmer()

collection = {} # entire corpus: key is a term, value is the index of that term in vectors
vectors = {} # key is docid, value is list (key is term, value is 1/0 weight)
lengths = {} # key is docid, value is vector length

# figure out the collection
# loop through each document's contents (we don't need the docids yet)
for doc in documents.values():
	# loop through each term in each document
	for term in doc:
		term = term.lower() # convert to lowercase
		if term not in stopwords: # ignore stopwords
			term = stemmer.stem( term ) # get stem
			# only deal with new terms not already in the collection
			if term not in collection:
				# the length of the collection tells me how many terms I already have
				# ... so add this new term with the next index
				collection[term] = len( collection )

# calculate vectors by iterating through all documents
for did in documents:
	vector = [0] * len( collection ) # start with zeroes of the correct length
	
	# iterate the terms in a document
	for term in documents[did]:
		term = term.lower() # lowercase
		if term not in stopwords: # ignore stopwords
			term = stemmer.stem( term ) # stem
			index = collection[term] # find the index in the vector for this term
			vector[index] = 1 # set the weight to be 1
	vectors[did] = vector # save this vector in a dictionary of vectors
	
	# calculate the length of the vector
	length = 0
	for n in vector:
		# for binary weights this won't matter because 1 squared = 1
		# ... but this is the mathematically correct formula for length
		length += pow(n,2)
	lengths[did] = sqrt( length )

# do the same for the query
query_vector = [0] * len( collection )
for term in query:
	if term not in stopwords:
		term = stemmer.stem(term)
		if term in collection:
			index = collection[term]
			query_vector[index] = 1
query_length = 0
for n in query_vector:
	query_length += n
query_length = sqrt(query_length)

# now calculate the cosine similarity
#   sims is a dictionary where key will be document id
#   and value will be cosine similarity between the document and the query
sims = {}

for did in vectors:
	sim = 0
	doc = vectors[did]
	# dot product - multiple the weights in the same vector positions
	for i in range( len( doc ) ):
		sim += doc[i] * query_vector[i]
	# divide by the product of the vector lengths and store in the dictionary
	sims[did] =  sim / ( lengths[did] * query_length )

# print docids and similarity scores sorted by similarity (descending)
for did in sorted( sims, key=sims.get, reverse=True ):
	print( '{}: {}'.format( did, sims[did] ) )