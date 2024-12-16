import psycopg2
import time
import csv
from psycopg2._psycopg import connection

def create_table(conn:connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products (
            asin character varying PRIMARY KEY,
            title character varying NULL,
            img_url character varying NULL,
            productURL character varying NULL,
            stars numeric NULL,
            reviews integer NULL,
            price money NULL,
            listPrice money NULL,
            categoryName character varying NULL,
            isBestSeller boolean NULL,
            boughtInLastMonth integer NULL
        )
    '''
    )
    conn.commit()
    cursor.close()

def delete_table(conn: connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        DELETE FROM products
        '''
    )
    cursor.close()

def insert(conn:connection):
    cursor = conn.cursor()
    
    with open('dataset_amazon') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data)
        # with open('./logs/tempos_postgres.txt', 'a+') as log_file:
        totalTime = 0
        for linha in data:
            start_time = time.perf_counter() #inicio do tempo
            # ['19705', 'fdca2d73C3Bf883', 'Spencer', 'Fitzpatrick', 'Mcintyre-Paul', 'Francishaven', 'Andorra', '(496)135-0763x0675', '426.072.4187x9174', 'ebruce@jarvis-nash.info', '2021-10-08', 'https://www.gutierrez-barber.info/']
            cursor.execute(
                '''
                INSERT INTO products (asin, title, img_url, productURL, stars, reviews, price, listPrice, categoryName, isBestSeller, boughtInLastMonth)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''',
                (linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10])
            )
            conn.commit()
            end_time = time.perf_counter()            
            #fim do tempo em milissegundos
            elapsed = (end_time - start_time) * 1000
            totalTime += elapsed
            # log_file.write(f"{elapsed:.4f}\n")
    cursor.close()
    print(f"Insert action took {totalTime:.4f} milliseconds")
        
def select_all(conn: connection):
    cursor = conn.cursor()
    start_time = time.perf_counter() # inicio do tempo
    cursor.execute(
        '''
        SELECT * FROM products
        '''
    )
    rows = cursor.fetchall()
    end_time = time.perf_counter() # fim do tempo
    elapsed = (end_time - start_time) * 1000 # tempo em milissegundos
    cursor.close()
    print(f"Select all action took {elapsed:.4f} milliseconds")

def perform_postgres_action():

    conn = psycopg2.connect(
        dbname="tcc",
        user="tcc",
        password="tcc",
        host="localhost",
        port="5432"
    )

    delete_table(conn)
    create_table(conn)
    insert(conn)

    # select_all(conn)
    # print(f"PostgreSQL action took {time:.2f} miliseconds")
    # cursor.execute("SELECT * FROM test_table WHERE name = %s", ("Test",))
    # print("PostgreSQL Fetched: ", cursor.fetchone())
    # cursor.close()
    # conn.close()

    # elapsed = time.time() - start
    # print(f"PostgreSQL action took {elapsed:.2f} seconds")



