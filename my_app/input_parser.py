import json

# keywords = {"mairie", "hôpital", "clinique", "pompiers", "commissariat", "stade", "école", "collège", "lycée", "université", "faculté",
#             "cinéma", "théâtre", "musée", "art", "histoire", "observatoire", "ambassade", "consulat", "restaurant", "bureau", "café",
#             "bar", "cabaret", "place", "parc", "archéologie", "zoologie", "architecture", "moderne", "contemporain"}


with open('my_app/stopwords.json', 'r', encoding='utf-8') as file:
    stopwords = json.load(file)


def cleaning(word):
    for forbidden_charac in "-',.;!?:(){\"":
        word = word.replace(forbidden_charac, " ")
    return word.lower()


def parse(sentence):
    sentence = sentence.strip()
    sentence_parsed = sentence.split()
    output = []
    for part in sentence_parsed:
        word = cleaning(part).strip()
        word_split = word.split()
        for element in word_split:
            if element not in stopwords and element not in (' ', ''):
                output.append(element)
    output = '+'.join(output)
    return str(output)


# print(parse("peut-être qu'il y a parfois trop de mots pour que la requête puisse fonctionner correctement !! Vérifions en ajoutant d'autres mots ?? , et de la ponctuation. Mais pour l'instant ça va mais on ne sait jamais, rajoutons-en plus encore !! AHAHA sait-on jamais si je cherche la Tour Eiffel "))
