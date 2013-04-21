#! /usr/bin/python
from __future__ import division
import nltk
import random
import re, pprint, os, numpy


path = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

# ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
# ANfiles = ['TAON-1.txt', 'TAON-2.txt', 'TAON-3.txt', 'TAON-4.txt']
ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt']

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


## creating vectors based on count
def BOW(document):
	word_counts = []
	for word in unique_terms:
		word_counts.append(document.count(word))
	return word_counts

# vectors by tf idf
# vectors = [numpy.array(tfidf(f)) for f in texts] 

#vectors by word count
vectors = [numpy.array(BOW(f)) for f in texts]
U,s,V = numpy.linalg.svd(vectors) # svd decomposition of A

print "Vectors created", len(vectors[0]), "after SVD decomposition", len(U)

# print "First 50 words are", unique_terms[:20]
for fileindex in U:
	print "First 10 stats for this document are:", fileindex[0:10]


# print "First 10 stats for the second document are:", vectors[1][0:20]
print "starting clustering"


## clustering : Group Average Agglomerative
clusterer = nltk.cluster.GAAClusterer(num_clusters=3)
clusters = clusterer.cluster(vectors, True)

## k-means clustering
# clusterer = nltk.cluster.KMeansClusterer(2, nltk.cluster.euclidean_distance)
# clusters = clusterer.cluster(U, assign_clusters=True, trace=False)

print "clusterer: ", clusterer
print "clustered: ", vectors
print "As: ", clusters
# print "Means: ", clusterer.means()

# show the dendrogram
clusterer.dendrogram().show()