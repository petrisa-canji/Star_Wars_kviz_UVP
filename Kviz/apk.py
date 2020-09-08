from bottle import run, route, template, static_file, redirect, request
import json
from modul import Model, mejava_osebnost_junak

model = Model()


@route('/')
def index():
    return template('static/kviz.html')

@route('/pravila')
def pravila():
    return template('static/kviz-pravila.html')

@route('/kviz')
def kviz():
    redirect(f'/vprasanje/0')

@route('/vprasanje/<id>')
def vprasanje(id):
    id = int(id)
    q = model.seznam_vprasanj[id]["vprasanje"]

    return template('static/vprasanja.html', id=id, text=q)

@route('/submit', method='POST')
def submit():
    id = int(request.forms.get('question'))
    odgovor = int(request.forms.get('answer'))
    rezultat_odgovora = model.seznam_vprasanj[id]["mozni odgovori"][odgovor]

    model.seznam_odgovorov += rezultat_odgovora

    id += 1

    if id == len(model.seznam_vprasanj):

        return template('static/konec.html')
    else:
        redirect('/vprasanje/{id}'.format(id=id))

@route('/rezultati')
def rezultati():
    odgovori = model.seznam_odgovorov
    model.reset_odgovorov()
    model.update_seznam_vprasanj()

    možnosti = set(odgovori)
    rezultati = [[i, odgovori.count(i)] for i in možnosti]
    rezultati = sorted(rezultati, key=lambda x: x[1], reverse=True)
    rezultati = mejava_osebnost_junak(rezultati)

    return template('static/rezultati.html', rezultati=rezultati)

    

if __name__ == '__main__':
    run(debug=True,reloder=True)