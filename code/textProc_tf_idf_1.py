#! /usr/bin/python
from __future__ import division
import string
import nltk
import random
import re, pprint, os, numpy
from sklearn import decomposition
#import sklearn.feature_extraction.text.Vectorizer
from stemming import porter
from nltk.corpus import stopwords

def main():
    #path = '/Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'
    path = '/home/rahmaniac/i290-DigitalHumanities-Theme/corpus/'
    n_top_words = 20
    ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
    # ANfiles = ['TAON-1.txt', 'TAON-2.txt', 'TAON-3.txt', 'TAON-4.txt']
    #ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt']

    stopW = nltk.corpus.stopwords.words('english')
    nouns = ['NNP','NNPS','NN']
    texts = []

    listing = os.listdir(path)

    for infile in ANfiles:
        url = path + infile
        # url = path + "AN-raw.txt"
        f = open(url)
        raw = f.read()

        f.close()
	pos_tag = []
        for line in raw.split('\n\n'):
        	pos_tag.append(nltk.pos_tag(removePunctuations(nltk.word_tokenize(line))))
	unigrams = [x[0] for x in filter(lambda x:len(x) == 2 and x[1] not in nouns, pos_tag)]
        unigrams = filter(lambda x:x not in "''", unigrams)

        word_list = [word for word in unigrams if word not in stopW]
        #word_list = [porter.stem(word) for word in word_list if word]
        #list = [word for word in list if word not in stopwords('english')]
        text = nltk.Text(word_list)

        texts.append(text)

    # print texts[:10]
    print "prepared ", len(texts), "documents ..."
    print "The can be accessed using texts[0] - texts[" + str(len(texts) - 1) + "]"



    #Load the list of texts into a TextCollection object
    collection = nltk.TextCollection(texts)
    print "Created a collection of", len(collection), "terms."

    # get list of unique terms
    unique_terms = list(set(collection))

    print "Unique terms found:", len(unique_terms)


    # function to create Tf*IDf vector for one document. For each
    # of our unique words, we have a feature which is td * idf for
    # for that word in the current document



    # vectors by tf idf
    vectors = [numpy.array(tfidf(f, collection, unique_terms)) for f in texts]

    #vectors by word count
    #vectors = [numpy.array(BOW(f,unique_terms)) for f in texts]

    print "Vectors created"

    print "First 50 words are", unique_terms[:20]
    # print "First 10 stats for the first document are:", vectors[0][0:20]
    # print "First 10 stats for the second document are:", vectors[1][0:20]

    ## clustering : Group Average Agglomerative
    # clusterer = nltk.cluster.GAAClusterer(num_clusters=3)
    # clusters = clusterer.cluster(vectors, True)

    ## k-means clustering
    # clusterer = nltk.cluster.KMeansClusterer(2, nltk.cluster.euclidean_distance)
    # print "starting clustering"
    # clusters = clusterer.cluster(vectors, assign_clusters=True, trace=False)
    #
    # print "clusterer: ", clusterer
    # print "clustered: ", vectors
    # print "As: ", clusters
    # print "Means: ", clusterer.means()

    # show the dendrogram
    # clusterer.dendrogram().show()

    #print numpy. vectors

    nmf = decomposition.NMF(n_components=5).fit(vectors)
    print nmf
    i =0
    for topic_idx, topic in enumerate(nmf.components_):
        #print i
        print topic_idx
        #print unique_terms[i] for i in topic.argsort()[:-n_top_words - 1:-1]
        # print'-----------------------------------'

        print("\n ".join([unique_terms[i]
                           for i in topic.argsort()[:-n_top_words - 1:-1]]))

        print '------------------------------'

def removePunctuations(tokens):
    returnlist = []
    for token in tokens:
        for punct in string.punctuation:
            token = token.replace(punct, '')
            token = token.rstrip(punct)
        if len(token) > 0:
            returnlist.append(token.rstrip('\n'))
    return returnlist

def tfidf(document,collection,unique_terms):
    word_tfidf = []
    for word in unique_terms:
        word_tfidf.append(collection.tf_idf(word, document))
    return word_tfidf


## and here we actually call the function and create our array of vectors.


## creating vectors based on count
def BOW(document,unique_terms):
    word_counts = []
    for word in unique_terms:
        word_counts.append(document.count(word))
    return word_counts


if __name__ == "__main__":
    main()
