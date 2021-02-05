import json


class Parser():
    """
    Class holding the parser.
    We give it the request the user typed in the input.
    The sentence is going to be treated to eliminate the punctuation, 'useless' words with the stopwords list.
    """

    with open('my_app/stopwords.json', 'r', encoding='utf-8') as file:
        STOPWORDS = json.load(file)

    def __init___(self):
        pass

    def cleaning(self, word):
        """
        Function cleaning a word, takes out the punctuation and replace it with a space.
        Puts the word in lower case.
        """
        for forbidden_charac in "-',.;!?:(){\"":
            word = word.replace(forbidden_charac, " ")
        self.word = word.lower()
        return self.word

    def parse(self, sentence):
        """
        This function uses the one above, to clean every word in the sentence passed in.
        It splits the sentence in words, clean them, and also eliminates the words that are present in the stopwords list.
        It adds a '+' around the words so the request is ready to be sent to the Google Maps API.
        """
        sentence = sentence.strip()
        sentence_parsed = sentence.split()
        output = []
        for part in sentence_parsed:
            self.cleaning(part)
            self.word.strip()
            word_split = self.word.split()
            for element in word_split:
                if element not in Parser.STOPWORDS and element not in (' ', ''):
                    output.append(element)
        output = '+'.join(output)
        return str(output)
