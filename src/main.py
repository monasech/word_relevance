from pandas.core.frame import DataFrame
#from filename_parser import filenameParser
from unique_word_finder import unique_word_finder
from repeated_word_finder import repeated_word_finder
import pandas as pd
path = '/Users/momo/src/training/word_relevance/data'
column_names = ['words']


#TODO: Remove the below code if the function works properly




# Begin by creating an empty dataframe, then populate it with the unique word column
df_init = pd.DataFrame()

df_init['words'] = unique_word_finder(path) 

#Logs the success of the unique word finder function
print(df_init.info())

df_counted = repeated_word_finder(df_init,path)

print(df_counted.info())

'''
csv_file = open(path + '/unique_words.csv','w')

writer = csv.writer(csv_file)

writer.writerow(unique_words)
'''