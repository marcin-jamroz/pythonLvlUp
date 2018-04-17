# app.py
from flask import Flask, request, Response, redirect, url_for, render_template, jsonify
import uuid
from collections import OrderedDict

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

users = {'Akwarysta69': ['J3si07r', False]}
fishes = {}


def isLogged():
    auth = request.authorization
    global users
    try:
        if auth['password'] == users.get(auth['username'], [0])[0] and users.get(auth['username'], [0, False])[1] == True:
            return True
        else:
            return False
    except TypeError:
        return False


@app.route('/')
def show_rybki():
    return 'Tutaj są rybki'


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    global users
    try:
        if auth['password'] == users.get(auth['username'], [0])[0]:
            users[auth['username']][1] = True
            return redirect(url_for('hello'))
        else:
            return Response('Błąd autoryzacji', 401)
    except TypeError:
        return Response('Błąd autoryzacji', 401)


@app.route('/logout', methods=['POST'])
def logout():
    if isLogged():
        auth = request.authorization
        users[auth['username']][1] = False
        return 'Wylogowano'
    else:
        return Response('Błąd autoryzacji', 401)


@app.route('/hello')  # domyślnie get
def hello():
    if isLogged():
        greeting = request.authorization['username']
        return render_template(
            'hello_tmpl.html',
            id=greeting
        )
    else:
        return Response('Błąd autoryzacji', 401)


@app.route("/fishes", methods=['GET', 'POST'])
def dec_fishes():
    if isLogged():
        if request.args.get('format', 0) == "json":
            if request.method == 'GET':
                global fishes
                ordered_fishes = OrderedDict(sorted(fishes.items()))
                return jsonify(ordered_fishes)
            elif request.method == 'POST':
                data = request.get_json(force=True)
                fishes[str(uuid.uuid4())] = data
                return 'Zapisano'
        else:
            return Response('Bad request', 400)
    else:
        return Response('Błąd autoryzacji', 401)


@app.route('/fishes/<id>', methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def change_fish(id):
    if isLogged():
        if request.args.get('format', 0) == "json":
            if request.method == 'GET':
                global fishes
                try:
                    return jsonify(fishes[id])
                except KeyError:
                    return Response('Brak identyfikatora w bazie', 404)
            elif request.method == 'DELETE':
                try:
                    del fishes[id]
                except KeyError:
                    return Response('Brak identyfikatora w bazie', 404)
                return 'Usunięto rybkę'
            elif request.method == 'PUT':
                data = request.get_json(force=True)
                try:
                    fishes[id] = data
                except KeyError:
                    return Response('Brak identyfikatora w bazie', 404)
                return 'Podmieniono rybkę'
            elif request.method == 'PATCH':
                data = request.get_json(force=True)
                try:
                    for key, value in data.items():
                        fishes[id][key] = value
                except KeyError:
                    return Response('Brak identyfikatora w bazie', 404)
                return 'Zmieniono rybkę'
        else:
            return Response('Bad request', 400)
    else:
        return Response('Błąd autoryzacji', 401)


if __name__ == '__main__':
    app.run(debug=True)
