import psycopg2


def create_db():
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            cur.execute("""
            DROP TABLE IF EXISTS 
            phones,
            emails,
            clients
            CASCADE
            """)

            cur.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                id SERIAL PRIMARY KEY,
                name VARCHAR(60),
                surname VARCHAR(60)
            );
            """)

            cur.execute("""
            CREATE TABLE IF NOT EXISTS phones(
                id SERIAL PRIMARY KEY, 
                phone_number NUMERIC(11) UNIQUE,
                client_id INTEGER NOT NULL REFERENCES clients(id)
            );
            """)

            cur.execute("""
            CREATE TABLE IF NOT EXISTS emails(
                id SERIAL PRIMARY KEY,
                email_adress VARCHAR(90) UNIQUE,
                client_id INTEGER NOT NULL REFERENCES clients(id)
            );
            """)

            conn.commit()
    print('Database created.')
    return


class Client:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        client_data = (f'Name: {self.name}\n'
                       f'Surname: {self.surname}\n'
                       f'Phone: {self.phone}\n'
                       f'Email: {self.email}\n')
        return client_data


def create_new_client():
    client_name = input('Input client name: ')
    client_surname = input('Input client surname: ')
    client_phone = input('Input client phone number: ')
    client_email = input('Input client email: ')
    new_client = Client(client_name, client_surname, client_phone, client_email)
    return new_client

    # cur.execute("""
    # INSERT INTO clients(name, surname)
    # VALUES('Alexey', 'Sergeev'),
    # ('Natasha', 'Chesnokova')
    # """)
    #
    # cur.execute("""
    # INSERT INTO phones(phone_number, client_id)
    #     VALUES('89066200669', 1),
    #     ('89520167374', 1),
    #     ('89301785144', 2)
    # """)
    #
    # cur.execute("""
    # INSERT INTO emails(email_adress, client_id)
    # VALUES('someadress@mail.ru', 1),
    # ('anotheradress@rambler.ru', 2)
    # """)
    #
    # conn.commit()
