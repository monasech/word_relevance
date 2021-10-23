import os


def filenameParser(path):

     ''' 
     Creates a list of the file names in a given directory
     '''
     files = os.listdir(path)

     filenames = []

     for file in files:
          print(file)
          filenames.append(file)
          print(len(filenames))
     
     return filenames