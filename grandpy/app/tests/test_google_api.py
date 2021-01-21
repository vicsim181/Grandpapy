from app.routes import ajax


def mock_parse():
    return 'donner+adresse+stade+france'


def test_google_api(monkeypatch):
    """
    Voir pour app.app_context() ou dans la doc flask pour testing flask.
    """
    monkeypatch.setattr('app.input_parser.parse', mock_parse)
    message = "Salut, je suis une phrase d'exemple pour tester la fonction parser. Voici une question : Peux-tu, s'il-te-plait Grandpy me donner l'adresse du Stade de France ? Merci !"
    assert ajax(message) == {"response": "https://www.google.com/maps/embed/v1/place?key=AIzaSyAstsdkCuu_k4i-V4ZNVW6WTZkYEeMvV1c&q=donner+adresse+stade+france"}
