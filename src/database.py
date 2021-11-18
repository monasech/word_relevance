import sqlite3
from filename_parser import parse_filename

filenames = parse_filename('/Users/momo/src/training/word_relevance/data')

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('words.db')

# Create a cursor
c = conn.cursor()

print(len(filenames))
sanitized_filenames = {x.replace('.txt','') for x in filenames}

for f in sanitized_filenames:
    c.execute('''ALTER TABLE words ADD COLUMN ''' + f + ''' INTEGER ''')



'''# Create a Table TODO: Automate the table column population based on the documents inside the folder
c.execute("""CREATE TABLE words (
    word text,
    Document_1_Frequency integer,
    Document_2_Frequency integer,
    Document_3_Frequency integer
)""")
'''

'''many_felines = [
                   ('tester', '1', '2','3'), 
                  ('cat', 2, 3, 2), 
                    ('felin', 1, 2, '3'),
                ]
'''
#c.executemany("INSERT INTO words VALUES (?,?,?,?)", many_felines)

#c.execute("INSERT INTO words VALUES('Gato', 1, 2, 3)")
#print("Command executed successfully")

# Commit our command
conn.commit()

# Close our connection
conn.close()

