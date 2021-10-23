from numpy import nan
from pandas.core.frame import DataFrame
from filename_parser import filenameParser
import pandas as pd

# TODO: On a separate file, take the dataframe produced by this file as an input and return a populated dataframe with the frequencies of the words.



# Then need to create a dataframe with the all the words in the words column, and all file names in the rest of the columns, with values set to zero initially.
def repeated_word_finder(data,path):
    '''This function will parse the dataframe for the selected word, and increment the counter for its appearance in the document it was found in'''
    filenames = filenameParser(path)
    for f in filenames:
        print(f)
        appended_filename = str(f.replace('.txt',''))
        print(appended_filename)
        data[appended_filename] = 0
        print(data.info())
        print("opening the document")
        open_doc = open(path + '/' + f,'r')
        print("document opened")
        for line in open_doc:
            print("canary first for loop")
            for word in line.split():
                print("canary second for loop")
                dfrow_index = data.index[data['words'] == word]
                print(dfrow_index)
                data.at[dfrow_index,appended_filename] += 1
        