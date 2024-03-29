import os
from os import name

import time
import csv

#from pandas.core.frame import DataFrame
from relevancy_calculator import breakup_query, word_importance, locate_word, generality_discount, word_relevance
from word_finder import find_filename,find_unique_word,find_repeated_word
import pandas as pd
import numpy as np
import tkinter 
import tkinter.filedialog
from utils import ask_directory
print("Hello World")

ask_to_rerun = input("run from phase 1? (y/n)")

start_time = time.time()
print ("Select the data location")
data_path = ask_directory("Directory Selection","Please select the directory for your data.")

print(data_path)

print("Select where to output the CSV files")
export_path_csv = ask_directory("Directory Selection","Please select the directory to save the CSVs in")


if ask_to_rerun == "y":

    print("Running Phase 1")
   
    
    
    column_names = ['words']

    



    # Begin by creating an empty dataframe, then populate it with the unique word column

    df_init = pd.DataFrame()

    df_init['words'] = find_unique_word(data_path) 
    print("--- %s seconds ---" % (time.time() - start_time))

    #Logs the success of the unique word finder function, and save the initial dataframe to a csv
    print(df_init)
    #csv_init_directory = askopenfilename()
    
    df_init.to_csv(export_path_csv +"\exported_csv_1.csv", encoding='utf-8', header=True, index=False)

    # Create a new dataframe to hold the counters for each word.
    df_counted = pd.DataFrame()

    df_counted = find_repeated_word(df_init,data_path)

    
    
    print("--- %s seconds ---" % (time.time() - start_time))


    print(df_counted)

    df_counted.to_csv(export_path_csv +"exported_csv_2.csv",index=False)

    print("--- %s seconds ---" % (time.time() - start_time))

    df_pass = df_counted
    


print("Begin phase two")
input_string = input("Please input the string you would like to parse for")
names_of_documents = find_filename(data_path)

try: df_pass
except NameError: df_pass = pd.read_csv(export_path_csv_2)
else: pass



word_list = breakup_query(input_string)

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

    number_of_documents_with_word = len(locate_word(df_pass,word,'words'))
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
# CalmCode (website) is a good resource 