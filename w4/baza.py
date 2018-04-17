import sqlite3
from flask import g, Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/films')
def films_list():
    db = get_db()
    #cursor = db.cursor()
    #cursor.execute('SELECT title FROM film')
    #data = cursor.fetchall()
    data = db.execute('SELECT title from film').fetchall()
    return render_template('film_title_template.html', films=data)

@app.route('/films/<int:film_id>')
def single_film(film_id):
    db = get_db()
    #data = db.execute('SELECT title, release_year, description FROM film WHERE film_id = ?',
    #                  (film_id,)).fetchone()
    data = db.execute('SELECT title, release_year, description FROM film WHERE film_id = :film_id',
                      {'film_id': film_id}).fetchone()
    return render_template('film_template.html', film=data)

@app.route('/films_with_category')
def films_with_category_list():
    db = get_db()
    data = db.execute('''
    SELECT title, name FROM film
    JOIN film_category ON film.film_id = film_category.film_id
    JOIN category ON film_category.category_id = category.category_id;
    ''').fetchall()
    return render_template('film_category_template.html', films=data)

@app.route('/actors')
def actors_list():
    db = get_db()
    data = db.execute('SELECT first_name, last_name FROM actor').fetchall()
    return render_template('actors_template.html', actors=data)

@app.route('/actors/add', methods=['GET', 'POST'])
def add_actor_version_1():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        db = get_db()
        db.execute('INSERT INTO actor (first_name, last_name) VALUES (?, ?)',
                   (first_name, last_name))
        db.commit()
        return redirect(url_for('actors_list'))
    else:
        return render_template('actors_form.html')

if __name__ == '__main__':
    app.run(debug=True)