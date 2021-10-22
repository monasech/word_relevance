import os


def filenameParser(dir_location):
     files = os.listdir(dir_location)

     filenames = []

     for file in files:
          print(file)
          filenames.append(file)
          print(len(filenames))
     
     return filenames