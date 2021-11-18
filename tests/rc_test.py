
import sys
sys.path.insert(0,'/home/mohammed/src/personal_learning/work_relevance/src/')

import pandas as pd
<<<<<<< HEAD
from relevancy_calculator import breakup_query,locate_word


def test_breakup_query_letters():
    assert breakup_query("Hola") == ["Hola"]
    
def test_breakup_query_letters_and_punctuation():
    assert breakup_query("???Hola!??") == ["Hola"]

def test_breakup_query_letters_and_numbers():
    assert breakup_query("1231313Hola!") == ["1231313Hola"]

def test_breakup_query_numbers():
    assert breakup_query("12313") == ["12313"]

def test_breakup_query_punctuation():
    assert breakup_query("!!!") == []
=======
from relevancy_calculator import query_to_string_list,locate_word


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
>>>>>>> b0278680bdd15db3301a84052422610155de4a5d

def test_locate_word():
    test_dataframe = pd.read_csv('/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv')
    wordy = locate_word(test_dataframe,'the','words')
    assert len(wordy) > 0
    #test_dataframe['words'] = un