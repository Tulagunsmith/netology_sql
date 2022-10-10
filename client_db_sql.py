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
    client_name = input('Input client name: ')
    client_surname = input('Input client surname: ')
    client_phone = input('Input client phone number: ')
    client_email = input('Input client email: ')
    client = Client(client_name, client_surname, client_phone, client_email)
    return client


# new_client = create_new_client()


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


# create_db()
# add_new_client(new_client.name, new_client.surname, new_client.phone, new_client.email)


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


# def change_name():
#     change_data = input("""
#     What would you like to change? Press 'p' for phone,
#     'e' for email, 'n' for name or 's' for surname
#     """)
#     with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
#         with conn.cursor() as cur:
#             values = ({f'{change_data}': old_name})
#
#             cur.execute("""
#             SELECT name FROM clients(phone_number, client_id)
#                 VALUES(%(phone_number)s, %(client_id)s)
#             """, values)


class NewData:
    def __init__(self):
        self.old_data = ''
        self.table = ''
        self.new_data = ''


def change_name(name, person_id):
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE clients SET name = %s WHERE id =%s"""
            cur.execute(name_change_query, (name, person_id))
            conn.commit()
            print('Name updated!')


def change_surname(surname, person_id):
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE clients SET surname = %s WHERE id =%s"""
            cur.execute(name_change_query, (surname, person_id))
            conn.commit()
            print('Surname updated!')


def change_email(email, person_id):
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE emails SET email_address = %s WHERE id =%s"""
            cur.execute(name_change_query, (email, person_id))
            conn.commit()
            print('Email updated!')


def change_phone(phone, phone_id):
    with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
        with conn.cursor() as cur:
            name_change_query = """UPDATE phones SET phone_number = %s WHERE id =%s"""
            cur.execute(name_change_query, (phone, phone_id))
            conn.commit()
            print('Phone number updated!')


# def change_phone2(phone, phone_id):
#     name_change_query = """UPDATE phones SET phone_number = %s WHERE id =%s"""
#     cur.execute(name_change_query, (phone, phone_id))
#     conn.commit()
#     print('Phone number updated!')
#
#
# with psycopg2.connect(database='netology_client_db', user="postgres", password="76239") as conn:
#     with conn.cursor() as cur:
#         change_phone2(97794444589, 4)
#         print('Jeronimo!')

