#! /usr/bin/python

from __future__ import division
import string
import nltk
import random
import re, pprint, os, numpy
from sklearn import decomposition
#import sklearn.feature_extraction.text.Vectorizer
from nltk.stem import porter
from nltk.corpus import stopwords
from pattern.vector import Document, Corpus, HIERARCHICAL

import en


corpusText = []

def processText(corpus):
	# r = the raw string on file read

	meta = ['power', 'faith', 'fear', 'anger', 'revenge']

	count = 1
	for doc in corpus:
		keywordSummary = en.content.keywords(doc, top=10, nouns=True, singularize=False, filters=meta)
		docCategories = en.content.categorise(doc)

		displayAnalysis(count, keywordSummary, docCategories)

		

	
def displayAnalysis(c, keywords, categories):
	print "AN-", c, " Analsis:"
	print "=========================="
	print

	print "KEYWORDS:"
	print keywords
	print "-------------------"
	print

	print "CATEGORIES OF WORDS:"
	for item in categories:
		print item.name
		print item.count
		print item.words
		print item.type
		print "*************"



def main():
	path = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

	# ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
	ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt']

	dirListing = os.listdir(path)

	for fname in ANfiles:
		url = path + fname

		#file operations
		f = open(url)
		raw = f.read()
		f.close()

		corpusText.append(raw)

	processText(corpusText)


	
if __name__ == "__main__":
    main()






