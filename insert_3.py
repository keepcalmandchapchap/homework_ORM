import sqlalchemy as sq
import json
from sqlalchemy.orm import sessionmaker
from models_1 import create_tables, Publisher, Shop, Book, Stock, Sale

#Доп.задача

driver = ''
user = ''
password = ''
connect = ''
port = ''
database = ''
DSN = f'{driver}://{user}:{password}@{connect}:{port}/{database}'


if __name__ == '__main__':    
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open('data.json', 'r') as f:
        data = json.load(f)

    for d in data:
        model = d['model']
        if model == 'publisher':
            new_publisher = Publisher(id=d['pk'], 
                                      name=d['fields']['name'])
            session.add(new_publisher)
        if model == 'book':
            new_book = Book(id=d['pk'], 
                            title=d['fields']['title'], 
                            id_publisher=d['fields']['id_publisher'])
            session.add(new_book)
        if model == 'shop':
            new_shop = Shop(id=d['pk'], 
                            name=d['fields']['name'])
            session.add(new_shop)
        if model == 'stock':
            new_stock = Stock(id=d['pk'], 
                              id_book=d['fields']['id_book'], 
                              id_shop=d['fields']['id_shop'], 
                              count=d['fields']['count'])
            session.add(new_stock)
        if model == 'sale':
            new_sale = Sale(id=d['pk'],
                             price=d['fields']['price'], 
                             date_sale=d['fields']['date_sale'], 
                             id_stock=d['fields']['id_stock'], 
                             count=d['fields']['count'])
            session.add(new_sale)
        session.commit()


    session.close()


