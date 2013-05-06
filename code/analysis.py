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

path = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'
# ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt']

stopW = stopwords.words('english');



allText = []
allDocument = []

listing = os.listdir(path)

for fname in ANfiles:
	url = path + fname
	
	# file operations
	f = open(url)
	raw = f.read()
	f.close()

	#preprocessing of text
	doc = Document(raw, name=fname)
	allDocument.append(doc)

	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	allText.append(text);




print "cleaned up text:", len(allText[0])






