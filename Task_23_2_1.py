import psycopg2
con = psycopg2.connect(
    database = 'postgres',
    user ='postgres',
    password ='****',
    host = '127.0.0.1',
    port='5433'

)
cur= con.cursor()
cur.execute('''SELECT * FROM book6 
            ''')
rows = cur.fetchall()
max_len=0
lst1=[]
for row in rows:
    print(f'id = {row[0]}',end = ', ')
    print(f' title = {row[1]}', end = ',')
    print(f'author = {row[2]}', end = ', ')
    print(f'publisher_id = {row[3]}', end = ', ')
    print(f'amount = {row[4]}', end = ', ')
    print(f'price = {row[5]}',end = ', ')
    print(f'author_id = {row[6]}')
con.close
