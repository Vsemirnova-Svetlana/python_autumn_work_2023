import pandas as pd
import psycopg2
con = psycopg2.connect(
    database = 'postgres',
    user ='postgres',
    password ='shiyanbin2016',
    host = '127.0.0.1',
    port='5433'

)
cur= con.cursor()
cur.execute('''SELECT * FROM book6 
            ''')
rows = cur.fetchall()
lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []

for row in rows:
    df = pd.DataFrame({'id': lst1,
                       'title': lst2,
                       'author': lst3,
                       'publisher_id': lst4,
                       'amount': lst5,
                       'price': lst6,
                       'author_id': lst7})

    lst1.append(row[0])
    lst2.append(row[1])
    lst3.append(row[2])
    lst4.append(row[3])
    lst5.append(row[4])
    lst6.append(row[5])
    lst7.append(row[6])
con.close

print(df)