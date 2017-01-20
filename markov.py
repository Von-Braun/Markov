# -*- coding: utf-8 -*-
import sys
import random
import string
printable = set(string.printable)

def load_data(file_name='markov_database'):
    with open(file_name+'.txt', 'r') as text_file:
        pure_all_text=text_file.read().replace('\n', ' ')
    pure_all_text=filter(lambda x: x in printable, pure_all_text)
    return pure_all_text.encode('ascii', 'ignore').translate(None, '+-[]{}()=_*&^%$#@<>/\\|:;\"\'~`')

#Build the Markov Chain database
def build_database(text, file_name='markov_database'):
    text=filter(lambda x: x in printable, text)
    all_text=text.encode('ascii', 'ignore').translate(None, '+-[]{}()=_*&^%$#@<>/\\|:;\"\'~`')

    with open(file_name+".txt", "w") as text_file:
        text_file.write(all_text)

#ANALYSE_TEXT--------------------------------------------------------------------------------------------------------------------------------
def build_markov_dictionary(text,size=2):
    temporary=''
    markov_dictionary={}
    text=text.split(' ')
    text = filter(lambda a: a != '', text)
    for i in range(len(text) - 2):
        temporary=''
        space=''
        for amount in range(0,size):
            if amount>0: space=' '
            temporary=temporary+space+str(text[i+amount])

        try:
           markov_dictionary.setdefault(temporary,[]).append(str(text[i+size]))
        except:
            pass
    return markov_dictionary

#FOR TWO WORDS---------------------------------------------------------------------------------------------------------------------------------
#get the first two words
def make_sentance(text,markov_dictionary,ending_charecters_list=['.','!','?'],size=2):
    start_options=[] #make a list of all the first two words of all sentences
    text=text.split()
    text = filter(lambda a: a != '', text)
    for i in range(0,len(text)):
        word=text[i]
        word_is_an_ending=False
        for end_charecter in ending_charecters_list:
            if word.endswith(end_charecter):
                word_is_an_ending=True
                
        if word_is_an_ending:
            try:
                start_text=[]
                for amount in range(1,size+1):
                    start_text.append(text[i+amount])
                start_options.append(' '.join(start_text))
            except:
                pass
    sentence=random.choice(start_options)

    #generate sentence
    last=sentence.split(' ')[len(sentence.split(' '))-1] #last word
    ending=[]
    for i in range(1,size+1):
        ending.append(sentence.split(' ')[len(sentence.split(' '))-i])

    while not (last.endswith('.') or last.endswith('!') or last.endswith('?')): #stop at end of a sentance
        ending=[]
        for i in range(1,size+1):
            ending.append(sentence.split(' ')[len(sentence.split(' '))-i])
        ending.reverse()
        try:
            sentence=sentence+' '+random.choice(markov_dictionary[' '.join(ending)]) #pick one of the words that tends to come after the last two
        except:
            sentence=sentence+'.'
        last=sentence.split(' ')[len(sentence.split(' '))-1] #last word
    return sentence