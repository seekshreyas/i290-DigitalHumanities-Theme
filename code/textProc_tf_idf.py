#! /usr/bin/python
from __future__ import division
import nltk
import random
import re, pprint, os, numpy


path = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

ANfiles = ['AN-raw.txt', 'AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
#ANfiles = ['AN-1.txt', 'AN-2.txt', ]

stopW = nltk.corpus.stopwords.words('english')


texts = []

listing = os.listdir(path)

for infile in ANfiles:

	url = path + infile
	# url = path + "AN-raw.txt"
	f = open(url)
	raw = f.read()

	f.close()

	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	texts.append(text)

# print texts[:10]
print "prepared ", len(texts), "documents ..."
print "The can be accessed using texts[0] - texts[" + str(len(texts) -1) + "]"



#Load the list of texts into a TextCollection object
collection = nltk.TextCollection(texts)
print "Created a collection of", len(collection), "terms."

# get list of unique terms
unique_terms = list(set(collection))

print "Unique terms found:", len(unique_terms)


# function to create Tf*IDf vector for one document. For each
# of our unique words, we have a feature which is td * idf for 
# for that word in the current document

def tfidf(document):
	word_tfidf = []

	for word in unique_terms:
		word_tfidf.append(collection.tf_idf(word, document))

	return word_tfidf


## and here we actually call the function and create our array of vectors.

vectors = [numpy.array(tfidf(f)) for f in texts]

print "Vectors created"

print "First 50 words are", unique_terms[:20]
print "First 10 stats for the first document are:", vectors[0][0:20]
print "First 10 stats for the second document are:", vectors[1][0:20]