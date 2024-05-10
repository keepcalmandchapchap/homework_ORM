import sqlalchemy as sq
from models_1 import Publisher, Shop, Book, Stock, Sale
from sqlalchemy.orm import sessionmaker

# 2 задача

driver = ''
user = ''
password = ''
connect = ''
port = ''
database = ''
DSN = f'{driver}://{user}:{password}@{connect}:{port}/{database}'

if __name__ == '__main__':
    search = input('Введите индетификатор или имя издателя: ')
    
    try:
        search = int(search)
    except:
        search = str(search)
    
    engine = sq.create_engine(DSN)
    Session = sessionmaker(engine)
    session = Session()

    if type(search) == int:
        for i in session.query(
            Book.title,
            Shop.name, 
            Sale.price, 
            Sale.date_sale
            ).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == search
            ).all():
            print(f'{i[0]} | {i[1]} | {i[2]} | {i[3].strftime('%d.%m.%Y')}')
    else:
        for i in session.query(
            Book.title,
            Shop.name, 
            Sale.price, 
            Sale.date_sale
            ).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == search
            ).all():
            print(f'{i[0]} | {i[1]} | {i[2]} | {i[3].strftime('%d.%m.%Y')}')

    session.close()
