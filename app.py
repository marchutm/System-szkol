from flask import Flask, render_template, request, redirect, url_for, session as login_session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import User

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Klucz do sesji

# Tworzymy silnik do obsługi bazy danych SQLite
engine = create_engine('sqlite:///users.db', echo=True)

# Tworzymy sesję do interakcji z bazą danych
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/users')
def users():
    if 'username' not in login_session:
        return redirect(url_for('index'))
    # Pobieramy wszystkich użytkowników z bazy danych
    users = session.query(User).all()

    return render_template('index.html', users=users)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in login_session:
        if login_session['role'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Sprawdzamy, czy użytkownik istnieje w bazie danych
        user = session.query(User).filter_by(email=email, password=password).first()

        if user:
            login_session['username'] = user.username
            login_session['role'] = user.role
            flash('Zalogowano pomyślnie!', 'success')  # Dodajemy wiadomość flash
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            flash('Niepoprawne dane logowania!', 'error')  # Dodajemy wiadomość flash
            return render_template('login.html')

    return render_template('login.html')


@app.route('/user/dashboard')
def user_dashboard():
    if 'username' not in login_session:
        return redirect(url_for('index'))
    if login_session.get('role') != 'user':
        return redirect(url_for('admin_dashboard'))
    return render_template('user_dashboard.html', username=login_session['username'])


@app.route('/admin/dashboard')
def admin_dashboard():
    if 'username' not in login_session:
        return redirect(url_for('index'))
    if login_session.get('role') != 'admin':
        return redirect(url_for('user_dashboard'))
    return render_template('admin_dashboard.html', username=login_session['username'])


@app.route('/logout')
def logout():
    login_session.clear()
    flash('Wylogowano pomyślnie!', 'success')  # Dodajemy wiadomość flash
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
