import sys,os
import stanfordnlp

nlp = stanfordnlp.Pipeline(lang = 'hi')

file = open(sys.argv[1],'r')
file1 = open(sys.argv[2],'w')

doc = nlp(file.read())
for sent in doc.sentences:
	for wrd in sent.words:
		temp = wrd.index + '\t' + wrd.text + '\t' + wrd.lemma + '\t' + wrd.upos + '\t' + wrd.xpos + '\t' + '_' + '\t' + str(wrd.governor) + '\t' + wrd.dependency_relation + '\t' + '_' + '\t' + '_' + '\n'
		file1.write(temp)
	
	file1.write('\n')
		
file1.close()
file.close()


		
		 
