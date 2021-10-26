import pandas as pd
import numpy as np
import re

def query_breakup(string_query):
        
        query_list = (re.findall(r"([a-zA-Z0-9\-]+)", string_query))
        
        print(query_list)

        return query_list


def word_locator(df, word):

        word_index = (df[df['words']==word].index.values)

        word_row = np.array(df.iloc[word_index,:])
        
        documents_containg_word = list(zip(*np.where(word_row>0)))

        return documents_containg_word

def generality_discount(df,documents_containing_word):
    '''
    This function takes the dataframe and the number of documents containing the word
    and returns the generality discount for the word.
    '''
    
    

    # find row that contains the word w, then find columns where that value is > 1
    # Afterwards with that count, create a dataframe with the word, and the generality discount for each

    

'''
The program should function as follows:
1. take as input (dataframe, string to be found)
2. Break string into individual words
3. Search dataframe for string and copy all column names and new values as such:
3 cont. df['document_8_counter'] = x
        df['document_8_total'] = y
        df['document_8_]
'''