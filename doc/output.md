# Theme Detection 

## Prelimininary Quant Study Output


#### AN-raw.txt Stats

- total words (with repeats) length:
	- 602982
- total vocab (no repeats - including punctuation):	
	- 73
- lexical richness (i.e. total/vocab):	
	- 8260.02739726
- top 50 words (without stemming/ lemmatizing):
	- [',', 'the', 'and', 'to', 'of', 'i', "''", 'a', 'he', 'that', 'was', 'in', 'you', 'his', 'my', 'had', 'it', 'with', 'as', '``', 'for', 'her', 'me', 'but', 'at', 'him', 'not', 'she', 'on', 'this', 'which', 'have', 'be', 'by', 'all', 'so', 'when', 'they', 'is', 'who', 'said', 'will', 'your', 'one', 'from', 'we', 'what', 'then', 'were', 'no'] 

- words (showing only 10) that occur once (hapaxes):
	- ["'m", "'madam", "'my", "'this", "'we", '1,000', '3', '`all', '`behold', '`why', 'a-fishing', 'a-hunting', 'a-hunting.', 'abate.', 'abating', 'abdicating', 'abduction.', 'ablest', 'abode', 'abounded', 'abounding', 'abroad.', 'absurdities', 'absurdity', 'abundance', 'abundance.', 'abused', 'abusing', 'access', 'accession', 'accident.', 'acclamations', 'accompaniment.', 'accompanying', 'accomplish', 'accomplished.', 'accomplishment', 'accomplishments', 'accordingly.', 'accuses', 'accusing', 'acquainted.', 'acquire.', 'acquired', 'acting', 'actions', 'active', 'acute', 'adam', 'added.'] 

###### after removing stopwords 
	content words (without stopwords but repeat): 	63202
	content percentage: 	0.1
	~~~~~ after stemming ~~~~~~
	word count for: 		power 	: 30
	word percentage for: 		power 	: 0.0 

	word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		power 	: 24
	word percentage for: 		power 	: 0.02 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		power 	: 24
	word percentage for: 		power 	: 0.04 

	~~~~~~~~~~~
	word count for: 		faith 	: 17
	word percentage for: 		faith 	: 0.0 

	word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		faith 	: 30
	word percentage for: 		faith 	: 0.01 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		faith 	: 30
	word percentage for: 		faith 	: 0.05 

	~~~~~~~~~~~
	word count for: 		poor 	: 33
	word percentage for: 		poor 	: 0.01 

	word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		poor 	: 30
	word percentage for: 		poor 	: 0.05 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		poor 	: 30
	word percentage for: 		poor 	: 0.05 

	~~~~~~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~~~~~~~
---


## AN-1.txt Stats

- total words (with repeats) length: 			
	- 7492
- total vocab (no repeats - including punctuation):	
	- 60
- lexical richness (i.e. total/vocab):	
	- 124.866666667
- top 50 words (without stemming/ lemmatizing):
	- [',', 'the', 'to', "''", 'and', 'her', 'of', 'i', 'you', 'that', 'was', 'a', '``', 'he', 'in', 'his', 'it', 'me', 'your', 'as', 'father', 'grand-vizir', 'have', 'him', 'my', 'scheherazade', 'had', 'if', 'sultan', 'this', 'with', '?', 'sister', 'be', 'for', 'so', 'who', 'but', 'is', 'not', 'said', 'shall', 'she', 'what', 'before', 'one', 'will', "'s", 'dinarzade', 'do'] 
- words (showing only 10) that occur once (hapaxes):
	- ["'", "'my", '.', 'about', 'absolutely', 'accidentally', 'accomplish', 'addressed', 'affair.', 'affection', 'afraid', 'again', 'ah', 'air', 'alive.', 'allow', 'allowed', 'allowing', 'almost', 'also', 'amazed', 'ancient', 'anguish', 'another', 'answer', 'answered.', 'arabian', 'arrived', 'arts', 'asks', 'astonishment.', 'attend', 'awaits', 'awful', 'awoke', 'back.', 'bad', 'bade', 'barbarous', 'bear', 'beautiful', 'beauty', 'beauty.', 'began', 'begged', 'begin', 'behaviour', 'besides', 'better.', 'beyond'] 

##### after removing stopwords ~~~~~~
	content words (without stopwords but repeat): 	810
	content percentage: 	0.11
	~~~~~ after stemming ~~~~~~
	word count for: 		power 	: 1
	word percentage for: 		power 	: 0.01 

	word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		power 	: 1
	word percentage for: 		power 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		power 	: 1
	word percentage for: 		power 	: 0.12 

	~~~~~~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	~~~~~~~~~~~
	word count for: 		poor 	: 1
	word percentage for: 		poor 	: 0.01 

	word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		poor 	: 1
	word percentage for: 		poor 	: 0.12 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		poor 	: 1
	word percentage for: 		poor 	: 0.12 

	~~~~~~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~~~~~~~
---



## AN-2.txt Stats

- total words (with repeats) length: 			8060
- total vocab (no repeats - including punctuation):	57
- lexical richness (i.e. total/vocab):	141.403508772
- top 50 words (without stemming/ lemmatizing):
	- [',', 'the', "''", 'and', 'to', 'he', 'you', 'i', 'his', 'a', 'of', '``', 'was', 'merchant', 'genius', 'in', 'said', 'with', 'him', 'that', 'this', 'have', 'my', 'when', 'at', 'had', 'on', 'so', 'as', 'killed', 'old', 'they', 'man', 'not', '?', 'but', 'by', 'day', 'kill', 'me', 'them', 'what', 'it', 'son', 'story', 'then', 'time', 'will', 'would', 'your'] 

- words (showing only 10) that occur once (hapaxes):
	- ['.', ':', 'adventure', 'affair.', 'affairs', 'affairs.', 'afraid', 'after', 'agree', 'ah', 'allow', 'alms', 'also', 'anxiety.', 'any', 'appointed.', 'approached', 'arise', 'arrange', 'arrived.', 'astonishment.', 'attend', 'avert', 'awaited', 'awake', 'away.', 'back.', 'beautiful', 'because', 'been', 'before', 'beg', 'being', 'bewailed', 'bid', 'biscuits', 'biscuits.', 'bitterly', 'black', 'branch', 'broke', 'brother', 'brought', 'business', 'certainly', 'children.', 'clear', 'cloud', 'coming', 'command'] 

##### after removing stopwords ~~~~~~
	content words (without stopwords but repeat): 	919
	content percentage: 	0.11
	~~~~~ after stemming ~~~~~~
	word count for: 		power 	: 0
	word percentage for: 		power 	: 0.0 

	word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		power 	: 0
	word percentage for: 		power 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		power 	: 0
	word percentage for: 		power 	: 0.0 

	~~~~~~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	~~~~~~~~~~~
	word count for: 		poor 	: 1
	word percentage for: 		poor 	: 0.01 

	word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		poor 	: 0
	word percentage for: 		poor 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		poor 	: 0
	word percentage for: 		poor 	: 0.0 

	~~~~~~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~~~~~~~
---



#### AN-3.txt Stats

- total words (with repeats) length: 			
	- 6114
- total vocab (no repeats - including punctuation):	
	- 54
- lexical richness (i.e. total/vocab):	
	- 113.222222222
- top 50 words (without stemming/ lemmatizing):
	- [',', 'i', 'to', 'the', "''", 'and', 'my', 'of', 'a', 'she', 'her', 'you', '``', 'this', 'that', 'was', 'it', 'him', 'me', 'in', 'son', 'have', 'not', 'steward', 'will', 'calf', 'is', 'with', 'as', 'but', 'he', 'said', 'which', 'wife', 'at', 'when', "'s", 'am', 'had', 'man', 'old', 'then', 'who', ';', 'his', 'into', 'on', 'slave', 'story', 'take'] 

- words (showing only 10) that occur once (hapaxes):
	- ['(', ')', 'absence', 'action', 'afterwards', 'agreement', 'alive', 'ample', 'an', 'animal', 'another.', 'any', 'appeared', 'astonishing', 'astonishment.', 'attend.', 'avail.', 'away.', 'bairam', 'became', 'because', 'become', 'begged', 'begin', 'best', 'black', 'bones', 'bought.', 'bound', 'break', 'by', 'came', 'came.', 'caresses.', 'carry', 'celebrate', 'change', 'changes', 'child.', 'children', 'compassion', 'concealed', 'condition', 'conditions.', 'confide', 'consented', 'continued', 'cord', 'cried', 'cried.'] 

##### after removing stopwords ~~~~~~
	content words (without stopwords but repeat): 	668
	content percentage: 	0.11
	~~~~~ after stemming ~~~~~~
	word count for: 		power 	: 0
	word percentage for: 		power 	: 0.0 

	word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		power 	: 0
	word percentage for: 		power 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		power 	: 0
	word percentage for: 		power 	: 0.0 

	~~~~~~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		faith 	: 0
	word percentage for: 		faith 	: 0.0 

	~~~~~~~~~~~
	word count for: 		poor 	: 0
	word percentage for: 		poor 	: 0.0 

	word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		poor 	: 0
	word percentage for: 		poor 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		poor 	: 0
	word percentage for: 		poor 	: 0.0 

	~~~~~~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

	~~~~~ after removing stopwords ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~ after Porter stemming ~~~~~~
	word count for: 		loyal 	: 0
	word percentage for: 		loyal 	: 0.0 

	~~~~~~~~~~~
---



*************** AN-4.txt Stats ***************

total words (with repeats) length: 			6066
total vocab (no repeats - including punctuation):	55
lexical richness (i.e. total/vocab):	110.290909091
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'i', 'and', 'to', 'my', 'of', 'a', "''", 'me', 'you', 'he', 'we', 'but', 'had', 'not', 'that', 'with', 'his', 'in', 'was', 'him', '``', 'two', 'at', 'for', 'her', 'it', 'she', 'they', 'all', 'so', 'thousand', 'as', 'came', 'did', 'do', 'have', 'on', 'this', 'up', 'when', 'brother', 'dogs', 'genius', 'merchant', 'one', 'set', 'then', 'third'] 

words (showing only 10) that occur once (hapaxes):
['!', "'", '.', ':', 'about', 'accepted', 'accounts', 'added', 'afterwards', 'afterwards.', 'against', 'also', 'an', 'angry', 'answered', 'appeased', 'arrived', 'asked', 'attention', 'away', 'back', 'bath', 'became', 'befallen', 'before.', 'beggar', 'board.', 'both', 'brought', 'buried', 'buried.', 'business', 'buy', 'capital', 'caravan', 'care', 'children', 'closely', 'come', 'company.', 'compare', 'condemned', 'congratulations', 'consented.', 'corner', 'countries', 'country', 'dawned', 'days', 'died'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	613
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.02 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-5.txt Stats ***************

total words (with repeats) length: 			6440
total vocab (no repeats - including punctuation):	54
lexical richness (i.e. total/vocab):	119.259259259
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'he', "''", 'i', 'and', 'to', 'a', 'you', 'of', 'in', 'that', '``', 'but', 'it', 'me', 'fisherman', 'was', 'his', 'will', 'genius', ';', 'not', 'which', 'as', 'at', 'had', 'him', 'if', 'out', 'said', 'so', 'with', 'would', '?', 'have', 'nets', 'vase', 'choose', 'could', 'my', 'then', 'what', '!', 'came', 'fish', 'great', 'no', 'on', 'only'] 

words (showing only 10) that occur once (hapaxes):
['.', 'afraid', 'afterwards', 'alas', 'allow', 'almost', 'already', 'always', 'angry', 'annoyed.', 'answering', 'any', 'appeared', 'ask', 'asked', 'astonishment.', 'attentively', 'bad', 'bank', 'basket', 'became', 'because', 'being', 'better', 'body', 'broken', 'build', 'buy', 'came.', 'captive', 'captivity', 'cast', 'caught', 'caused', 'certain', 'change', 'children.', 'civilly', 'clean', 'clouds', 'collecting', 'come', 'coming', 'conjure', 'contain', 'copper', 'courage.', 'cunning.', 'deal', 'delighted.'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	707
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.03 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.28 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.28 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-6.txt Stats ***************

total words (with repeats) length: 			3690
total vocab (no repeats - including punctuation):	53
lexical richness (i.e. total/vocab):	69.6226415094
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'he', 'and', "''", 'a', 'him', 'king', 'his', 'that', 'of', 'you', 'in', 'physician', 'this', '``', 'i', 'is', 'had', 'it', 'said', 'with', 'your', 'was', 'when', 'cure', 'not', 'went', 'what', 'all', 'do', 'if', 'king.', 'made', 'sire', 'told', 'very', 'vizir', 'will', 'ball', 'been', 'by', 'club', 'day', 'greek', 'him.', 'most', 'were', 'who'] 

words (showing only 10) that occur once (hapaxes):
['.', ';', 'able', 'accordingly', 'after', 'am', 'answered', 'any', 'application.', 'approached', 'arose', 'assassinate', 'astonishment', 'at', 'audience-chamber', 'avaricious', 'awake', 'bad', 'bat', 'bath', 'bathe', 'before', 'beg', 'believe', 'best', 'body', 'body.', 'bowed', 'bring', 'called', 'came', 'can', 'cease', 'come', 'communication', 'completely', 'condescension', 'confide', 'continued', 'country', 'court.', 'curiosity', 'dangerous', 'deal', 'death.', 'descendants', 'determined', 'doctors', 'drug', 'eager'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	388
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.05 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.52 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-7.txt Stats ***************

total words (with repeats) length: 			2581
total vocab (no repeats - including punctuation):	52
lexical richness (i.e. total/vocab):	49.6346153846
top 50 words (without stemming/ lemmatizing):
['the', ',', 'to', 'he', 'of', 'and', 'a', 'it', "''", 'had', 'parrot', 'was', '``', 'i', 'that', 'her', 'vizir', 'when', 'husband', 'in', 'but', 'cage', 'him', 'his', 'not', 'on', 'so', 'what', 'all', 'asked', 'day', 'did', 'for', 'from', 'if', 'is', 'king', 'me', 'night', 'one', 'she', 'take', 'this', 'told', 'you', 'as', 'away', 'been', 'bird', 'by'] 

words (showing only 10) that occur once (hapaxes):
["'s", '.', ';', '?', 'above', 'absence', 'added', 'afterwards', 'am', 'another', 'answered', 'are', 'assassinate', 'away.', 'back', 'be', 'beautiful', 'before', 'better', 'birds', 'bought', 'brought', 'business', 'came', 'can', 'candle.', 'case', 'convinced', 'death', 'departed.', 'deserve', 'determined.', 'disclose', 'disturbed', 'do', 'douban', 'down', 'during', 'eyes', 'finished', 'fisherman', 'found', 'front', 'genius', 'gift', 'go', 'great', 'ground', 'guilty.', 'hand-mill'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	272
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-8.txt Stats ***************

total words (with repeats) length: 			17432
total vocab (no repeats - including punctuation):	61
lexical richness (i.e. total/vocab):	285.770491803
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'to', 'he', "''", 'of', 'his', 'a', 'you', 'was', '``', 'in', 'i', 'had', 'them', 'that', 'on', 'said', 'as', 'fish', 'not', 'she', 'it', 'who', 'your', 'him', 'sultan', 'when', 'at', 'fisherman', 'king', 'will', 'do', 'for', 'my', 'then', 'this', 'which', 'with', 'but', 'have', 'if', 'am', 'be', 'did', 'four', 'one', '?', 'are'] 

words (showing only 10) that occur once (hapaxes):
['.', 'accident', 'account', 'added', 'addressed', 'advice', 'afraid', 'afraid.', 'alas', 'allowed', 'almost', 'alone', 'aloud', 'already', 'answering', 'anxiety.', 'applies', 'approached', 'arrived', 'ashes', 'ask', 'asleep', 'assassin.', 'assembled', 'astonished', 'astonished.', 'astonishment.', 'astounded', 'ateca', 'ateca.', 'bad', 'beautiful.', 'beautifully-painted', 'because', 'become', 'before', 'before.', 'beheld', 'bemoaned', 'bent', 'birds', 'bitterly.', 'block', 'blue', 'book.', 'books', 'bowed', 'bracelets', 'break', 'building'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	1918
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.05 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.05 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-9.txt Stats ***************

total words (with repeats) length: 			5779
total vocab (no repeats - including punctuation):	57
lexical richness (i.e. total/vocab):	101.385964912
top 50 words (without stemming/ lemmatizing):
['the', ',', "''", 'and', 'to', 'i', 'she', 'of', 'he', 'you', 'sultan', '``', 'a', 'said', 'his', 'him', 'in', 'then', 'was', 'for', 'it', 'king', 'is', 'me', 'my', 'where', 'as', 'that', 'her', 'this', 'will', 'young', '?', 'at', 'but', 'slave', 'so', 'went', 'with', 'are', 'black', 'day', 'enchantress', 'had', 'not', 'now', 'once', 'over', 'prince', 'were'] 

words (showing only 10) that occur once (hapaxes):
['.', 'about', 'about.', 'accompany', 'add', 'adopt', 'affection', 'afternoon', 'again', 'again.', 'agreed', 'alive', 'alive.', 'all.', 'although', 'am', 'an', 'arose', 'asleep', 'assembled', 'astonished', 'avenge', 'beat', 'beaten', 'beats', 'beautiful', 'because', 'been', 'befallen', 'being', 'believe', 'best', 'bewailed', 'blow', 'blows.', 'body', 'boil', 'bring', 'buffalo', 'build', 'burst', 'called', 'cause', 'cease', 'changes', 'city', 'colours', 'comes', 'consulted', 'country'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	632
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-10.txt Stats ***************

total words (with repeats) length: 			19958
total vocab (no repeats - including punctuation):	62
lexical richness (i.e. total/vocab):	321.903225806
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'to', "''", 'of', 'a', 'you', 'was', 'she', 'he', 'in', '``', 'that', 'at', 'his', 'had', 'her', 'with', 'all', 'zobeida', 'but', 'it', 'their', 'they', 'who', 'porter', 'i', 'not', 'as', 'by', 'have', 'were', 'on', 'we', 'which', 'be', 'for', 'from', 'my', 'said', 'then', "'s", 'him', 'if', 'is', 'me', 'this', 'when', 'calenders'] 

words (showing only 10) that occur once (hapaxes):
["'", '.', 'accompaniment.', 'according', 'accustomed', 'across', 'addressed', 'admiring', 'admittance', 'admitting', 'adventure', 'advice', 'advice.', 'affairs', 'affront', 'again', 'again.', 'agreed', 'air', 'air.', 'allow', 'almost', 'although', 'amazement', 'amber', 'amina.', 'amused', 'amusement', 'amusement.', 'angrily', 'answer', 'answer.', 'anxiously', 'anybody.', 'apparently', 'appearance', 'appetites', 'apples', 'apricots', 'ardour', 'armed', 'aside', 'asleep', 'assurances', 'astonished', 'astonishment', 'astonishment.', 'attention', 'away.', 'bade'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	2144
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.01 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.05 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.05 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.05 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.05 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-11.txt Stats ***************

total words (with repeats) length: 			10926
total vocab (no repeats - including punctuation):	60
lexical richness (i.e. total/vocab):	182.1
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'i', 'and', 'of', 'a', 'my', 'he', 'was', 'had', 'in', "''", 'me', 'at', 'that', 'you', 'it', 'but', 'not', 'we', 'as', 'by', '``', 'his', 'this', 'when', 'with', 'for', 'which', 'on', 'be', 'no', 'did', 'prince', 'said', 'could', 'him', 'lady', 'one', 'son', 'uncle', 'us', 'all', 'calender', 'do', 'have', 'once', 'so', 'then'] 

words (showing only 10) that occur once (hapaxes):
['!', '.', ':', '?', 'abandon', 'able', 'absence', 'absent', 'accident.', 'accompanied', 'accordingly', 'act', 'adventure', 'again', 'age', 'alarmed', 'alike', 'alone', 'also', 'amused', 'anger', 'anger.', 'answer', 'ante-room', 'anxiety', 'anyone', 'anything', 'anything.', 'apologies', 'appear', 'appeared', 'approach', 'army', 'army.', 'arrest.', 'arrival', 'arrive', 'ask', 'asking', 'avoided', 'aware', 'bag', 'barely', 'beard', 'beautiful', 'beauty', 'became', 'become', 'bed.', 'before.'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	1139
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 3
word percentage for: 		power 	: 0.03 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.09 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.18 

~~~~~~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.01 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.09 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-12.txt Stats ***************

total words (with repeats) length: 			23941
total vocab (no repeats - including punctuation):	62
lexical richness (i.e. total/vocab):	386.14516129
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'of', 'to', "''", 'a', 'i', 'he', 'was', 'his', 'in', 'that', '``', 'had', 'as', 'but', 'it', 'my', 'me', 'you', 'him', 'on', 'sultan', 'who', 'with', 'by', 'not', 'her', 'she', 'this', 'into', 'is', 'man', 'they', 'all', 'at', 'princess', 'for', 'when', 'which', 'from', 'one', 'no', 'so', 'were', 'said', 'then', 'have', 'could'] 

words (showing only 10) that occur once (hapaxes):
['(', ')', '.', 'able', 'abroad', 'accompanied', 'accompany', 'accomplished', 'accord', 'accursed', 'across', 'action', 'added', 'adopt', 'advanced', 'against', 'aimlessly', 'alarm', 'alive', 'almost', 'along', 'amidst', 'anchor', 'another.', 'anxiety', 'anyone', 'ape', 'appear', 'appearance', 'appeared', 'apply', 'approach', 'approached', 'arab', 'arabs', 'arm', 'arranged', 'arrow', 'ashes.', 'aside', 'assume', 'assumed', 'astonishment', 'attack', 'attendants', 'attendants.', 'attending', 'attention', 'attracted', 'audience'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	2498
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.01 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.04 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.08 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.04 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.04 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-13.txt Stats ***************

total words (with repeats) length: 			15248
total vocab (no repeats - including punctuation):	61
lexical richness (i.e. total/vocab):	249.967213115
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'i', 'and', 'to', "''", 'a', 'of', 'my', 'you', 'in', 'was', '``', 'me', 'as', 'with', 'that', 'for', 'had', 'but', 'his', 'is', 'he', 'this', 'who', 'genius', 'at', 'have', 'she', 'by', 'her', ';', '?', 'it', 'said', 'not', 'when', 'which', 'all', 'an', 'on', 'princess', 'will', 'your', 'do', 'man', 'up', 'only', 'we', 'were'] 

words (showing only 10) that occur once (hapaxes):
['.', 'abandon', 'ablest', 'above', 'absence', 'accident', 'accordingly', 'account', 'accustomed', 'act', 'added', 'addressing', 'adopt', 'adventure', 'advised', 'after', 'against', 'age', 'aid', 'all.', 'allow', 'angrily', 'anxiety', 'anxious', 'anything', 'arabic', 'arm', 'arrived', 'ask', 'ass', 'ate', 'attacked', 'attended', 'audacity', 'awful', 'baby', 'badness', 'band', 'barely', 'basis', 'bath', 'beast', 'befitting', 'began', 'begged', 'beheld', 'behind', 'being', 'beings', 'believe'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	1664
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 3
word percentage for: 		power 	: 0.02 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.06 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.12 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.12 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.12 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-14.txt Stats ***************

total words (with repeats) length: 			25791
total vocab (no repeats - including punctuation):	64
lexical richness (i.e. total/vocab):	402.984375
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'i', 'to', 'of', 'a', 'that', 'in', 'my', 'me', 'was', 'had', 'as', 'with', 'it', 'he', 'on', 'you', 'for', 'but', 'which', 'they', 'we', 'be', "''", 'at', 'this', 'when', 'all', 'his', 'so', 'not', 'one', 'out', '``', 'have', 'then', 'were', 'by', 'him', 'into', 'man', 'myself', 'from', 'is', 'up', 'no', 'will', 'young'] 

words (showing only 10) that occur once (hapaxes):
["'", '.', '`why', 'able', 'above', 'absence', 'absence.', 'absent.', 'absurdity', 'accepted', 'accident', 'accordingly', 'account.', 'across', 'actions', 'actually', 'addressing', 'adventures.', 'afresh', 'ago', 'alas', 'alighted', 'alive.', 'all.', 'aloes', 'aloud', 'already', 'also', 'alternately', 'always', 'ambergris', 'amuse', 'amused', 'anemones', 'answer', 'arguing', 'arisen', 'arose', 'around', 'arrived', 'arrows.', 'art', 'ashes', 'ashore', 'asked', 'asking', 'asleep', 'assure', 'astern.', 'asunder'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	2688
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-15.txt Stats ***************

total words (with repeats) length: 			87524
total vocab (no repeats - including punctuation):	68
lexical richness (i.e. total/vocab):	1287.11764706
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'i', 'to', 'of', 'a', 'my', 'that', 'was', 'in', 'with', 'me', 'had', 'we', "''", 'he', 'which', 'it', 'as', 'for', 'at', 'upon', 'his', 'but', 'you', 'when', 'all', 'by', 'him', 'this', 'were', 'our', 'from', 'they', 'one', 'them', 'so', 'have', 'not', 'their', 'up', 'be', 'us', 'could', 'who', 'myself', '``', 'on', 'then'] 

words (showing only 10) that occur once (hapaxes):
["'m", "'this", '(', ')', '.', '`all', '`behold', '`the', 'a-fishing', 'abounded', 'abounding', 'about.', 'abroad', 'absence', 'absolutely', 'abundance', 'abundance.', 'abusing', 'accompanied', 'accounts', 'accustomed', 'ached', 'acquaintance', 'acquired', 'action', 'adam', 'added.', 'addressed', 'adieu', 'adjoining', 'admire', 'admiring', 'admit', 'admitted', 'adorning', 'adroitly', 'advanced', 'adventure.', 'advice', 'advised', 'affairs', 'afloat', 'agate', 'ages', 'aggrieved', 'aghast.', 'ah', 'aim', 'aiming', 'air.'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	8870
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 4
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 4
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 4
word percentage for: 		power 	: 0.05 

~~~~~~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.05 

~~~~~~~~~~~
word count for: 		poor 	: 7
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 7
word percentage for: 		poor 	: 0.08 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 7
word percentage for: 		poor 	: 0.08 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-16.txt Stats ***************

total words (with repeats) length: 			15953
total vocab (no repeats - including punctuation):	63
lexical richness (i.e. total/vocab):	253.222222222
top 50 words (without stemming/ lemmatizing):
['the', ',', 'to', 'and', 'of', 'he', 'a', 'his', 'was', "''", 'in', 'him', 'it', 'that', 'had', 'for', 'i', '``', 'who', 'at', 'hunchback', 'man', 'as', 'doctor', 'is', 'my', 'on', 'police', 'when', '!', 'chief', 'tailor', 'they', 'with', 'you', 'but', "'s", 'be', 'have', 'me', 'all', 'not', 'this', 'so', 'down', 'one', 'out', 'up', 'wife', 'by'] 

words (showing only 10) that occur once (hapaxes):
["'ll", '(', ')', '.', 'able', 'accepted', 'accidentally', 'accordingly', 'accusing', 'added', 'advance', 'affair', 'again', 'again.', 'agitated', 'ago', 'aid', 'allah', 'almost', 'already.', 'although', 'altogether', 'among', 'amused', 'another', 'answered', 'antics', 'appeared', 'arm.', 'armpits', 'arms', 'arrested', 'arrived', 'ass', 'assassin.', 'astonished', 'astonishment', 'attacked', 'attend', 'audience', 'author', 'bad', 'barber', 'bath.', 'bear', 'beating', 'beautiful', 'become', 'bed', 'bed-room'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	1631
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.06 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.06 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-17.txt Stats ***************

total words (with repeats) length: 			19509
total vocab (no repeats - including punctuation):	62
lexical richness (i.e. total/vocab):	314.661290323
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'and', 'of', 'he', 'a', 'i', 'his', 'my', "''", 'her', 'she', 'was', 'will', 'in', 'had', 'him', 'that', 'with', 'you', 'on', 'shall', '``', 'at', 'for', 'as', 'me', 'have', 'it', 'all', 'brother', 'by', 'be', 'but', 'when', 'which', 'not', 'this', 'into', 'old', 'so', 'alnaschar', 'from', 'who', 'woman', 'house', 'out', 'give', 'hundred'] 

words (showing only 10) that occur once (hapaxes):
["'madam", "'we", '--', '.', '3', 'abominable', 'about', 'accident', 'accompanied', 'actually', 'acute', 'admiration', 'adorable', 'adventure', 'adventures', 'age', 'agony', 'almost', 'alms', 'along.', 'although', 'always', 'among', 'amongst', 'amuse', 'anger', 'anxious', 'apartments', 'apparently', 'appeared', 'approach', 'approaching', 'around', 'arrested', 'arrived', 'ascend', 'ashamed', 'assassins', 'assume', 'attendant', 'attitude', 'attitude.', 'avenged', 'bade', 'band', 'beard', 'bearer.', 'bearing', 'beauty', 'begged'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	2017
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.01 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.05 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.05 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-18.txt Stats ***************

total words (with repeats) length: 			11153
total vocab (no repeats - including punctuation):	61
lexical richness (i.e. total/vocab):	182.836065574
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'and', "''", 'of', 'he', 'that', 'a', 'his', 'i', 'my', 'as', 'it', 'in', 'was', 'you', '``', 'him', 'had', 'this', 'with', 'for', 'brother', 'at', 'on', 'barmecide', 'be', 'but', 'man', 'all', 'so', 'barber', 'which', 'who', '?', 'by', 'have', 'is', 'when', 'from', 'we', 'were', 'been', 'before', 'himself', 'they', ';', 'hunchback', 'me'] 

words (showing only 10) that occur once (hapaxes):
["'", '.', '`the', 'abandon', 'abandoned', 'about', 'access', 'accused', 'across', 'admire', 'affairs.', 'afternoon', 'age.', 'air', 'allow', 'alms.', 'although', 'amuse', 'angry', 'anything', 'apartments', 'apologised', 'apparently', 'appearance', 'appeared', 'appetite.', 'archives', 'associated', 'astonishment', 'attacked', 'attentively.', 'back.', 'backwards', 'balsam.', 'barmecides', 'barren', 'beard', 'beat', 'became', 'bedouin', 'bedouins', 'beg.', 'beheld', 'behold', 'belong', 'belonged', 'belonged.', 'benefactor', 'beside', 'bestowed'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	1179
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

~~~~~~~~~~~
word count for: 		poor 	: 3
word percentage for: 		poor 	: 0.03 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 3
word percentage for: 		poor 	: 0.25 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 3
word percentage for: 		poor 	: 0.25 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-19.txt Stats ***************

total words (with repeats) length: 			74309
total vocab (no repeats - including punctuation):	65
lexical richness (i.e. total/vocab):	1143.21538462
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'to', 'of', "''", 'he', 'a', 'his', 'i', 'you', 'her', 'in', 'was', 'that', 'as', 'prince', 'princess', 'she', '``', 'at', 'for', 'him', 'had', 'on', 'with', 'it', 'but', 'king', 'this', 'not', 'my', 'so', 'which', 'be', 'is', 'camaralzaman', 'have', 'your', 'by', 'all', 'will', "'s", 'me', 'who', 'said', 'one', 'they', ':', 'no'] 

words (showing only 10) that occur once (hapaxes):
["'ll", '.', 'abdicating', 'abduction.', 'above', 'abroad.', 'absence.', 'absurd', 'abused', 'accident', 'accompanied', 'accompany', 'accordingly.', 'acquaintance', 'acquainted.', 'across', 'action', 'active', 'actual', 'addressed', 'adequate', 'adorable', 'advancement.', 'adventure', 'adventurer', 'advise', 'affair', 'affairs', 'affairs.', 'affectionate', 'affliction', 'again.', 'against', 'age', 'aid.', 'air.', 'alarming', 'alive', 'allegiance', 'alliance.', 'allows', 'allude', 'ally', 'alone.', 'along', 'aloud', 'also', 'alternately.', 'altogether', 'amazed'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	7720
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 8
word percentage for: 		power 	: 0.01 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 7
word percentage for: 		power 	: 0.03 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 7
word percentage for: 		power 	: 0.09 

~~~~~~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.01 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.01 

~~~~~~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-20.txt Stats ***************

total words (with repeats) length: 			42569
total vocab (no repeats - including punctuation):	69
lexical richness (i.e. total/vocab):	616.942028986
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'and', 'of', "''", 'he', 'his', 'that', 'a', 'in', 'you', 'i', 'was', 'noureddin', 'with', 'her', 'not', 'had', 'for', 'him', '``', 'at', 'it', 'but', 'as', 'they', 'on', 'said', 'persian', 'king', 'be', 'will', 'caliph', 'this', 'is', 'me', 'who', 'slave', 'your', "'s", 'she', 'beautiful', 'have', 'saouy', 'by', 'vizir', 'what', 'if', 'when'] 

words (showing only 10) that occur once (hapaxes):
['.', '1,000', 'abandoned', 'abate.', 'able', 'above', 'absence', 'absent.', 'acclamations', 'accomplished', 'accomplishment', 'accordingly', 'account', 'accounts', 'accuses', 'acquire.', 'act', 'acting', 'actually', 'added', 'adieu', 'administered', 'administration', 'admire', 'admitted.', 'advised', 'affairs', 'affection', 'affects', 'affronted', 'after-wards', 'afterwards', 'age', 'agitation', 'ago', 'agree', 'agreeable', 'aid', 'alas', 'alighted', 'alike', 'alive.', 'allah', 'amazement.', 'amidst', 'amongst', 'amuse', 'amused', 'announcement', 'announcing'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	4544
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.02 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.02 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 3
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 3
word percentage for: 		faith 	: 0.07 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.02 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.02 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-21.txt Stats ***************

total words (with repeats) length: 			29322
total vocab (no repeats - including punctuation):	61
lexical richness (i.e. total/vocab):	480.68852459
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'to', "''", 'he', 'of', 'a', 'aladdin', 'his', 'her', 'him', 'in', 'was', 'that', 'she', '``', 'for', 'had', 'it', 'i', 'but', 'with', 'you', 'sultan', 'said', 'princess', "'s", 'at', 'magician', 'on', 'not', 'who', 'as', 'so', 'what', 'palace', 'this', ':', 'mother', 'out', 'by', 'genie', 'my', 'is', 'from', 'me', 'your', '?', 'have'] 

words (showing only 10) that occur once (hapaxes):
["'", '--', '.', 'a-hunting', 'a-hunting.', 'accident', 'accomplished', 'ached', 'advice', 'agate', 'age', 'ago.', 'ailments', 'air', 'almost', 'altogether.', 'always.', 'amazed', 'amazement', 'amid', 'amiss', 'another.', 'answer.', 'appear', 'appeared.', 'appointed', 'are', 'armed', 'armies', 'arms.', 'arrayed', 'arts', 'ashes', 'asking', 'asleep', 'astonishment.', 'attend', 'audience-chamber', 'avenge', 'await', 'awakened', 'aware', 'back.', 'bandaged', 'banks', 'basket', 'bath.', 'battles', 'be.', 'bear'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	3288
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.01 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.03 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.06 

~~~~~~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.01 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.03 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.06 

~~~~~~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.06 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.06 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-22.txt Stats ***************

total words (with repeats) length: 			5490
total vocab (no repeats - including punctuation):	56
lexical richness (i.e. total/vocab):	98.0357142857
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'and', 'of', 'a', "''", 'i', 'you', 'caliph', 'that', 'his', 'he', 'him', 'for', 'have', 'in', 'your', 'at', 'it', 'my', 'which', '``', 'blind', 'man', 'on', 'they', 'was', 'as', 'be', 'but', 'by', 'had', 'is', 'so', 'with', 'all', 'back', 'me', 'then', 'this', 'what', 'highness', 'if', 'no', 'palace', 'said', 'same', 'vizir', 'when'] 

words (showing only 10) that occur once (hapaxes):
["'s", '--', '.', '?', 'able', 'about', 'act', 'action', 'adventures', 'almost', 'alms.', 'along', 'already', 'also', 'am', 'amusement', 'animal', 'any', 'apart', 'appear', 'appeared', 'appears', 'asking', 'astonished', 'atone', 'attend', 'bad', 'bade', 'bagdad', 'bank', 'been', 'beg', 'began', 'beggar', 'beggar.', 'begged', 'being', 'beseeching', 'blessing', 'blood.', 'blow.', 'boat', 'boldness', 'both', 'bow', 'bowed', 'bowing', 'bringing', 'business', 'caliph.'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	585
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 2
word percentage for: 		faith 	: 0.34 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-23.txt Stats ***************

total words (with repeats) length: 			14191
total vocab (no repeats - including punctuation):	59
lexical richness (i.e. total/vocab):	240.525423729
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'i', 'and', 'to', 'of', 'you', "''", 'my', 'that', 'a', 'it', 'as', 'was', 'dervish', 'had', 'me', 'but', '``', 'in', 'he', 'with', 'we', 'for', 'not', 'have', 'is', 'will', 'what', 'are', 'if', 'camels', 'this', 'on', 'your', 'so', 'were', 'at', 'by', 'do', 'no', 'one', 'which', 'after', 'could', 'his', 'out', 'said', 'all', 'eye'] 

words (showing only 10) that occur once (hapaxes):
["'s", '--', '.', 'accept', 'accidentally', 'accompanied', 'accustomed', 'addressed', 'again', 'ah', 'air.', 'alight', 'alms', 'also.', 'anoint', 'any', 'anybody', 'anyone', 'anything', 'appear', 'arms', 'ask.', 'away', 'back.', 'backs', 'bagdad', 'balsora.', 'beasts.', 'beautifully', 'became', 'befallen', 'before.', 'began', 'beggar', 'begged', 'behaving', 'behind.', 'behold', 'being', 'believe', 'believed', 'benefits', 'beside', 'besides', 'best', 'bestowed', 'better', 'bewail', 'beware', 'bid'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	1471
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.27 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.07 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.07 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-24.txt Stats ***************

total words (with repeats) length: 			22155
total vocab (no repeats - including punctuation):	59
lexical richness (i.e. total/vocab):	375.508474576
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'i', 'to', 'and', 'of', 'a', 'was', 'that', 'my', 'in', 'she', 'her', 'as', 'me', "''", 'you', 'at', 'had', 'not', 'it', 'but', 'have', 'with', 'for', 'he', 'on', 'your', '``', 'his', 'which', 'by', 'so', 'be', 'is', 'when', 'all', 'amina', 'into', 'this', 'no', 'one', 'who', 'would', 'did', 'from', ';', 'man', 'never', 'then'] 

words (showing only 10) that occur once (hapaxes):
['.', ':', 'absence.', 'absolutely', 'accompanied', 'accomplished', 'account', 'acquainted', 'added', 'admit', 'admitted', 'affection', 'afraid', 'ago.', 'air', 'alarm.', 'allow', 'alone', 'along', 'also', 'also.', 'altogether', 'amina.', 'among', 'amount', 'ample', 'ancestors', 'angry', 'animal', 'animals', 'answer', 'answered', 'anxious', 'anybody', 'apartments.', 'apparently', 'appear', 'appearance', 'appeared', 'approached', 'approaching', 'arose', 'art', 'ask', 'asked', 'astonished', 'astonishment', 'attachment', 'attacked', 'attention'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	2282
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.18 

~~~~~~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 0
word percentage for: 		poor 	: 0.0 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-25.txt Stats ***************

total words (with repeats) length: 			19449
total vocab (no repeats - including punctuation):	63
lexical richness (i.e. total/vocab):	308.714285714
top 50 words (without stemming/ lemmatizing):
['the', ',', 'to', 'and', 'he', "''", 'of', 'a', 'that', 'his', 'in', 'had', 'you', 'ali', 'it', 'cogia', 'was', '``', 'i', 'merchant', 'vase', 'him', 'as', 'olives', 'be', 'cadi', 'not', 'said', 'with', 'but', 'by', 'have', 'me', 'so', 'this', 'caliph', ';', 'them', 'they', 'for', 'if', 'my', 'at', 'will', 'on', 'all', 'before', 'no', 'which', 'one'] 

words (showing only 10) that occur once (hapaxes):
['.', 'accepted', 'accompany', 'actual', 'address', 'addressed', 'admit', 'advice', 'advice.', 'against', 'ago', 'ago.', 'aid', 'alarm', 'aleppo', 'allege', 'allow', 'allowed', 'almost', 'also.', 'always', 'among', 'another', 'answer', 'applause', 'appointed', 'approach', 'arm', 'arms', 'arrived', 'assure', 'assuring', 'astonished', 'astonishment', 'atone', 'attend', 'attracted', 'attractions', 'audience.', 'away.', 'awed', 'bade', 'banks', 'base', 'beautiful', 'begged', 'behind', 'betrayed', 'better.', 'between'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	2081
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 0
word percentage for: 		power 	: 0.0 

~~~~~~~~~~~
word count for: 		faith 	: 0
word percentage for: 		faith 	: 0.0 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 1
word percentage for: 		faith 	: 0.05 

~~~~~~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.01 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.1 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.1 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-26.txt Stats ***************

total words (with repeats) length: 			44908
total vocab (no repeats - including punctuation):	63
lexical richness (i.e. total/vocab):	712.825396825
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'to', 'of', 'and', 'he', 'that', 'was', 'her', 'a', 'in', "''", 'i', 'his', 'had', 'she', 'with', 'you', 'as', 'princess', 'prince', 'for', 'it', 'not', 'be', 'but', 'my', 'by', 'him', 'on', 'so', 'at', 'horse', '``', 'your', 'me', 'all', 'which', 'from', 'when', 'sultan', 'this', 'have', 'indian', "'s", 'no', 'who', 'what', 'into', 'king'] 

words (showing only 10) that occur once (hapaxes):
['(', ')', '--', '.', 'abandon', 'abating', 'able', 'abominable', 'above', 'absence.', 'absolutely', 'absurd', 'absurdities', 'accident', 'accompanied', 'accompanying', 'accomplished', 'account.', 'acquainted', 'across', 'act', 'adding', 'addressed', 'adventure', 'adventurer.', 'adventures.', 'against', 'ago', 'aid', 'alas', 'alight', 'alike', 'all.', 'alliance', 'allowing', 'aloud', 'already.', 'although', 'altogether', 'ambassador', 'amiable', 'amiable.', 'amusement', 'ancestors.', 'announced', 'announcement', 'another', 'another.', 'ante-room', 'anxiety'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	4484
content percentage: 	0.1
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 2
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.02 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.02 

~~~~~~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.01 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 3
word percentage for: 		faith 	: 0.07 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 3
word percentage for: 		faith 	: 0.07 

~~~~~~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.02 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 1
word percentage for: 		poor 	: 0.02 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---



*************** AN-27.txt Stats ***************

total words (with repeats) length: 			56920
total vocab (no repeats - including punctuation):	63
lexical richness (i.e. total/vocab):	903.492063492
top 50 words (without stemming/ lemmatizing):
[',', 'the', 'and', 'to', "''", 'of', 'that', 'you', 'a', 'i', 'in', 'he', '``', 'was', 'it', 'as', 'for', 'his', 'they', 'had', 'her', 'not', 'but', 'with', 'be', 'have', 'at', 'is', 'sultan', 'she', 'their', 'me', 'on', 'princess', 'will', 'all', 'your', 'prince', 'so', 'bird', 'by', 'my', 'were', 'this', 'what', 'from', 'them', 'who', 'said', 'one'] 

words (showing only 10) that occur once (hapaxes):
["'", '.', 'able', 'abode', 'abominable', 'abroad', 'absent', 'absent.', 'absolutely', 'accepted', 'accession', 'accompanied', 'accomplished.', 'accomplishments', 'addressing', 'admire.', 'adrift', 'advance', 'adventure.', 'advise', 'affected', 'afraid', 'again.', 'against', 'agreeable.', 'ah', 'allowed', 'aloud', 'amazed', 'amazement.', 'among', 'amused', 'angry', 'animals', 'anxiety', 'anyone', 'apartments.', 'appear', 'appointed', 'approach.', 'arm.', 'armed.', 'arms.', 'arose', 'arranged', 'arriving', 'arrow', 'arts', 'ascend.', 'ascent.'] 

~~~~~ after removing stopwords ~~~~~~
content words (without stopwords but repeat): 	6037
content percentage: 	0.11
~~~~~ after stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.0 

word Synonyms for: 		power 	[Synset('power.n.01'), Synset('power.n.02'), Synset('ability.n.02'), Synset('office.n.04'), Synset('power.n.05'), Synset('exponent.n.03'), Synset('might.n.01'), Synset('world_power.n.01'), Synset('baron.n.03'), Synset('power.v.01')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.02 

~~~~~ after Porter stemming ~~~~~~
word count for: 		power 	: 1
word percentage for: 		power 	: 0.02 

~~~~~~~~~~~
word count for: 		faith 	: 4
word percentage for: 		faith 	: 0.01 

word Synonyms for: 		faith 	[Synset('religion.n.01'), Synset('faith.n.02'), Synset('religion.n.02'), Synset('faith.n.04')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		faith 	: 3
word percentage for: 		faith 	: 0.02 

~~~~~ after Porter stemming ~~~~~~
word count for: 		faith 	: 3
word percentage for: 		faith 	: 0.05 

~~~~~~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.0 

word Synonyms for: 		poor 	[Synset('poor_people.n.01'), Synset('hapless.s.01'), Synset('poor.a.02'), Synset('poor.a.03'), Synset('poor.a.04'), Synset('inadequate.s.02'), Synset('poor.s.06')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.03 

~~~~~ after Porter stemming ~~~~~~
word count for: 		poor 	: 2
word percentage for: 		poor 	: 0.03 

~~~~~~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

word Synonyms for: 		loyal 	[Synset('loyal.a.01'), Synset('patriotic.a.01'), Synset('firm.s.10')] 

~~~~~ after removing stopwords ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~ after Porter stemming ~~~~~~
word count for: 		loyal 	: 0
word percentage for: 		loyal 	: 0.0 

~~~~~~~~~~~
---