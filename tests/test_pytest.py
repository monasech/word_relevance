import sys
sys.path.insert(0,'/home/mohammed/src/personal_learning/work_relevance/src/')

import relevancy_calculator as rc

def test_increment():
    assert rc.query_breakup("Hola!") == ["Hola"]

