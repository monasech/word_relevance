from os import name
import time

from numpy.core.numeric import NaN
#from pandas.core.frame import DataFrame
from relevancy_calculator import query_to_string_list, word_importance, word_locator, generality_discount, word_relevance
from word_finder import filenameParser,unique_word_finder,repeated_word_finder
import pandas as pd
import numpy as np
#from tkinter.filedialog import askdirectory, askopenfilename
#TODO: Rewrite function names to be more pythonic (Verb first)
verby = input("run from phase 1? (y/n)")
mac_or_linux = input("mac or linux?")
start_time = time.time()
if mac_or_linux == "mac":

    data_path = '/Users/momo/src/training/word_relevance/data/'
    export_path_csv_1 = '/Users/momo/src/training/word_relevance/export/dft_init_to_csv.csv'
    export_path_csv_2 = '/Users/momo/src/training/word_relevance/export/dft_counted_to_csv.csv'
    export_path_csv_3 = '/Users/momo/src/training/word_relevance/export/dft_result_to_csv.csv'
else:
    data_path = '/home/mohammed/src/personal_learning/work_relevance/data/'
    export_path_csv_1 = '/home/mohammed/src/personal_learning/work_relevance/export/dft_init_to_csv.csv'
    export_path_csv_2 = '/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv'
    export_path_csv_3 = '/home/mohammed/src/personal_learning/work_relevance/export/dft_result_to_csv.csv'
if verby == "y":

    print("Running Phase 1")
    #path = '/home/mohammed/src/personal_learning/work_relevance/data/'
    
    
    column_names = ['words']

    



    # Begin by creating an empty dataframe, then populate it with the unique word column

    df_init = pd.DataFrame()

    df_init['words'] = unique_word_finder(data_path) 
    print("--- %s seconds ---" % (time.time() - start_time))

    #Logs the success of the unique word finder function, and save the initial dataframe to a csv
    print(df_init)
    #csv_init_directory = askopenfilename()
    df_init.to_csv(export_path_csv_1, encoding='utf-8', header=True, index=False)

    # Create a new dataframe to hold the counters for each word.
    df_counted = pd.DataFrame()

    df_counted = repeated_word_finder(df_init,data_path)

    
    
    print("--- %s seconds ---" % (time.time() - start_time))


    print(df_counted)

    df_counted.to_csv(export_path_csv_2,index=False)

    print("--- %s seconds ---" % (time.time() - start_time))

    df_pass = df_counted
    
# Pass the query strings  to the query_to_string_list function, then receive a list of words. Iterate 
# through these words and get the word importance, generality discount, and word relevance of each

print("Begin phase two")
input_string = input("Please input the string you would like to parse for")
names_of_documents = filenameParser(data_path)

try: df_pass
except NameError: df_pass = pd.read_csv(export_path_csv_2)
else: pass



word_list = query_to_string_list(input_string)

print(" The list of words to be tested is :")
print(word_list)


df_result = pd.DataFrame()

df_result["word_query"] = word_list


for word in word_list:
    
    word_index_result = (df_result[df_result["word_query"] == word].index.values)
    
    word_index_pass_array = (df_pass[df_pass["words"] == word].index.values)
    word_index_pass_list = word_index_pass_array.tolist()
    
    try: word_index_pass = word_index_pass_list[0]
    except IndexError: word_index_pass = NaN
    else: pass

    print(type(word_index_pass))
    print("Word index incoming")
    print(word_index_result)
    print(word_index_pass)
    #ord_row = df_pass.iloc[word_index_pass,:]

    number_of_documents_with_word = len(word_locator(df_pass,word,'words'))
    print(df_pass)
    
    print("number of documents with word = " + str(number_of_documents_with_word))
    number_of_documents = len(names_of_documents)

    if number_of_documents_with_word == 0:
    
            gen_discount = 0
            df_result.loc[word_index_result,"generality_discount"] = gen_discount
            #print(df_result)
    else: 
            gen_discount = generality_discount(number_of_documents_with_word,number_of_documents)
            df_result.loc[word_index_result,"generality_discount"] = gen_discount


    #print(number_of_documents)
    #df_result["generality discount"] = 0

    for name in names_of_documents:
        appended_name = str(name.replace('.txt',''))
        #print(appended_name)
        
            #print(df_result)
        word_importance_column_name = "word importance in " + appended_name
        word_relevance_column_name = "word relevance in" + appended_name
        # Error seems to be in line 119
        print("line 120 below")
        print(word_index_pass)
        print(appended_name)
        #frequency_of_word = df_pass.at[word_index_pass,appended_name]
        try: frequency_of_word = df_pass.at[word_index_pass,appended_name]
        except ValueError: frequency_of_word = 0
        else: pass

        print("the frequency of the word is = " + str(frequency_of_word))
        total_words_in_document = df_pass[appended_name].sum()
        print("the total words in the document is = " + str(total_words_in_document))
        
             
        word_importance_value = word_importance(frequency_of_word,total_words_in_document) 
        df_result.loc[word_index_result,word_importance_column_name] = word_importance_value
        word_relevance_value = word_relevance(word_importance_value,gen_discount)
        
        df_result.loc[word_index_result,word_relevance_column_name] =  word_relevance_value

    

    print(df_result)
df_result.to_csv(export_path_csv_3,index=False)

print("--- %s seconds ---" % (time.time() - start_time))



# TODO: Prompts, configurations, gui file and directory selector.
# TODO: Convert for loops to lambda functions
# TODO: Improve readibility, use code blocks 
# TODO: Use dictionary and list comprehensions

# TODO: Create a log file for the program that details the time taken for each step

# TODO: After finishing all todos, work on kedro pipeline and packaging. Explore writing a front-end interface and an API [FAST API].
# TODO: 