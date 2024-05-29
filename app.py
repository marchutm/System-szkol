from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import User

app = Flask(__name__)

# Tworzymy silnik do obsługi bazy danych SQLite w pamięci
engine = create_engine('sqlite:///users.db', echo=True)

# Tworzymy sesję do interakcji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/users')
def users():
    # Pobieramy wszystkich użytkowników z bazy danych
    users = session.query(User).all()

    return render_template('index.html', users=users)


@app.route('/')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
