from os import name
import time
#from pandas.core.frame import DataFrame
from relevancy_calculator import query_breakup, word_importance, word_locator, generality_discount, word_relevance
from word_finder import filenameParser,unique_word_finder,repeated_word_finder
import pandas as pd
import numpy as np
#from tkinter.filedialog import askdirectory, askopenfilename

verby = input("run from phase 1? (y/n)")


if verby == "y":

    print("Running Phase 1")
    #path = '/home/mohammed/src/personal_learning/work_relevance/data/'
    data_path = '/Users/momo/src/training/word_relevance/data/'
    export_path_csv_1 = '/Users/momo/src/training/word_relevance/export/dft_init_to_csv.csv'
    export_path_csv_2 = '/Users/momo/src/training/word_relevance/export/dft_counted_to_csv.csv'
    export_path_csv_3 = '/Users/momo/src/training/word_relevance/export/dft_result_to_csv.csv'
    column_names = ['words']

    start_time = time.time()



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

# Pass the query strings  to the query_breakup function, then receive a list of words. Iterate 
# through these words and get the word importance, generality discount, and word relevance of each

print("Begin phase two")
input_string = "tennis match"

try: df_pass
except NameError: df_pass = pd.read_csv('/Users/momo/src/training/word_relevance/export/dft_counted_to_csv.csv')
else: pass

try: data_path
except NameError: data_path = '/Users/momo/src/training/word_relevance/data/'
else: pass

try: export_path_csv_3
except NameError: export_path_csv_3 = '/Users/momo/src/training/word_relevance/export/dft_result_to_csv.csv'
else: pass

word_list = query_breakup(input_string)

print(word_list)


df_result = pd.DataFrame()

df_result["word_query"] = word_list

names_of_documents = filenameParser(data_path)

for word in word_list:
    
    word_index_result = (df_result[df_result["word_query"] == word].index.values)
    
    word_index_pass = (df_pass[df_pass["words"] == word].index.values)
    print("Word index incoming")
    print(word_index_result)
    print(word_index_pass)
    word_row = np.array(df_result.iloc[word_index_result,2:])
    
    number_of_documents_with_word = len(word_locator(df_pass,word,'words'))
    #print(df_pass)
    #print(number_of_documents_with_word)
    number_of_documents = len(names_of_documents)
    #print(number_of_documents)
    #df_result["generality discount"] = 0

    for name in names_of_documents:
        appended_name = str(name.replace('.txt',''))
        print(appended_name)
        if number_of_documents_with_word == 0:
    
            gen_discount = 0
            df_result.loc[word_index_result,"generality_discount"] = gen_discount
            print(df_result)
        else: 
            gen_discount = generality_discount(number_of_documents_with_word,number_of_documents)
            df_result.loc[word_index_result,"generality_discount"] = gen_discount
            print(df_result)
        word_importance_column_name = "word importance of -> " + appended_name
        word_relevance_column_name = "word relevance of -> " + appended_name
        #print(df_result.loc[word_index,appended_name])
        #print(df_result.loc[:,appended_name].sum())
        word_importance_value = word_importance(df_pass.loc[word_index_pass,appended_name],df_pass.loc[:,appended_name].sum()) 
        df_result.loc[word_index_result,word_importance_column_name] = word_importance_value
        word_relevance_value = word_relevance(df_result.loc[word_index_result,word_importance_column_name],df_result.loc[word_index_result,"generality_discount"])
        
        df_result.loc[word_index_result,word_relevance_column_name] =  word_relevance_value

    

    print(df_result)
df_result.to_csv(export_path_csv_3,index=False)









# TODO: Create a log file for the program that details the time taken for each step
