import pandas as pd
from pandas.core.frame import DataFrame
import os
import numpy as np
import re




<<<<<<< HEAD
def find_filename(path):
=======
def parse_filename(path):
>>>>>>> b0278680bdd15db3301a84052422610155de4a5d

     ''' 
     Creates a list of the file names in a given directory
     '''
     files = os.listdir(path)

     filenames = []

     for file in files:
          filenames.append(file)
     
     return filenames



def find_unique_word(path):
    ''' This function will parse all text files in a given directory, and return all the unique words as a set'''
<<<<<<< HEAD
    filenames = find_filename(path)
=======
    filenames = parse_filename(path)
>>>>>>> b0278680bdd15db3301a84052422610155de4a5d
    unique_words = []
    for f in filenames:
        with open(path + '/' + f,'r') as file:
            #TODO: Consolidate all regex functions under one function
            current_doc_all_words_ = (re.findall(r"([a-zA-Z0-9\-]+)", file.read()))
            #current_doc_all_words_ = alphanumeric_parser(file)
            #print(len(current_doc_all_words_))
            #current_doc_unique_words_separate = re.split('\s|(?<!\d)[,.](?!\d)', current_doc_unique_words_conjoined)
            unique_words.extend(current_doc_all_words_)   
            #print(unique_words)     
    return list(set(unique_words))



def find_repeated_word(df,path):
    '''This function will parse the dataframe for the selected word, and increment the counter for its appearance in the document it was found in'''
<<<<<<< HEAD
    filenames = find_filename(path)
=======
    filenames = parse_filename(path)
>>>>>>> b0278680bdd15db3301a84052422610155de4a5d
    for f in filenames:
        appended_filename = str(f.replace('.txt',''))
        #print("The Documents name is: " + appended_filename )
        df[appended_filename] = 0
        with open(path + '/' + f,'r') as file:
            current_doc_all_words = (re.findall(r"([a-zA-Z0-9\-]+)", file.read()))
            #print(len(current_doc_all_words))
            for word in current_doc_all_words:

                word_index = (df[df['words']==word].index.values)
                df.loc[word_index,appended_filename] += 1
    print(df)           
    return df
    
   