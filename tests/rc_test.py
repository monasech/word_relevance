
import sys
sys.path.insert(0,'/home/mohammed/src/personal_learning/work_relevance/src/')

import pandas as pd
from relevancy_calculator import query_breakup,word_locator


def test_query_breakup_letters():
    assert query_breakup("Hola") == ["Hola"]
    
def test_query_breakup_letters_and_punctuation():
    assert query_breakup("???Hola!??") == ["Hola"]

def test_query_breakup_letters_and_numbers():
    assert query_breakup("1231313Hola!") == ["1231313Hola"]

def test_query_breakup_numbers():
    assert query_breakup("12313") == ["12313"]

def test_query_breakup_punctuation():
    assert query_breakup("!!!") == []

def test_word_locator():
    test_dataframe = pd.read_csv('/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv')
    wordy = word_locator(test_dataframe,'the','words')
    assert len(wordy) > 0
    #test_dataframe['words'] = un