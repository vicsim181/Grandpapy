from flask import render_template
from my_app import app
from .input_parser import parse
from .google_api import treat_geocoding_answer
from .wiki_api import wiki_process
from flask import jsonify
import os
import random


GMAPS_KEY = os.environ['google_maps_key']
SENTENCES_FIRST_ANSWER = ["Et voilà l'adresse demandée en un temps record !",
                          "Et paf ! En un rien de temps je t'ai trouvé tout ça, voici l'adresse ",
                          "Regarde ce que j'ai pour toi... Une adresse !! "]
SENTENCES_AROUND = ["Je n'ai jamais été visiter cet endroit. Mais j'en connais des choses ! Par exemple, ",
                    "Je dois bien avouer que je ne connais pas ce lieu, par contre je sais que ",
                    "Bon je dois bien avouer que je n'y suis jamais allé là-bas. Mais je suis déjà allé tout prêt ! Je sais tout de même que "]
SENTENCES_PLACE = ["Je connais bien cet endroit ! Tiens par exemple, ",
                   "Ah je me souviens quand j'y suis déjà allé ! Tu sais, ",
                   "Tiens d'ailleurs à propos de cet endroit que je connais bien, laisse moi te raconter que "]


def random_sentence(correspondence):
    first_sentence = random.choice(SENTENCES_FIRST_ANSWER)
    if correspondence == 1:
        second_sentence = random.choice(SENTENCES_PLACE)
        return first_sentence, second_sentence
    else:
        second_sentence = random.choice(SENTENCES_AROUND)
        return first_sentence, second_sentence


@app.route('/', methods=('GET', 'POST'))
@app.route('/home/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/ajax/<message>', methods=('GET', 'POST'))
def ajax(message):
    parsed_request = parse(message)
    lat, lng = treat_geocoding_answer(parsed_request)
    wiki_answer, correspondence = wiki_process(parsed_request, lat, lng)
    first_sentence, second_sentence = random_sentence(correspondence)
    return jsonify({
        "first_sentence": first_sentence,
        "map": f"https://www.google.com/maps/embed/v1/place?key={GMAPS_KEY}&q={parsed_request}",
        "second_sentence": second_sentence,
        "wiki": wiki_answer
    })
