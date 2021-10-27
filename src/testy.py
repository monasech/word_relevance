import pandas as pd

from relevancy_calculator import word_locator
test_dataframe = pd.read_csv('/home/mohammed/src/personal_learning/work_relevance/export/dft_counted_to_csv.csv')
print(test_dataframe)

wordy = len(word_locator(test_dataframe,'the','words'))

print("wordy is")
print(wordy)
# print(len(wordy))