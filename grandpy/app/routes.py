import json
from flask import render_template, redirect
from flask.helpers import url_for
from app import app
from .input_parser import parse
from flask import jsonify


@app.route('/', methods=('GET', 'POST'))
@app.route('/home/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/ajax/<message>', methods=('GET', 'POST'))
def ajax(message):
    parsed = parse(message)
    return jsonify({
        "result": parsed
    })
