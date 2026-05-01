import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5435",
    user="postgres_task",
    password="student",
    database="student"
)

cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM products;")
print(f"Всего товаров: {cur.fetchone()[0]}")

cur.close()
conn.close()