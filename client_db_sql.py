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
                email_address VARCHAR(90) UNIQUE,
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
    client_name = input("Input client's name: ")
    client_surname = input("Input client's surname: ")
    client_phone = input("Input client's phone number: ")
    client_email = input("Input client's email: ")
    client = Client(client_name, client_surname, client_phone, client_email)
    return client


def add_new_client(client_name, client_surname, client_phone, client_email):
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            values = ({'name': client_name, 'surname': client_surname})
            cur.execute("""
            INSERT INTO clients(name, surname)
            VALUES(%(name)s, %(surname)s)
            RETURNING id
            """, values)

            person_id = cur.fetchone()
            values = ({'phone_number': client_phone, 'client_id': person_id})

            cur.execute("""
            INSERT INTO phones(phone_number, client_id)
                VALUES(%(phone_number)s, %(client_id)s)
            """, values)

            values = ({'email_address': client_email, 'client_id': person_id})

            cur.execute("""
            INSERT INTO emails(email_address, client_id)
            VALUES(%(email_address)s, %(client_id)s)
            """, values)

            conn.commit()
    print('New client added.')


def add_phone():
    person_id = input("Please, input client's id number to add a phone number: ")
    new_phone_number = input("Input phone number you'd like to add: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            values = ({'phone_number': new_phone_number, 'client_id': person_id})

            cur.execute("""
            INSERT INTO phones(phone_number, client_id)
                VALUES(%(phone_number)s, %(client_id)s)
            """, values)
    print('Phone number added.')


def change_name():
    person_id = input("Please, input client's id number to change the name: ")
    name = input("Input the new name: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE clients SET name = %s WHERE id =%s"""
            cur.execute(name_change_query, (name, person_id))
            conn.commit()
            print('Name updated!')


def change_surname():
    person_id = input("Please, input client's id number to change the surname: ")
    surname = input("Input the new surname: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE clients SET surname = %s WHERE id =%s"""
            cur.execute(name_change_query, (surname, person_id))
            conn.commit()
            print('Surname updated!')


def change_email():
    person_id = input("Please, input client's id number to change the email: ")
    email = input("Input the new email: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE emails SET email_address = %s WHERE id =%s"""
            cur.execute(name_change_query, (email, person_id))
            conn.commit()
            print('Email updated!')


def change_phone():
    phone_id = input("Please, input phone's id to change the phone: ")
    phone = input("Input the new phone number: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE phones SET phone_number = %s WHERE id =%s"""
            cur.execute(name_change_query, (phone, phone_id))
            conn.commit()
            print('Phone number updated!')


def delete_phone():
    phone_id = input("Please, input phone's id to delete the phone: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            del_phone_query = """DELETE FROM phones WHERE id=%s"""
            cur.execute(del_phone_query, (phone_id,))
            conn.commit()
            print('Phone number deleted.')


def delete_client():
    client_id = input("Please, input client's id to delete: ")
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            del_phone_query = """DELETE FROM phones WHERE client_id=%s"""
            cur.execute(del_phone_query, (client_id,))
            del_email_query = """DELETE FROM emails WHERE client_id=%s"""
            cur.execute(del_email_query, (client_id,))
            del_client_query = """DELETE FROM clients WHERE id=%s"""
            cur.execute(del_client_query, (client_id,))
            conn.commit()
            print('Client deleted.')


def find_client():
    data = input("Please, input name, surname, phone or email to find the person: ")
    if data.isdigit():
        with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
            with conn.cursor() as cur:
                find_query = """
                SELECT * FROM clients
                JOIN emails ON clients.id = client_id
                JOIN phones ON clients.id = phones.client_id
                WHERE 
                phone_number = %s
                """
                cur.execute(find_query, (data,))
                print(cur.fetchall())
    else:
        with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
            with conn.cursor() as cur:
                find_query = """
                SELECT * FROM clients
                JOIN emails ON clients.id = client_id
                JOIN phones ON clients.id = phones.client_id
                WHERE 
                name = %s OR
                surname = %s OR
                email_address = %s
                """
                cur.execute(find_query, (data, data, data))
                print(cur.fetchall())


def user_help():
    print(
        'Список комманд:',
        '1 - добавить нового клиента в базу данных',
        '2 - добавить телефон существующему клиенту',
        '3 - изменить имя существующего клиента',
        '4 - изменить фамилию существующего клиента',
        '5 - изменить телефон существующего клиента',
        '6 - изменить адрес эл. почты существующего клиента',
        '7 - удалить телефон для существующего клиента',
        '8- удалить существующего клиента',
        '9 - найти клиента по его данным (имени, фамилии, email-у или телефону)',
        '0 - выведет список команд',
        '"q" - выход',
        sep='\n'
    )


def doomsday_book():
    create_db()
    user_help()
    while True:
        command = input('Введите вашу команду: ')
        if command == '1':
            new_client = create_new_client()
            add_new_client(new_client.name, new_client.surname, new_client.phone, new_client.email)
        elif command == '2':
            add_phone()
        elif command == '3':
            change_name()
        elif command == '4':
            change_surname()
        elif command == '5':
            change_phone()
        elif command == '6':
            change_email()
        elif command == '7':
            delete_phone()
        elif command == '8':
            delete_client()
        elif command == '9':
            find_client()
        elif command == '0':
            user_help()
        elif command == 'q':
            print('Выход')
            break


doomsday_book()
