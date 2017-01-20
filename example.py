import markov

sentence_count=3
paragraph_count=2
sentence_limit=50
complexity=3


text=markov.load_data('markov_database')
#markov.build_database(text)
markov_dictionary1=markov.build_markov_dictionary(text,complexity)
print '-'*80
for I in range(0,paragraph_count):
	for i in range(0,sentence_count):
		generated_text = '//'*sentence_limit
		while generated_text in open('ted.txt').read() or len(generated_text)>sentence_limit:
		    generated_text = markov.make_sentance(text,markov_dictionary1,['.','/','\n'],complexity)
		print generated_text
	print ''
print '-'*80
