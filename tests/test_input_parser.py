from my_app.input_parser import cleaning
from my_app.input_parser import parse


def test_cleaning():
    """
    Testing the capability of the "cleaning" function to actually clean a sentence. 
    The punctuation has to be removed, except the apostrophe.
    """
    message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
    message_cleaned = cleaning(message)
    assert message_cleaned == "salut  je suis une phrase d exemple pour tester la fonction parser  voici une question   peux tu  s il te plait grandpy me donner l adresse du stade de france   merci  "



def test_parse():
    """
    Testing the capability of the "parse" function to separate the words of a sentence.
    The apostrophe has to be removed, and the words which contained one split and processed.
    """
    message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
    assert parse(message) == "donner+stade+france"
