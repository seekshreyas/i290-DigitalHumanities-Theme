Info290 Digital Humanities Project Proposal by Shreyas
-----

We all love stories. And when it is finished, we love talking about stories. If it is a story we love, we go back to understand its characters, understand the synopsis and above all try to make sense of it all. We try to understand the underlying themes and concepts behind a story. This is my area of enquiry in this project.

I want to track an over-arching theme in a literary text. The keyword is ‘track’. My initial premise is that I do not wish to ‘discover’ themes in my analysis. For this I would like to rely on human coding to identify a theme. But once identified, the theme would then have to be operationalized into measurable variables, because I wish to rely on quantitative analysis for  my research. Once operationalized I wish to ‘track’ the presence and progress of the theme within the literary text.

The literary text chosen for my enquiry is ‘One Thousand and One Nights’ also called ‘The Arabian Nights’. My reasons for choosing this text are:

Although, Arabian Nights is a name given to a collection of stories or tales, some of which are albeit famous tales, the collection itself has greater recognition than the actual tales. Such a significant symbolic presence of the collection with respect to its constituent tales underlines the presence of an overarching relationship and a theme within the stories.
The text is ancient, and perhaps there are multiple versions or interpretations in circulation today. A theme tracker developed on one version can then potentially be applied to those other interpretations to have theme based analysis and see what are the themes that have survived through the ages or the most prominent of the themes when comparing all the interpretations of the same text. I will state here though, that comparing multiple versions of Arabian Nights is beyond the scope of this project, but could very well be one of the applications.
I have grown up on these tales. I love them and am familiar with them. As we have seen in papers in the earlier weeks, cognitive understanding could be vital in the application of tools for digital humanities.
What would be such themes, that I might track?

Themes like __power__, __faith__, __destiny__ etc. I want to apply my process for multiple themes.

### Challenges with using Arabian Nights as text:

The first and obvious one is that I would be working on a translation and not the original text and it could be argued that this being a derived work may not be a true representation of the original work. I acknowledge that, and hence my research enquiry is based called Theme Tracking in Literary Text with Arabian Nights being my chosen dataset to demonstrate my research method, not to lay assertive critical claims. Hopefully the techniques developed would be independent enough to be enable them to be applied to other similar datasets.
Being in literature, we are dealing with unstructured text.

We would have none or little metadata.

Although, in a certain respect, using a literature based dataset could be advantageous where my text is going to be well written and adhering to a conformity, unlike something like a twitter feed where people may express the same thing in very different and non-conforming ways.

 

### Current Research

- Relevance Feedback i.e. once the theme is operationalized and a statistical model has been created, We can then give a feedback on relevance of those findings based on our close-reading to take advantage of recognition over recall.
[“Finding Literary Themes with Relevance Feedback” (Hearst & Muralidharan, 2012)]

- Motifs in The Arabian Nights and in Ancient and Medieval European Literature: A Comparison [Christa A. Tuczay]. This may not be very relevant because it concerns with concrete symbolic representations whereas I may be looking for more subtle themes.
Association Rules could be used to general ‘topic maps’ to generate insights from text-mining activities [Visual text mining using association rules (A.A. Lopes, , R. Pinho , F.V. Paulovich , R. Minghim) ]
Technology

Store multiple versions of source files as plain text flat files or in NoSQL databases like MongoDB. I am still debating this internally. Performing operations on database with these many dimensions (like no of words) could be expensive operations. But in certain cases could be advantageous as well because it might bring some sort of structure to unstructured text. Otherwise I might have to store diff versions of the same flat file raw, stemmed or lemmatized etc
NLP techniques to break down my unstructured documents to quantifiable values. I may also explore not just the text, but dialogues between characters to assert the themes, where NLP could be useful.
In the first initial phase I am more inclined towards clustering approach. It could start off as unsupervised with FAC. Seeing how my dataset reacts with each model, I might change approach to CAC etc.
Once I reach a verifiable hypothesis stage, I might consider developing classifiers like naive bayes to verify my hypothesis.
Programming languages would primarily be Python, and sometimes R.

### Project Action Plan

- Week 1 (11th Mar’13 – 18th Mar’13):
	- Obtain text, Text Pre-processing and Quantification of Text. Also project logistics like github repo, project website, documentation wiki.

- Week 2-3 (18th Mar’13 – 1st Apr’13)
	- Develop & analyze the quantitative model of the literary text. Develop models, validate results.

- Week 4-5 (1st Apr’13 – 15th Apr’13) 
	- Develop verifiable research hypothesis. Tweak the model if necessary. Validate results.

- Week 6-7 (15th Apr’13 – 29th Apr’13)
	- Summarize findings. Work on final presentation/paper.