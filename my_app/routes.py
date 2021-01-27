from flask import render_template
from my_app import app
from .input_parser import parse
from .google_api import treat_geocoding_answer
from .wiki_api import wiki_process
from flask import jsonify
import os


GMAPS_KEY = os.environ['google_maps_key']
SENTENCES_FIRST_ANSWER = [""]
SENTENCES_AROUND = ["Je n'ai jamais été visiter cet endroit. Mais j'en connais des choses ! Par exemple, ", "", ""]
SENTENCES_PLACE = ["Je connais bien cet endroit ! Tiens par exemple, ", ]


def random_sentence():



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
        "first_sentence": first_sentence,
        "map": f"https://www.google.com/maps/embed/v1/place?key={GMAPS_KEY}&q={parsed}",
        "second_sentence": second_sentence,
        "wiki": wiki_answer
    })
