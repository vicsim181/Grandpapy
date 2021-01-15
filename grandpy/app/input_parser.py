import json
import spacy

nlp = spacy.load('fr_core_news_sm')
doc = nlp("Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?")


keywords = {"mairie", "hôpital", "clinique", "pompiers", "commissariat", "stade", "école", "collège", "lycée", "université", "faculté",
            "cinéma", "théâtre", "musée", "art", "histoire", "observatoire", "ambassade", "consulat", "restaurant", "bureau", "café",
            "bar", "cabaret", "place", "parc", "archéologie", "zoologie", "architecture", "moderne", "contemporain"}


with open('D:/Github/P7/grandpy/app/stopwords.json', encoding='utf-8') as file:
    stopwords = json.load(file)


def cleaning(word):
    for forbidden_charac in "-,.;!?:(){\"":
        word = word.replace(forbidden_charac, " ")
    return word.lower()


def parse(sentence):
    sentence = sentence.replace("'", ' ').strip()
    sentence_parsed = sentence.split()
    output = []
    for part in sentence_parsed:
        word = cleaning(part).strip()
        word_split = word.split()
        for element in word_split:
            if element not in stopwords and element not in (' ', ''):
                output.append(element)
    output = ' '.join(output)
    return str(output)


def essai_spacy():
    # doc = nlp(parse("Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"))
    print(doc)
    for token in doc:
        if not token.is_stop:
            print(token.text)
    for ent in doc.ents:
        print(ent.text, ent.label_)


# parse("peut-être qu'il y a parfois trop de mots pour que la requête puisse fonctionner correctement !! Vérifions en ajoutant d'autres mots ?? , et de la ponctuation. Mais pour l'instant ça va mais on ne sait jamais, rajoutons-en plus encore !! AHAHA sait-on jamais si je cherche la Tour Eiffel ")
# parse("Les adresses c'est vraiment très intéressant comme l'est le football par exemple avec Santiago Bernabeu à Madrid en Espagne")
# print(get_request("Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie"))
