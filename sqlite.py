import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values ('TANH', 'ENGEERNING', 'A')''')
cursor.execute('''Insert Into STUDENT values ('DUNG', 'Data Science', 'B')''')
cursor.execute('''Insert Into STUDENT values ('TOAN', 'Data Science', 'C')''')
cursor.execute('''Insert Into STUDENT values ('HUYEN', 'ENGEERNING', 'D')''')



data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()

    