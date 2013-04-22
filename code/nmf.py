# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD

from __future__ import print_function

from time import time
from sklearn.feature_extraction import text
from sklearn import decomposition
from sklearn import datasets
import os
import nltk
n_samples = 3
n_features = 1000
n_topics = 5
n_top_words = 200
path = '/home/rahmaniac/i290-DigitalHumanities-Theme/corpus/'
#ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt']
ANfiles = ['AN-1.txt', 'AN-2.txt', 'AN-3.txt', 'AN-4.txt', 'AN-5.txt', 'AN-6.txt', 'AN-7.txt', 'AN-8.txt', 'AN-9.txt', 'AN-10.txt', 'AN-11.txt', 'AN-12.txt', 'AN-13.txt', 'AN-14.txt', 'AN-15.txt', 'AN-16.txt', 'AN-17.txt', 'AN-18.txt', 'AN-19.txt', 'AN-20.txt', 'AN-21.txt', 'AN-22.txt', 'AN-23.txt', 'AN-24.txt', 'AN-25.txt', 'AN-26.txt', 'AN-27.txt']
# Load the 20 newsgroups dataset and vectorize it using the most common word
# frequency with TF-IDF weighting (without top 5% stop words)

texts = []

listing = os.listdir(path)

for infile in ANfiles:
    url = path + infile
    # url = path + "AN-raw.txt"
    f = open(url)
    raw = f.read()

    f.close()

    #tokens = nltk.word_tokenize(raw)
    #text = nltk.Text(tokens)
    texts.append(raw)


t0 = time()
#print("Loading dataset and extracting TF-IDF features...")
#dataset = datasets.fetch_20newsgroups(shuffle=True, random_state=1)

vectorizer = text.CountVectorizer(max_df=0.95, max_features=n_features)
counts = vectorizer.fit_transform(texts)
tfidf = text.TfidfTransformer().fit_transform(counts)

nmf = decomposition.NMF(n_components=n_topics).fit(tfidf)


# Inverse the vectorizer vocabulary to be able
feature_names = vectorizer.get_feature_names()
fil = open('out.txt','w')
for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    fil.write("Topic #%d:" % topic_idx)
    print("\n ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))
    fil.write("\n ".join([feature_names[i]
                      for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()
