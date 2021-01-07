import json

with open('app/stopwords.json', encoding='utf-8') as file:
    stopwords = json.load(file)
    print(stopwords)


def cleaning(word):
    for forbidden_charac in ",.;!?:(){\"":
        word = word.replace(forbidden_charac, ' ')
    return word.lower()


def parse(sentence):
    sentence = sentence.replace("'", ' ').strip()
    sentence_parsed = sentence.split()
    output = []
    for part in sentence_parsed:
        word = cleaning(part)
        if word not in stopwords:
            output.append(word)
    return output
