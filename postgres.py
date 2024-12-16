import psycopg2
import time
import csv
from psycopg2._psycopg import connection

def create_table(conn:connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            first_name character varying NULL,
            last_name character varying NULL,
            company character varying NULL,
            city character varying NULL,
            country character varying NULL,
            phone character varying NULL,
            email character varying NULL
        )
    '''
    )
    conn.commit()
    cursor.close()

def delete_table(conn: connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        DELETE FROM customers
        '''
    )
    cursor.close()

def insert(conn:connection):
    cursor = conn.cursor()
    
    with open('customers-500000.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data)
        with open('./logs/tempos_postgres.txt', 'a+') as log_file:
            for linha in data:
                start_time = time.perf_counter() #inicio do tempo
                # ['19705', 'fdca2d73C3Bf883', 'Spencer', 'Fitzpatrick', 'Mcintyre-Paul', 'Francishaven', 'Andorra', '(496)135-0763x0675', '426.072.4187x9174', 'ebruce@jarvis-nash.info', '2021-10-08', 'https://www.gutierrez-barber.info/']
                cursor.execute(
                    '''
                    INSERT INTO customers (first_name, last_name, company, city, country, phone, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ''',
                    (linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[9])
                )
                conn.commit()
                end_time = time.perf_counter()            
                #fim do tempo em milissegundos
                elapsed = (end_time - start_time) * 1000
                log_file.write(f"{elapsed:.4f}\n")
    cursor.close()
        
def select_all(conn: connection):
    cursor = conn.cursor()
    start_time = time.perf_counter() # inicio do tempo
    cursor.execute(
        '''
        SELECT * FROM customers
        '''
    )
    rows = cursor.fetchall()
    end_time = time.perf_counter() # fim do tempo
    elapsed = (end_time - start_time) * 1000 # tempo em milissegundos
    cursor.close()
    print(f"Select all action took {elapsed:.4f} milliseconds")

def calculate_average():
    with open('./logs/tempos_postgres.txt', 'r') as log_file:
        lines = log_file.readlines()
        total = 0
        for line in lines:
            total += float(line)
        print(total)
        print(len(lines))
        return total / len(lines)
    
def perform_postgres_action():

    conn = psycopg2.connect(
        dbname="tcc",
        user="tcc",
        password="tcc",
        host="localhost",
        port="5432"
    )

    # delete_table(conn)
    # create_table(conn)
    # insert(conn)

    # time = calculate_average()
    select_all(conn)
    # print(f"PostgreSQL action took {time:.2f} miliseconds")
    # cursor.execute("SELECT * FROM test_table WHERE name = %s", ("Test",))
    # print("PostgreSQL Fetched: ", cursor.fetchone())
    # cursor.close()
    # conn.close()

    # elapsed = time.time() - start
    # print(f"PostgreSQL action took {elapsed:.2f} seconds")



