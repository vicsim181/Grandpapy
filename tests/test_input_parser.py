from my_app.parser import Parser


class Test_parser():
    """
    Class holding the tests of the parser class.
    """
    def test_cleaning(self):
        """
        Testing the capability of the "cleaning" function to actually clean a sentence.
        The punctuation has to be removed, except the apostrophe.
        """
        parser_test = Parser()
        message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
        # message_cleaned = parser_test.cleaning(message)
        assert parser_test.cleaning(message) == 'salut  je suis une phrase d exemple pour tester la fonction parser  voici une question   peux tu  s il te plait grandpy me donner l adresse du stade de france   merci  '

    def test_parse(self):
        """
        Testing the capability of the "parse" function to separate the words of a sentence.
        The apostrophe has to be removed, and the words which contained one split and processed.
        """
        parser_test_2 = Parser()
        message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
        assert parser_test_2.parse(message) == "donner+stade+france"
