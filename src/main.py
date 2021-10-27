from os import name
import time
from pandas.core.frame import DataFrame
from relevancy_calculator import query_breakup, word_importance, word_locator, generality_discount, word_relevance
from word_finder import filenameParser,unique_word_finder,repeated_word_finder
import pandas as pd
import numpy as np
from tkinter.filedialog import askdirectory, askopenfilename

verby = input("run from phase 1? (y/n)")


if verby == "y":

    print("Running Phase 1")
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
    csv_init_directory = askopenfilename()
    df_init.to_csv(csv_init_directory, encoding='utf-8', header=True, index=False)

    # Create a new dataframe to hold the counters for each word.
    df_counted = pd.DataFrame()

    df_counted = repeated_word_finder(df_init,path)

    print("--- %s seconds ---" % (time.time() - start_time))


    print(df_counted)

    df_counted.to_csv('/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv',index=False)

    print("--- %s seconds ---" % (time.time() - start_time))

    df_pass = df_counted

# Pass the query strings  to the query_breakup function, then receive a list of words. Iterate 
# through these words and get the word importance, generality discount, and word relevance of each

print("Begin phase two")
input_string = "tennis match"

try: df_pass
except NameError: df_pass = pd.read_csv('/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv')
else: pass

try: path
except NameError: path = '/home/mohammed/src/personal_learning/work_relevance/data'
else: pass

word_list = query_breakup(input_string)

print(word_list)


df_result = pd.DataFrame()

df_result["word_query"] = word_list

names_of_documents = filenameParser(path)

for word in word_list:
    
    word_index = (df_result[df_result["word_query"] == word].index.values)
    word_row = np.array(df_result.iloc[word_index,2:])
    
    number_of_documents_with_word = len(word_locator(df_pass,word,'words'))
    #print(df_pass)
    #print(number_of_documents_with_word)
    number_of_documents = len(names_of_documents)
    #print(number_of_documents)
    #df_result["generality discount"] = 0

    for name in names_of_documents:
        if number_of_documents_with_word == 0:
    
            gen_discount = 0
            df_result.loc[word_index,"generality_discount"] = gen_discount
            print(df_result)
        else: 
            gen_discount = generality_discount(number_of_documents_with_word,number_of_documents)
            df_result.loc[word_index,"generality_discount"] = gen_discount
            print(df_result)

        df_result.loc[word_index,"word importance of"] = word_importance(df_result.loc(word_index,name).value(),df_result.loc[:,name].sum()) 
        df_result.loc[word_index,"word relevance of"] = word_relevance(df_result.loc[word_index,"word importance of"].value(),df_result.loc[word_index,"generality_discount"].value()) 

    

    print(df_result)










# TODO: Create a log file for the program that details the time taken for each step
