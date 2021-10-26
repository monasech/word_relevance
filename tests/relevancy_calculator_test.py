
import sys
sys.path.insert(0,'/home/mohammed/src/personal_learning/work_relevance/src/')

from relevancy_calculator import query_breakup

def test_query_breakup_letters():
    assert query_breakup("Hola") == ["Hola"]
    
def test_query_breakup_letters_and_punctuation():
    assert query_breakup("???Hola!??") == ["Hola"]

def test_query_breakup_letters_and_numbers():
    assert query_breakup("1231313Hola!") == ["Hola"]

def test_query_breakup_numbers():
    assert query_breakup("12313") == ["12313"]

def test_query_breakup_punctuation():
    assert query_breakup("!!!") == []

