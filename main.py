import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from orm_task import create_table, Publisher, Shop, Book, Stock, Sale


DSN = 'postgresql://postgres:76239@localhost:5432/netology_orm_test'
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