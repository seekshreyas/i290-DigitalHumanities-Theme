#! /usr/bin/python

import nltk
corpus_root = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

ANfiles = ['AN-raw.txt', 'AN-1.txt']

interestingWords = ['power', 'faith', 'poor', 'loyal']

raw = []
i = 0

def basicTextQuants(text):
	totLength = len(text)
	vocab = len(sorted(set(text)))
	lexicalRich = float(totLength)/ float(vocab)

	print "total words (with repeats) length: ", totLength
	print "total vocab (no repeats - including punctuation):", vocab
	print "lexical richnes (i.e. total/vocab):", lexicalRich

for file in ANfiles:
	# wordlists.append(nltk.corpus.PlaintextCorpusReader(corpus_root, ANfiles))
	path = corpus_root + file

	print "***************" + file + " Stats ***************"

	f = open(path)
	raw.append(f.read())
	# print wordlists[findex].words()
	basicTextQuants(raw[i])
	i += 1

	print "---"
