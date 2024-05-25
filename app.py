from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import User  

app = Flask(__name__)

# Tworzymy silnik do obsługi bazy danych SQLite w pamięci
engine = create_engine('sqlite:///users.db', echo=True)

# Tworzymy sesję do interakcji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def index():
    # Pobieramy wszystkich użytkowników z bazy danych
    users = session.query(User).all()

    # Tworzymy listę stringów reprezentujących użytkowników i ich maile
    user_info = [f"Username: {user.username}, Email: {user.email}\n" for user in users]

    # Łączymy stringi w jeden tekst, oddzielając je nową linią
    users_text = ''.join(user_info)

    return users_text


if __name__ == '__main__':
    app.run(debug=True)
