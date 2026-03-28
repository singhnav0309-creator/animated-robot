try:
 import psycopg2
 def table():
     conn = psycopg2.connect(dbname='postgres', user='postgres', password='1234', host='localhost', port='6304')

     cursor = conn.cursor()
     cursor.execute('''create table employees(Name Text, ID int, Age int)''')
     print('Table created successfully')

     conn.commit()
     conn.close()

 def data():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='1234', host='localhost', port='6304')

    cursor = conn.cursor()

    name = input('Enter name: ')
    id = input('Enter ID: ')
    age = input('Enter age: ') 

    query = '''insert into employees(Name, ID, Age) values(%s, %s, %s);'''
    cursor.execute(query, (name, id, age))

    print('Data inserted successfully')

    conn.commit()
    conn.close()

 data()

# Create a function to extract data from the table and display it.
 def extract():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='1234', host='localhost', port='6304')
    cursor = conn.cursor() 
    cursor.execute('''select * from employees''')
    show = cursor.fetchone()
    print(show)
    #print('Data inserted successfully')

 extract()

except Exception as e:
    print('Error:', e)  

except ValueError:
    print('Invalid input. Please enter a valid value.')
     

