Our program must

- Draw a keyword cloud based on the words found in the abstract of your papers.
- Create a visualization showing the number of ﬁgures per article.
- Create a list of the links found in each paper.

To do this the program will analyse the pdfs using the grobid API and this will return an XML file that will be used to answer these three questions.

To draw a word cloud with the abstract information from the pdf, the program use the wordCloud library and extract the text between the <abstract></abstract> tags from the xml file of each pdf. 
To create the visualisation of the number of figures per article, the program will count the number of times the <figure></figure> tag appears in the XML file of each pdf and will use the matplotlib.pyplot library to create the histogram.
To create a list of links we will  search in the XML file for <ptr target> tags, that contain a phrase that follows this pattern "https?://[^\s]+".
