from my_app.wiki_api import search_for_element_to_display


def mock_get_wiki_answer(input_request):
    answer = {
        "batchcomplete": "",
        "query": {
            "geosearch": [
                {
                    "pageid": 62014,
                    "ns": 0,
                    "title": "Stade de France",
                    "lat": 48.924444,
                    "lon": 2.36,
                    "dist": 12.1,
                    "primary": ""
                },
                {
                    "pageid": 12548608,
                    "ns": 0,
                    "title": "Avenue Jules-Rimet",
                    "lat": 48.924537,
                    "lon": 2.362539,
                    "dist": 173.7,
                    "primary": ""
                },
                {
                    "pageid": 13241805,
                    "ns": 0,
                    "title": "Centre aquatique olympique (Paris)",
                    "lat": 48.923583,
                    "lon": 2.355333,
                    "dist": 366.2,
                    "primary": ""
                },
                {
                    "pageid": 10864756,
                    "ns": 0,
                    "title": "Piscine olympique de Saint-Denis",
                    "lat": 48.9238667,
                    "lon": 2.3548667,
                    "dist": 392.6,
                    "primary": ""
                },
                {
                    "pageid": 29554,
                    "ns": 0,
                    "title": "Groupe Afnor",
                    "lat": 48.92028,
                    "lon": 2.3611,
                    "dist": 469.7,
                    "primary": ""
                },
                {
                    "pageid": 854957,
                    "ns": 0,
                    "title": "Agence nationale d'accréditation et d'évaluation en santé",
                    "lat": 48.920278,
                    "lon": 2.361944,
                    "dist": 482.8,
                    "primary": ""
                }
            ]
        }
    }
    return answer


def test_treatment_wiki_answer_to_decide_which_element_to_display(monkeypatch):
    """
    In this test we use the fake json answer given by the mock_get_google_geocoding_answer function above.
    Ici on va récupérer la réponse ci-dessus pour simuler la réponse de l'API de wikipédia avec une recherche
    via les coordonnées du Stade de France à Saint-Denis(93).
    """
    request = 'donner+adresse+stade+france'
    answer = mock_get_wiki_answer(request)
    monkeypatch.setattr('my_app.wiki_api.get_wiki_answer', mock_get_wiki_answer)
    result = search_for_element_to_display(request, answer)
    assert result == ('Stade de France', 12.1)
