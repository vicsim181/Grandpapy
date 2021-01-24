import json
from flask import render_template
from flask.helpers import url_for
from my_app import app
from .input_parser import parse
from flask import jsonify
import os


gmaps_key = os.environ['google_maps_key']


@app.route('/', methods=('GET', 'POST'))
@app.route('/home/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/ajax/<message>', methods=('GET', 'POST'))
def ajax(message):
    print(str(message))
    parsed = parse(message)
    return jsonify({
        "response": f"https://www.google.com/maps/embed/v1/place?key={gmaps_key}&q={parsed}"
    })
