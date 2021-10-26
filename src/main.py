import time
from pandas.core.frame import DataFrame
from word_finder import filenameParser,unique_word_finder,repeated_word_finder
import pandas as pd
import numpy as np
from tkinter.filedialog import askdirectory

# TODO: Have the path as user input 
#path = '/home/mohammed/src/personal_learning/work_relevance/data/'
path = askdirectory()
column_names = ['words']

start_time = time.time()



# Begin by creating an empty dataframe, then populate it with the unique word column

df_init = pd.DataFrame()

df_init['words'] = unique_word_finder(path) 
print("--- %s seconds ---" % (time.time() - start_time))

#Logs the success of the unique word finder function, and save the initial dataframe to a csv
print(df_init)
csv_init_directory = askdirectory()
df_init.to_csv(r'csv_init_directory', encoding='utf-8', header='true')

# Create a new dataframe to hold the counters for each word.
df_counted = pd.DataFrame()

df_counted = repeated_word_finder(df_init,path)

print("--- %s seconds ---" % (time.time() - start_time))


print(df_counted.info())

df_counted.to_csv(r'/home/mohammed/src/personal_learning/work_relevance/export/dftocsv.csv', sep='\t', encoding='utf-8', header='true')

print("--- %s seconds ---" % (time.time() - start_time))
# Note, the current implementation takes roughly 120 Seconds or so to run
# TODO: Create a log file for the program that details the time taken for each step

'''
df.to_csv(unique_words_counted.csv)

csv_file = open(path + '/unique_words.csv','w')

writer = csv.writer(csv_file)

writer.writerow(unique_words)

'''