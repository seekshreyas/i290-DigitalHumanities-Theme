#! /usr/bin/python
import math
import nltk

from nltk.corpus import wordnet as wn

corpus_root = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

ANfiles = ['AN-raw.txt', 'AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt', ]

interestingWords = ['power', 'faith', 'poor', 'loyal']

stopW = nltk.corpus.stopwords.words('english')

raw = []
i = 0

def percent(count, total):
	perc = (float(count)/float(total)) * 100
	return round(perc, 2)


def basicTextQuants(text):
	totLength = len(text)
	tokens = nltk.word_tokenize(text)
	vocab = len(sorted(set(tokens)))
	lexicalRich = float(totLength)/ float(vocab)
	
	words = []
	for t in tokens:
		words.append(t.lower())

	fDist = nltk.probability.FreqDist(words)
	topWords = fDist.keys()
	uniqueWords = fDist.hapaxes()

	# fDist.plot()

	print "total words (with repeats) length: \t\t\t", totLength
	print "total vocab (no repeats - including punctuation):\t", vocab
	print "lexical richness (i.e. total/vocab):\t", lexicalRich
	print "top 50 words (without stemming/ lemmatizing):\n", topWords[:50], "\n"
	print "words (showing only 10) that occur once (hapaxes):\n", uniqueWords[:50], "\n"

	print "~~~~~ after removing stopwords ~~~~~~"

	wordsWithoutStopW = []

	# for t in tokens:
	content = [t.lower() for t in tokens if t.lower() not in stopW]

	contentFrac = round(len(content)/float(totLength), 2)
	print "content words (without stopwords but repeat): \t", len(content)
	print "content percentage: \t", contentFrac

	wordSynonyms = {}
	wordHyponyms = {}

	print "~~~~~ after stemming ~~~~~~"
	porter = nltk.PorterStemmer()

	wordsStemmed = [porter.stem(c) for c in content]
	# print wordsStemmed

	# word percentage
	for eachWord in interestingWords:
		wordPercent = percent(text.count(eachWord), totLength)
		wordPercentWithoutStopW = percent(content.count(eachWord), len(content))
		wordPercentWithStemming = percent(wordsStemmed.count(porter.stem(eachWord)), len(wordsStemmed))


		wordSynonyms[eachWord] = wn.synsets(eachWord)

		# context = text.concordance(eachWord)

		# wordHyponyms[eachWord] = eachWord.hyponym
		
		print "word count for: \t\t", eachWord, "\t:", text.count(eachWord) 
		print "word percentage for: \t\t", eachWord, "\t:", wordPercent, "\n"

		print "word Synonyms for: \t\t", eachWord, "\t", wordSynonyms[eachWord], "\n"

		# print "word context for: \t\t", eachWord, "\n", context
		# print "word Hyponyms for: \t\t", eachWord, "\t", wordHyponyms[eachWord], "\n"
		
		print "~~~~~ after removing stopwords ~~~~~~"

		print "word count for: \t\t", eachWord, "\t:", wordsStemmed.count(eachWord) 
		print "word percentage for: \t\t", eachWord, "\t:", wordPercentWithoutStopW, "\n"

		print "~~~~~ after Porter stemming ~~~~~~"
		print "word count for: \t\t", eachWord, "\t:", wordsStemmed.count(porter.stem(eachWord)) 
		print "word percentage for: \t\t", eachWord, "\t:", wordPercentWithStemming, "\n"

		print "~~~~~~~~~~~"

for file in ANfiles:
	# wordlists.append(nltk.corpus.PlaintextCorpusReader(corpus_root, ANfiles))
	path = corpus_root + file

	print "*************** " + file + " Stats ***************\n"

	f = open(path)
	raw.append(f.read())
	# print wordlists[findex].words()
	basicTextQuants(raw[i])
	i += 1

	print "---\n\n\n"
