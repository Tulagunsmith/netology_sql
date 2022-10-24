import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    books = relationship("Book", back_populates="publisher")

    def __str__(self):
        return f'Publisher {self.id}: {self.name}'


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    stocks = relationship("Stock", back_populates="shop")

    def __str__(self):
        return f'Shop {self.id}: {self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship("Publisher", back_populates="books")
    stocks = relationship("Stock", back_populates="book")

    def __str__(self):
        return f'Book {self.id}: {self.title}, {self.id_publisher}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship("Book", back_populates="stocks")
    shop = relationship("Shop", back_populates="stocks")
    sales = relationship("Sale", back_populates="stock")

    def __str__(self):
        return f'Stock {self.id}: {self.id_book}, {self.id_shop}, {self.count}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime, sq.ForeignKey("shop.id"), nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship("Stock", back_populates="sales")

    def __str__(self):
        return f'Stock {self.id}: {self.price}, {self.date_sale}, {self.id_stock}, {self.count}'


def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


