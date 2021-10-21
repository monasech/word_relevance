The task will be broken down as such:

1. Enumerate all text files to be parsed.
2. Parse all files for their lines and parse each line for unique words. Unique words are added to a table, along with an initialized counter of 1, whereas non-unique words will have their count incremented by one for each occurence.
3. The program is then implemented, with a function for accepting user input as a string. This string is then broken down in to individual words, which will have their word counts pulled as variables to be passed to the functions which will calclate the word importance, generality discount, and word relevance. The metrics will be given across all documents, with data sorting applied to the results for the most relevant documents to appear on top.# word_relevance
