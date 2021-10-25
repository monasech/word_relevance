# TODO: Need to write a function to parse all files for words, add them to a giant list. then filter for unique words. 
from filename_parser import filenameParser
import pandas as pd
from pandas.core.frame import DataFrame
import os


def filenameParser(path):

     ''' 
     Creates a list of the file names in a given directory
     '''
     files = os.listdir(path)

     filenames = []

     for file in files:
          print(file)
          filenames.append(file)
          print(len(filenames))
     
     return filenames
#import csv

#path = '/Users/momo/src/training/word_relevance/data'


def unique_word_finder(path):
    ''' This function will parse all text files in a given directory, and return all the unique words as a set'''
    filenames = filenameParser(path)
    unique_words = set()
    for f in filenames:
        open_doc = open(path + '/' + f,'r')
        for line in open_doc:
            for word in line.split():
                unique_words.add(word)
    return list(unique_words)


# TODO: On a separate file, take the dataframe produced by this file as an input and return a populated dataframe with the frequencies of the words.



# Then need to create a dataframe with the all the words in the words column, and all file names in the rest of the columns, with values set to zero initially.
def repeated_word_finder(df,path):
    '''This function will parse the dataframe for the selected word, and increment the counter for its appearance in the document it was found in'''
    filenames = filenameParser(path)
    for f in filenames:
        # TODO: Need to insert a column with the new filename into the dataframe
        print(f)
        appended_filename = str(f.replace('.txt',''))
        print("The Documents name is: " + appended_filename )
        df[appended_filename] = 0
        print(df.info())
        print("opening the document")
        open_doc = open(path + '/' + f,'r')
        print("document opened")
        for line in open_doc:
            print("canary first for loop")
            for word in line.split():
                # TODO: Check for None or Empty
                if word:
                    print("canary second for loop")
                    #dfrow_index = df.index[df['words'].value == word]
                    #print(dfrow_index)
                    word_index = (df[df['words']==word].index.values)
                    print(word_index)
                    # Have managed to pull the row index for the word, TODO: need to figure out the counter incrementation
                    df.ix[word_index,appended_filename] += 1
    return df