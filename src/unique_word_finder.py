# TODO: Need to write a function to parse all files for words, add them to a giant list. then filter for unique words. 
from filename_parser import filenameParser
#import csv

#path = '/Users/momo/src/training/word_relevance/data'


def unique_word_finder(path):
    ''' This function will parse all text files in a given directory, and return all the unique words as a set'''
    filenames = filenameParser(path)
    unique_words = set()
    for f in filenames:
        open_doc = open(path + '/' + f,'r')
        for line in open_doc:
            for word in line.split():
                unique_words.add(word)
    return list(unique_words)


#TODO: Remove the below code if the function works properly
'''
print(len(unique_words))

csv_file = open(path + '/unique_words.csv','w')

writer = csv.writer(csv_file)

writer.writerow(unique_words)
'''