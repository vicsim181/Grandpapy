import sys
sys.path.append('..')
from input_parser import cleaning as cleaning
from input_parser import parse as parse


# Testing the capability of the "cleaning" function to actually clean a sentence. 
# The punctuation has to be removed, except the apostrophe.
def test_cleaning():
    message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
    message_cleaned = cleaning(message)
    assert message_cleaned == "salut  je suis une phrase d'exemple pour tester la fonction parser  voici une question   peux tu  s'il te plait grandpy me donner l'adresse du stade de france   merci  "


# Testing the capability of the "parse" function to separate the words of a sentence.
# The apostrophe has to be removed, and the words which contained one split and processed.
def test_parse():
    message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
    assert parse(message) == ["donner", "adresse", "stade", "france"]
