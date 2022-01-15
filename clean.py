import stanfordnlp
lang = "hi"

config = {
	'processors': 'tokenize,mwt',
	'lang' : f"{lang}",
}

nlp = stanfordnlp.Pipeline(**config)

f=open('Hindi_201_sents.txt','r')

doc = nlp(f.read())
sent_array=[]

for sent in doc.sentences :
	for word in sent.words :
		sent_array.append(word.text)
		
	g = open('output','a+')
	for i in sent_array:
		g.write(str(i)+ '  ')
	g.write('\n')
		
	sent_array = []
		
