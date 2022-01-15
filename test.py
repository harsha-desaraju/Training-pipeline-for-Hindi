import stanfordnlp

nlp = stanfordnlp.Pipeline(lang = 'hi' , processors = 'tokenize,mwt')

doc = nlp('नहीं।')

print(doc.sentences[0].words[0].text)
print(doc.sentences[0].words[1].text)
