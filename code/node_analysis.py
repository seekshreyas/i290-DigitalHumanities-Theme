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
color = 'rgbcmyk'

def processText(corpus):
	# r = the raw string on file read

	meta = stopwords.words('english')
	additionalFilters = ['prince', 'princess', 'sultan', 'sultana', 'genius']
	meta.append(additionalFilters)

	count = 1
	print "Arabian Nights Text Analysis"
	print "=============================\n"


	for doc in corpus:
		keywordSummary = en.content.keywords(doc, top=10, nouns=True, singularize=True, filters=additionalFilters)
		docCategories = en.content.categorise(doc)
		

		displayAnalysis(count, keywordSummary, docCategories)
		count +=1
	

		





def displayAnalysis(c, keywords, categories):
	print "\n\n\n\n"
	print "## AN-", c, " Analsis:\n"

	print "#### KEYWORDS:\n\t"

	print keywords


	print "\n#### CATEGORIES OF WORDS:\n"

	print "Summarization of Category results"
	print "<table>"
	print "<tr> 	<td>Primary Category</td> <td>Secondary Category</td> <td>Emotional Category</td></tr>"
	print "<tr> 	<td>%f</td> <td>%f</td> <td>%f</td>		</tr>" %(categories.primary, categories.secondary, categories.emotions)
	print "</table>"

	print "##### Categories in Details"

	selectedRIDCategories = ['need', 'sensation', 'restraint', 'anxiety', 'glory', 'positive affect', 'sadness', 'expressive behavior', 'affection', 'aggression']

	for item in categories:
		if (item.type == 'emotions' and item.count > 8):
			print "###### %s \n" %(item.name)
			print "- Total no of words in this category: %d" %(item.count)
			print "- Type of category (i.e. Primary/Secondary/Emotions): %s" %(item.type)
			print "- Set of Words in this category:"
			print "\n<pre> %s </pre>" %set(item.words)


def main():
	path = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

	ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
	# ANfiles = ['AN-1.txt', 'AN-2.txt']

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






