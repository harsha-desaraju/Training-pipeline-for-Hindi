import stanfordnlp

nlp = stanfordnlp.Pipeline(lang='hi',processors='tokenize,mwt,pos')

i=0

file = open('/home/iiser/Hindi Corpora/2012/hin_newscrawl_2012_1M-sentences.txt','r')
file1 = open('new.txt','w')

for line in file:
	doc = nlp(line)
	List = []
	word_list = doc.sentences[0].words
	for j in range(0,len(word_list)):
		List.append(word_list[j].text)

	temp = str(List) + '\n'
	file1.write(temp)
	i+=1
	
	if i>200:
		break
		
file1.close()
file.close()


	
