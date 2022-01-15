import stanfordnlp
import pandas as pd

def f(x):
	return x*x

def extract_lemma(doc):
	parsed_text = {'word' : [],'lemma' : []}
	for sent in doc.sentences:
		for wrd in sent.words:
			parsed_text['word'].append(wrd.text)
			parsed_text['lemma'].append(wrd.lemma)
			
	return pd.DataFrame(parsed_text)


nlp = stanfordnlp.Pipeline(processors = "tokenize,mwt,lemma,pos")

Doc = nlp("The prospects for Britain’s orderly withdrawal from the European Union on March 29 have receded further, even as MPs rallied to stop a no-deal scenario.")

# Doc.sentences[0].print_tokens()

print(extract_lemma(Doc))


