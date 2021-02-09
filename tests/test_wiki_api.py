from my_app.wiki_api import Wikipedia


class Test_wikipedia():
    """
    Class holding the tests of the wikipedia class in the wiki_api script.
    """
    def mock_get_wikipedia_geo_answer(self):
        self.answer = {
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

    def test_search_for_correspondence(self):
        """
        In this function we test the ability of the function to determine if the name of the wikipedia pages matches with the request.
        We need again the fake json result from the mock function above.
        We try here with the answer related to the 'Stade de France' in Saint-Denis(93).
        """
        wiki_test_2 = Wikipedia()
        request = 'donner+adresse+stade+france'
        self.mock_get_wikipedia_geo_answer()
        wiki_test_2.geo_result = self.answer
        result = wiki_test_2.search_for_correspondence(request)
        assert result == 1

    def mock_get_wikipedia_explanation(self):
        answer_2 = {
         'batchcomplete': '',
         'query': {'pages': {'62014': {'extract': 'Le Stade de France est le plus '
                                                 'grand stade français avec 80 698 '
                                                 'places en configuration '
                                                 'football/rugby. Il se situe dans le '
                                                 'quartier de la Plaine Saint-Denis à '
                                                 'Saint-Denis, dans la proche '
                                                 'banlieue nord de Paris. Il est '
                                                 "l'œuvre de quatre architectes : "
                                                 'Michel Macary, Aymeric Zublena, '
                                                 'Michel Regembal et Claude '
                                                 "Costantini. L'architecture de ce "
                                                 "stade s'inspire du Worldport de la "
                                                 'compagnie aérienne américaine Pan '
                                                 "Am qui se situait à l'aéroport "
                                                 'international John-F.-Kennedy de '
                                                 'New York.\n'
                                                 'Il est inauguré le 28 janvier 1998 '
                                                 'par Jacques Chirac, président de la '
                                                 'République, lors du match de '
                                                 'football France - Espagne.',
                                     'ns': 0,
                                     'pageid': 62014,
                                     'title': 'Stade de France'}}}}
        return answer_2

    def test_treat_explanation(self, monkeypatch):
        """
        In this test we use the fake json answer given by the mock_get_wiki_answer function above.
        We are going to check that the function gives us back the first 5 sentences (or less) of the description part of the article.
        We try with the answer related to the 'Stade de France' in Saint-Denis(93).
        """
        wiki_test = Wikipedia()
        self.mock_get_wikipedia_geo_answer()
        wiki_test.geo_result = self.answer
        monkeypatch.setattr('my_app.wiki_api.Wikipedia.get_wikipedia_explanation', self.mock_get_wikipedia_explanation)
        result = wiki_test.treat_explanation()
        assert result == """le Stade de France est le plus grand stade français avec 80 698 places en configuration football/rugby. Il se situe dans le quartier de la Plaine Saint-Denis à Saint-Denis, dans la proche banlieue nord de Paris. Il est l'œuvre de quatre architectes : Michel Macary, Aymeric Zublena, Michel Regembal et Claude Costantini. L'architecture de ce stade s'inspire du Worldport de la compagnie aérienne américaine Pan Am qui se situait à l'aéroport international John-F.-Kennedy de New York.
Il est inauguré le 28 janvier 1998 par Jacques Chirac, président de la République, lors du match de football France - Espagne."""
