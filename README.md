The task will be broken down as such:

1. Enumerate all text files to be parsed.
2. Parse all files for their lines and parse each line for unique words. Unique words are added to a table, along with an initialized counter of 1, whereas non-unique words will have their count incremented by one for each occurence.
3. The program is then implemented, with a function for accepting user input as a string. This string is then broken down in to individual words, which will have their word counts pulled as variables to be passed to the functions which will calclate the word importance, generality discount, and word relevance. The metrics will be given across all documents, with data sorting applied to the results for the most relevant documents to appear on top.# word_relevance


The structure is as follows:

in main.py the files are called in the following order to do the following tasks:
1. filename_parser.py : Generates list of filenames in a directory
2. find_unique_word.py: Generates list of all unique words in the files
3. find_repeated_word.py: Appends the dataframe with all the instances found in each document
4. relevancy_calculator.py: Performs the mentioned word relevancy calculation on the data frame, and outputs a new dataframe along with a csv file, and saves the data frame to an sqlite database for further reference or manipulation
