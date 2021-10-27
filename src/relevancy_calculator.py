import pandas as pd
import numpy as np
import re
import math

def query_breakup(string_query):
        '''
        This function will take the strings that will have the relevancy calculator functions 
        applied to them, and split them into individual words. 
        '''
        query_list = re.split(r"\s+", string_query)
        
               # query_list.append((re.findall(r"([a-zA-Z0-9\-]+)", word)))
        
        print(query_list)

        return query_list


def word_locator(df, word,column_name):
        '''
        This function takes as input a pandas dataframe containing a column of unique words
        and columns detailing the frequency a particular word appears in a document.
        The function then returns the list of documents that contain the word.
        '''
        word_index = (df[df[column_name] == word].index.values)
        print(word_index)
        word_row = np.array(df.iloc[word_index,2:])
        print(word_row)
        documents_containg_word = list(zip(*np.where(word_row>0)))

        return documents_containg_word

def generality_discount(number_of_documents_with_word,number_of_documents):
    '''
    This function takes the number of documents in the corpus N and the number of documents containing the word n
    and returns the generality discount for the word.
    '''
    return math.log10(number_of_documents)/number_of_documents_with_word
    
def word_importance(frequency_row,total_words_row):
        '''
        This function takes the row of document frequency and the row for total words
        and returns the word importance in a Pandas dataframe row.
        '''
        return frequency_row/total_words_row

def word_relevance(word_importance, generality_discount):
        '''
        This function takes the word importance and generality discount and 
        returns the word relevance by performing element multiplication.
        '''
        return word_importance * generality_discount
    # find row that contains the word w, then find columns where that value is > 1
    # Afterwards with that count, create a dataframe with the word, and the generality discount for each

    

