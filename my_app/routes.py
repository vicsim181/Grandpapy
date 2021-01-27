from flask import render_template
from my_app import app
from .input_parser import parse
from .google_api import treat_geocoding_answer
from .wiki_api import wiki_process
from flask import jsonify
import os


gmaps_key = os.environ['google_maps_key']


@app.route('/', methods=('GET', 'POST'))
@app.route('/home/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/ajax/<message>', methods=('GET', 'POST'))
def ajax(message):
    parsed = parse(message)
    lat, lng = treat_geocoding_answer(parsed)
    wiki_answer = wiki_process(lat, lng)
    return jsonify({
        "map": f"https://www.google.com/maps/embed/v1/place?key={gmaps_key}&q={parsed}",
        "wiki": wiki_answer
    })
