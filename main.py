import os
import sqlalchemy as sq
import json
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from orm_task import create_table, Publisher, Shop, Book, Stock, Sale


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

database = os.getenv('DATABASE')
user = os.getenv('USER')
password = os.getenv('PASSWORD')


DSN = f'postgresql://{user}:{password}@localhost:5432/{database}'
engine = sq.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()


def fill_bd():
    with open('fixtures.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


def print_publisher():
    user_data = input('Enter publisher name or id number: ')
    if user_data.isdigit():
        for c in session.query(Publisher).filter(Publisher.id == user_data).all():
            print(c)
    else:
        for c in session.query(Publisher).filter(Publisher.name == user_data).all():
            print(c)


if __name__ == "__main__":
    create_table(engine)
    fill_bd()
    print_publisher()

