
import sys
sys.path.insert(0,'/home/mohammed/src/personal_learning/work_relevance/src/')

import pandas as pd
from relevancy_calculator import query_to_string_list,word_locator


def test_query_to_string_list_letters():
    assert query_to_string_list("Hola") == ["Hola"]
    
def test_query_to_string_list_letters_and_punctuation():
    assert query_to_string_list("???Hola!??") == ["Hola"]

def test_query_to_string_list_letters_and_numbers():
    assert query_to_string_list("1231313Hola!") == ["1231313Hola"]

def test_query_to_string_list_numbers():
    assert query_to_string_list("12313") == ["12313"]

def test_query_to_string_list_punctuation():
    assert query_to_string_list("!!!") == []

def test_word_locator():
    test_dataframe = pd.read_csv('/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv')
    wordy = word_locator(test_dataframe,'the','words')
    assert len(wordy) > 0
    #test_dataframe['words'] = un