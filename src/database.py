import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('words.db')

# Create a cursor
c = conn.cursor()

arr_test = ["one", "two", "three", "four", "five"]

for i in arr_test:
     c.execute('''ALTER TABLE words ADD COLUMN ''' + i + ''' INTEGER ''')

print(len(arr_test))

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

