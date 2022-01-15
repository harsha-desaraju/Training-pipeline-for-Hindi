import sys,os
import stanfordnlp

nlp = stanfordnlp.Pipeline(lang='hi',processors='tokenize')

i=0

file = open(sys.argv[1],'r')
file1 = open(sys.argv[2],'w')

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


	
