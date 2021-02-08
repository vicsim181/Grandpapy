from flask import render_template
from my_app import app
from .parser import Parser
from .google_api import Googlemaps
from .wiki_api import Wikipedia
from flask import jsonify
import random


SENTENCES_FIRST_ANSWER = ["Et voilà l'adresse demandée en un temps record ! ",
                          "Et paf ! En un rien de temps je t'ai trouvé tout ça, voici l'adresse: ",
                          "Regarde ce que j'ai pour toi... Une adresse !! "]
SENTENCES_AROUND = ["Je n'ai jamais été visiter cet endroit. Mais j'en connais des choses ! Par exemple, ",
                    "Je dois bien avouer que je ne connais pas ce lieu, par contre je sais que ",
                    "Bon je dois bien avouer que je n'y suis jamais allé là-bas. Mais je suis déjà allé tout prêt ! Je sais tout de même que "]
SENTENCES_PLACE = ["Je connais bien cet endroit ! Tiens par exemple, ",
                   "Ah je me souviens j'y suis déjà allé ! Tu sais, ",
                   "Tiens d'ailleurs à propos de cet endroit que je connais bien, laisse moi te raconter que "]
ERROR_SENTENCES = ['Désolé mon petit je ne peux pas te répondre pour le moment !', "Tu m'excuses mais je n'ai pas la tête à répondre à tes questions !"]
googlemaps = Googlemaps()
wikipedia = Wikipedia()
parser = Parser()


def random_sentence(correspondence):
    """
    Depending on the correspondence results get from the Wikipedia class, we assign a sentence to the answer.
    If the wikipedia article doesn't match enough with the request, we send one of the SENTENCES_AROUND.
    If it matches enough, we wend one of the SENTENCES_PLACE.
    It also select a random sentence from the SENTENCES_FIRST_ANSWER to give as a direct answer when displaying the address.
    """
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
    """
    Display the home page of the website.
    """
    return render_template('home.html')


@app.route('/ajax/<message>', methods=('GET', 'POST'))
def ajax(message):
    """
    Called when an input is sent through the form on the main page.
    The function calls the differents classes linked to the needed APIs.
    Gives back the results obtained in a JSON file.
    """
    parsed_request = parser.parse(message)
    lat, lng = googlemaps.google_process(parsed_request)
    wiki_answer, correspondence = wikipedia.wiki_process(parsed_request, lat, lng)
    googlemaps.get_google_reverse_geocoding_answer(lat, lng)
    googlemaps.treat_reverse_geocoding()
    address = googlemaps.reverse_treated
    first_sentence, second_sentence = random_sentence(correspondence)
    return jsonify({
        "status": 1,
        "first_sentence": first_sentence,
        "address": address,
        "map": f"https://www.google.com/maps/embed/v1/place?key={Googlemaps.GMAPS_KEY_FRONT}&q={parsed_request}",
        "second_sentence": second_sentence,
        "wiki": wiki_answer
    })
