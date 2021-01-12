import json

keywords = {"adresse", "carte", "plan", "rue", "localisation", "endroit", "siège", "où se trouve"}

with open('D:/Github/P7/grandpy/app/stopwords.json', encoding='utf-8') as file:
    stopwords = json.load(file)
    # print(stopwords)


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
    return output
