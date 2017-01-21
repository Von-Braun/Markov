# Markov chain in python
Example.py demonstrates its use.

Ted.txt is a collection of Ted Hughes poems, used by example.py.

# Function description

build_markov_dictionary(text,complexity)

* text = the sample text used for building the markov chains(markov_dictionary).

* complexity = the number of consecutive words to link together.

make_sentance(text,markov_dictionary,ending_charecters,complexity)

* text = the sample text used for creating a list of words used for the start and end of sentences.

* markov_dictionary = used for generating the sentences. It is returned from the build_markov_dictionary function.

* ending_charecters = a list of charecters used to denote the end of a sentence. e.g. ['!','.','?'] etc.

* complexity = the number of consecutive words to link together. It must be the same as the value used to generate the markov_dictionary.
