#https://github.com/ODParkhomenko/SQL.-Homework-5-Python/blob/main/main.py
import psycopg2

def create_db(cur):

    cur.execute("DROP TABLE Client; DROP TABLE Phone;")

    cur.execute("""CREATE TABLE IF NOT EXISTS Client(
                client_id SERIAL  PRIMARY KEY,
                first_name VARCHAR(40) not null,
                last_name VARCHAR(40) not null,
                email VARCHAR(40) not null
            )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Phone(
                phone_id SERIAL  PRIMARY KEY,
                client_id Int foreign key references Client(Client_id),
                phone VARCHAR(40) not null
            )""")
    conn.commit()
conn.close()

def add_client(conn, first_name, last_name, email):
    cur.execute("""
    INSERT INTO Client(first_name, last_name, email) VALUES(%s, %s, %s);
    """, (first_name, last_name, email))


        conn.commit()
    conn.close()

add_client(conn = psycopg2.connect(database="netology_db", user="postgres", password="Zaq12wsxza!", first_name = "Vasya", Last_name = "Rogov", email=legion1983@narod.ru)


def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass



with psycopg2.connect(database="netology_db", user="postgres", password="Zaq12wsxza!") as conn:
    with conn.cursor() as cur:
        create_db(cur)


# with psycopg2.connect(database="clients_db", user="postgres", password="Zaq12wsxza!") as conn:
#     create_db(conn)
    pass  # вызывайте функции здесь

# conn.close()