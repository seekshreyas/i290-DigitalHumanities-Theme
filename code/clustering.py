
from __future__ import division
import nltk
import os
import sys
from collections import defaultdict
from nltk.tag import pos_tag
import numpy as np

import string
import nltk
import random
import re, pprint, os, numpy
from sklearn import decomposition
#import sklearn.feature_extraction.text.Vectorizer
from nltk.stem import porter
from nltk.corpus import stopwords

__author__ = 'rahmaniacc'


def main():
    path = 'Users/Shreyas/Documents/_Berkeley/sem2/i290DigitalHumanities/Project/ThemeDetection/corpus/'

    n_top_words = 20
    # ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
    # ANfiles = ['TAON-1.txt', 'TAON-2.txt', 'TAON-3.txt', 'TAON-4.txt']
    #ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt']
    ANfiles = ['AN-1.txt','AN-27.txt']
    stopW = nltk.corpus.stopwords.words('english')

    #pos tag values to filter nouns and verbs
    nouns = ['NNP','NNPS','NN','NNS','PRP', 'PRP$']
    verbs = ['MOD', 'V', 'VD', 'VG', 'VN', 'VB', 'VBD', 'VBG', 'VBZ', 'VBN', 'VBP', 'RB', 'RBR', 'RBS']
    possesive = ['POS']

    texts = []
    raw = ""
    #listing = os.listdir(path)

    wc = defaultdict()
    context_list = []
    clusters = {}
    document = []
    #all_clusters = []
    doc_no = 0
    for infile in ANfiles:
        url = path + infile
        f = open(url)
        raw += f.read()
        f.close()

        noun_wc = defaultdict(int)
        verb_list = []
        noun_list = []
        document.append(nltk.Text([w.lower() for w in nltk.word_tokenize(raw) if w not in stopW]))
        for line in raw.split('\n\n'):
            tokens = nltk.pos_tag([w.lower() for w in nltk.word_tokenize(line) if w not in stopW])
            w_noun = [t[0] for t in tokens if t[1] in nouns]
            w_verb = [t[0] for t in tokens if t[1] in verbs]

            for n in w_noun:
                noun_list.append(n)
                for v in w_verb:
                    verb_list.append(v)
                    noun_wc[(n, v)] += 1

        verb_list = list(set(verb_list))
        noun_list = list(set(noun_list))
        vectors = []
        for n in noun_list:
                vectors.append([np.array(getValue(n,v,noun_wc)) for v in verb_list])

        vector_array = [np.array(vectors)]

        nmf = decomposition.NMF(n_components=3).fit(vectors)
        topic_list = []
        for topic_idx, topic in enumerate(nmf.components_):
            topic_list.append([noun_list[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        filtered_list = set(topic_list[0]) ^ set(topic_list[1]) ^ set(topic_list[2])
        counter = 0
        for t in topic_list:
            topic_list[counter] = [x for x in filter(lambda x:x in filtered_list, t)]
            counter += 1
        clusters[doc_no] = topic_list
        doc_no += 1
    cluster_stats = {}
    freq_stats = {}

    for i in range(0,len(document)):
        topic_number = 0
        for cl in clusters[i]:

            for t in cl:


                if t in cluster_stats:
                    templist = cluster_stats[t]
                    if not 'chapter' + str(i) + '_topic' + str(topic_number) in templist:
                        templist.append('chapter1_topic' + str(topic_number))
                    cluster_stats[t] = templist
                else:
                    cluster_stats[t] = ['chapter' + str(i) + '_topic' + str(topic_number)]

                if t in freq_stats:
                    templist = freq_stats[t]
                    templist.append(document[i].count(t))
                    freq_stats[t] = templist
                else:
                    freq_stats[t] = [document[i].count(t)]

            topic_number += 1

    print 'press w for a list of all words in all clusters'
    print 'press any number between 1 and 27 to print all clusters in the corresponding document'
    print 'press s for stats about a particular word'

    choice = raw_input()

    if choice == 'w':
        for i in range(0,len(document)):
            print 'document ' + str(i+1)
            topic_number = 0
            for cl in clusters[i]:
                print str(topic_number) + '\n'
                for t in cl:
                    print t
                    print '\n'
            topic_number += 1

    elif choice == 's':
        word_input = raw_input('enter a word')
        if word_input in freq_stats:
            count =0
            stat = freq_stats[word_input]
            for freq in stat:
                print word_input + "occurs in chapter" + str(count) + ' ' + str(freq) + ' times'
                print '\n'
                count += 1

            cluster_stat = cluster_stats[word_input]
            print word_input + ' occurs in these clusters' + "\n"
            for c in cluster_stat:
                print c + '\n'


    else:
        cl = clusters[int(choice)-1]
        counter =0

        for t in cl:
            print 'topic'+ str(counter)
            for w in t:
                print w + '\n'
            counter += 1


    i = 0

def getValue(n,v,count_dict):
    if (n,v) in count_dict:
        return count_dict[(n,v)]
    else:
        return 0

if __name__ == "__main__":
    main()

