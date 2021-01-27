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


# print(parse("Salut je veux l'adresse du roazhon park de Rennes stp"))
