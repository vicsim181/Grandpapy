from my_app.google_api import get_google_geocoding_answer, treat_geocoding_answer


def mock_get_google_geocoding_answer(user_input):
    answer = {
        "results": [
            {
                "address_components": [
                    {
                        "long_name": "Saint-Denis",
                        "short_name": "Saint-Denis",
                        "types": [
                            "locality",
                            "political"
                        ]
                    },
                    {
                        "long_name": "Seine-Saint-Denis",
                        "short_name": "Seine-Saint-Denis",
                        "types": [
                            "administrative_area_level_2",
                            "political"
                        ]
                    },
                    {
                        "long_name": "Île-de-France",
                        "short_name": "IDF",
                        "types": [
                            "administrative_area_level_1",
                            "political"
                        ]
                    },
                    {
                        "long_name": "France",
                        "short_name": "FR",
                        "types": [
                            "country",
                            "political"
                        ]
                    },
                    {
                        "long_name": "93200",
                        "short_name": "93200",
                        "types": [
                            "postal_code"
                        ]
                    }
                ],
                "formatted_address": "93200 Saint-Denis, France",
                "geometry": {
                    "location": {
                        "lat": 48.9244592,
                        "lng": 2.3601645
                    },
                    "location_type": "GEOMETRIC_CENTER",
                    "viewport": {
                        "northeast": {
                            "lat": 48.9258081802915,
                            "lng": 2.361513480291502
                        },
                        "southwest": {
                            "lat": 48.92311021970851,
                            "lng": 2.358815519708498
                        }
                    }
                },
                "place_id": "ChIJv2Mi3bpu5kcREWMVCXFPwHA",
                "plus_code": {
                    "compound_code": "W9F6+Q3 Saint-Denis, France",
                    "global_code": "8FW4W9F6+Q3"
                },
                "types": [
                    "establishment",
                    "point_of_interest",
                    "stadium",
                    "tourist_attraction"
                ]
            }
        ],
        "status": "OK"
    }
    return answer


def test_google_api_geocoding_answer(monkeypatch):
    """
    Ici une réponse json simulée de la fonction interrogeant googlemaps est passée.
    On teste ici la fonction treat_google_answer() et le rendu à partir du json reçu.
    """
    result = treat_geocoding_answer('donner+adresse+stade+france')
    monkeypatch.setattr('my_app.google_api.get_google_geocoding_answer', mock_get_google_geocoding_answer)
    assert result == (48.9244592, 2.3601645)


def test_google_api_revers_answer():
    """
    Ici on simule la réponse de l'API de Google Maps en lui passant la longitude et latitude obtenue précédement.
    On teste le traitement qui sera fait de cette réponse.
    """
    pass
