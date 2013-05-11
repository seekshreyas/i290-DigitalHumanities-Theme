Theme Tracking of Arabian 
--------------------------
Author: _Shreyas_

### Abstract

Applying statistical analysis to linguistic exploration of ‘Arabian Nights’ corpus.

### Introduction

We all love stories. And when it is finished, we love talking about stories. If it is a story we love, we go back to understand its characters, understand the synopsis and above all try to make sense of it all. We try to understand the underlying themes and concepts behind a story. This was my area of enquiry in this project, i.e. to understand the underlying themes of my corpus.

The literary text chosen for my enquiry was ‘One Thousand and One Nights’ also called ‘The Arabian Nights’. I chose an abridged version of the Gutenberg release of Arabian Nights [1], which had a collection of 27 stories (a full list of contents can be viewed from the notes)[a].

Although, these were separate stories loosely linked to each other, I wanted to apply computational techniques to fine overarching themes within the corpus, like those of emotions.


### Analysis
Before starting text analysis, the corpus was preprocessed as:
removed the publisher information
author metadata (like author information, preface etc)
the entire corpus was split into separate files for each story, so each analysis could be done separately on each story.

### Surface Analysis

I started off with an initial surface analysis of the text using the Voyeur’s Voyant Tool. The word feature chosen was frequency of the words (text had only been normalized to lowercase)

My initial line of enquiry was around certain themes like those of ‘power’. My initial enquiry for ‘power’ was around frequencies of words like ‘faith’, ‘destiny’ etc, whose results did not prove that definitive to draw an analysis on themes. Intuitively, it might have been because these words were not that frequent within the text to draw a conclusion from number of their instances. 

Then, I refined my line of enquiry to looking at the possessive forms of the pronouns, based on my intuition that the possessiveness as a feature can give a better understanding of how a theme of power is distributed within a context. For these I looked into pronouns (like ‘he’, ‘she’, ‘me’) and their possessive forms (‘his’, ‘her’, ‘mine’) respectively.




As per the figures it was observed that the frequency of occurrence of ‘he’ was a lot higher than ‘me’ or ‘she’ in most of the text. This gives an indication that there is corpus is inclined more towards the male over the female, which isn’t that surprising, keeping in mind that ‘he’ could also be used to refer to God or Allah. 

Moving on to the possessive forms of the pronouns, comparative analysis between the pronouns and their possessive forms should a very different kind of variation for each of those pronouns. For ‘he’ vs ‘his’ analysis, there were a lot more instance of ‘he’ than its possessive forms whereas for words like ‘me’ vs ‘my’ and ‘she’ vs ‘her’ the words were largely very closely distributed. The variation was very close in case of ‘she’ vs ‘her’.


### Document Analysis

To get a sense of the relationship between the different stories, I wanted to cluster those documents. I chose to do it on a hierarchical clustering so I get a sense of which stories were more closely related over the other and how many different levels were there. For this the feature of each word was calculated separately, in one case as tf-idf (Term Frequency over document frequency of that term) and in another case as word frequency.

Fig(5) : Hierarchical clustering of corpus on tf-idf vector


Fig(6): Hierarchical clustering of corpus on word count vector

Overall, both of those clusters broadly come together at the end, indicating the last few stories are a lot more related to each other. This gives a semblance of a feeling that maybe the stories are coming together at the end.


### Word Context Analysis

A number of approaches were tried to get a context of the word like LDA, NMF, LSA. I finally chose to use NodeBox Linguistics Library, that bundles WordNet (using Oliver Steele's PyWordNet), NLTK, Damian Conway's pluralisation rules, Bermi Ferrer's singularization rules, Jason Wiener's Brill tagger, several algorithms adopted from Michael Granger's Ruby Linguistics module, John Wiseman's implementation of the Regressive Imagery Dictionary, Charles K. Ogden's list of basic English words, and Peter Norvig's spelling corrector[2].

For ascertaining the context of the word Regressive Imagery Dictionary approach was adopted using NodeBox. NodeBox English Linguistics[3] is able to do psychological content analysis using John Wiseman's Python implementation of the Regressive Imagery Dictionary. The RID asigns scores to primary, secondary and emotional process thoughts in a text.

Primary: free-form associative thinking involved in dreams and fantasy
Secondary: logical, reality-based and focused on problem solving
Emotions: expressions of fear, sadness, hate, affection, etc.

For my research purposes, I chose to understand the different emotions from a psychological content analysis point.  As per the algorithm, each word can be categorized on 6 primary categories based on emotions and they are : affection, glory, anxiety, sadness, expressive behavior, positive affect & aggression. 

To get a perspective, the relative categories of the words i.e. Primary, Secondary and Emotional was also calculated for each story.

Also, for each text I used the Nodebox text summarization API for getting keywords for each text. 


### Key Findings

Fig 7: The relative frequencies of words based on whether they belonged to Primary Category, Secondary Category or Emotions Category on the Regressive Imagery Dictionary score

Fig 8: The normalized frequency of ‘affection’ and ‘aggression’ words in emotions


Fig 9: The normalized frequency of ‘anxiety’ and ‘expressive behavior’ words in emotions category

Fig 10: The normalized frequency of ‘positive affect’ and ‘sadness’ words in emotions category

Above shows plots of normalized frequency plots of words in different emotion categories. 

Fig7 shows us that the relative distribution of words in the emotions category remains in the a certain range band. Fig 8: shows a normalized distribution of words that depict ‘affection’ and ‘aggression’, which depicts an interesting insight. The initial stories have a lot more aggression than affection, whereas as we get to the end it starts coming together and while in the last story the affection is more than aggression. Fig 9 shows a distribution of ‘anxiety’ related words and ‘expressive behavior’ related words. Overall, their disribution remains close to each other, but broadly is lower at the end than at the beginning. Fig10 shows a distribution of ‘positive affect’ words and ‘sadness’. Again overall, they stay quite close to each other. 

So a revealing insight was the changeover of the affection and aggression words. Close reading those texts also indicates an increased feeling forgiveness and affection. 

So, overall on a theme ‘affection’ vs ‘aggression’ there is a marked increase in relative terms over the chosen corpus

### Conclusion

The above shows an indication of a theme and its progress, but I do maintain that it is inconclusive. These findings can augment an intuitive understanding of the corpus by leading the user to look at it in different light, but are by no means a replacement to close reading understanding of the text.

### Future Work
This was just my very basic exploration of a chosen corpus statistically in the context of linguistics. The very first follow up work could be applying the same analysis to the entire ‘Thousand and One Nights’ corpus of thousand stories, to gather whether the same model holds true in the overall text. 


### Notes
- [a]: List of Stories in the Corpus

### Bibliography
- [1]: “The Arabian Nights Entertainments” by Andrew Lang (Gutenberg, 2008)
- [2]: Nodebox Linguistics Library
- [3]: Nodebox Linguistics Library, psychological content analysis by Regressive Imagery Dictionary

