from numpy import nan
from pandas.core.frame import DataFrame
from filename_parser import filenameParser
import pandas as pd

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