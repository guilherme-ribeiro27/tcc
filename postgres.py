import psycopg2
import time

def perform_postgres_action():
    start = time.time()

    conn = psycopg2.connect(
        dbname="test_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Teste de criação de tabela e inserção
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            value INTEGER
        )
    """)
    cursor.execute("INSERT INTO test_table (name, value) VALUES (%s, %s)", ("Test", 123))
    conn.commit()

    cursor.execute("SELECT * FROM test_table WHERE name = %s", ("Test",))
    print("PostgreSQL Fetched: ", cursor.fetchone())

    cursor.close()
    conn.close()

    elapsed = time.time() - start
    print(f"PostgreSQL action took {elapsed:.2f} seconds")
