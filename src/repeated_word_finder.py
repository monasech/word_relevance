from pandas.core.frame import DataFrame
from filename_parser import filenameParser
import pandas as pd


# TODO: Refactor the code below to take in the filenames and unique words as input, and create a dataframe with that input
# TODO: On a separate file, take the dataframe produced by this file as an input and return a populated dataframe with the frequencies of the words.
path = '/Users/momo/src/training/word_relevance/data'


#sanitized_filenames = {x.replace('.txt','') for x in filenames}

#column_names = ['words'] #+ list(sanitized_filenames)

#df = pd.DataFrame(columns = column_names)

# Then need to create a dataframe with the all the words in the words column, and all file names in the rest of the columns, with values set to zero initially.
def repeated_word_finder(data,path):
    '''This function will parse the dataframe for the selected word, and increment the counter for its appearance in the document it was found in'''
filenames = filenameParser(path)
for f in filenames:
    #data[f.replace('.txt','')] = pd.Series(dtype='int')
    open_doc = open(path + '/' + f,'r')
    for line in open_doc:
        for word in line.split():
            if word in data.words.values:
                dfrow_index = data.index[df['words'] == word]
                data.at[dfrow_index,f] += 1
# Need to return the row index for the word. Afterwards, need to find the corresponding document counter and increment by one                 
    
    
    print(df)
print(df)