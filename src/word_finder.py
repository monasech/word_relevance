import pandas as pd
from pandas.core.frame import DataFrame
import os
import numpy as np
import re


def filenameParser(path):

     ''' 
     Creates a list of the file names in a given directory
     '''
     files = os.listdir(path)

     filenames = []

     for file in files:
          #print(file)
          filenames.append(file)
          #print(len(filenames))
     
     return filenames



def unique_word_finder(path):
    ''' This function will parse all text files in a given directory, and return all the unique words as a set'''
    filenames = filenameParser(path)
    unique_words = []
    for f in filenames:
        with open(path + '/' + f,'r') as file:
            current_doc_all_words_ = (re.findall(r"([a-zA-Z\-]+)", file.read()))
            #print(len(current_doc_all_words_))
            #current_doc_unique_words_separate = re.split('\s|(?<!\d)[,.](?!\d)', current_doc_unique_words_conjoined)
            unique_words.extend(current_doc_all_words_)   
            #print(unique_words)     
    return list(set(unique_words))



def repeated_word_finder(df,path):
    '''This function will parse the dataframe for the selected word, and increment the counter for its appearance in the document it was found in'''
    filenames = filenameParser(path)
    for f in filenames:
        appended_filename = str(f.replace('.txt',''))
        #print("The Documents name is: " + appended_filename )
        df[appended_filename] = 0
        with open(path + '/' + f,'r') as file:
            current_doc_all_words = (re.findall(r"([a-zA-Z\-]+)", file.read()))
            #print(len(current_doc_all_words))
            for word in current_doc_all_words:

                word_index = (df[df['words']==word].index.values)
                df.loc[word_index,appended_filename] += 1
    return df
    
   