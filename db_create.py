import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usuwamy starą bazę danych, jeśli istnieje
if os.path.exists("user.db"):
    os.remove("user.db")

# Tworzymy silnik do obsługi bazy danych SQLite w pamięci
engine = create_engine('sqlite:///users.db', echo=True)

# Deklarujemy bazę, do której będą przypisane nasze klasy
Base = declarative_base()


# Definiujemy klasę reprezentującą tabelę 'users'
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    second_name = Column(String, nullable=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)


# Tworzymy tabele w bazie danych
Base.metadata.create_all(engine)

# Tworzymy sesję do interakcji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()
