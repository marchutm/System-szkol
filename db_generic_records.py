from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import User  # Załóżmy, że nasza klasa User znajduje się w module o nazwie `your_module`

# Tworzymy silnik do obsługi bazy danych SQLite w pamięci
engine = create_engine('sqlite:///users.db', echo=True)

# Tworzymy sesję do interakcji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()

# Usuwanie wszystkich rekordów z tabeli users
if True:
    session.query(User).delete()

# Tworzymy trzy przykładowe rekordy
sample_users = [
    User(username='krzysztof', email='user1@example.com', first_name='Krzysztof',
         last_name='Nowak', password='password1', role='user', occupation='teacher', phone_number='123456789'),
    User(username='user2', email='user2@example.com', first_name='Anna',
         last_name='Kowalska', password='password2', role='user', occupation='teacher', phone_number='987654321'),
    User(username='user3', email='user3@example.com', first_name='Jan',
         last_name='Kowalski', password='password3', role='admin', occupation='teacher', phone_number='555666777'),
    User(username='user4', email='user4@example.com', first_name='Jan',
         last_name='Kowalski', password='password4', role='admin', occupation='teacher', phone_number='187654321'),
    User(username='user5', email='user5@example.com', first_name='Michał',
         last_name='Kowalski', password='password5', role='user', occupation='majster', phone_number='655666777'),
]

# Dodajemy rekordy do bazy danych
session.add_all(sample_users)
session.commit()

# Zamykamy sesję
session.close()
