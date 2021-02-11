import json
from my_app.wiki_api import Wikipedia


class Test_wikipedia():
    """
    Class holding the tests of the wikipedia class in the wiki_api script.
    """
    def mock_get_wikipedia_geo_answer(self):
        with open('tests/wiki_geo_answer_mock.json', 'r', encoding='utf-8') as file:
            self.answer = json.load(file)

    def test_search_for_correspondence(self):
        """
        In this function we test the ability of the function to determine if wikipedia page matches with the request.
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
        with open('tests/wiki_explanations_mock.json', 'r', encoding='utf-8') as file:
            answer_2 = json.load(file)
        return answer_2

    def test_treat_explanation(self, monkeypatch):
        """
        In this test we use the fake json answer given by the mock_get_wiki_answer function above.
        We check that the function gives us back the first 5 sentences (max) of the description part of the article.
        We try with the answer related to the 'Stade de France' in Saint-Denis(93).
        """
        wiki_test = Wikipedia()
        self.mock_get_wikipedia_geo_answer()
        wiki_test.geo_result = self.answer
        monkeypatch.setattr('my_app.wiki_api.Wikipedia.get_wikipedia_explanation', self.mock_get_wikipedia_explanation)
        result = wiki_test.treat_explanation()
        assert result == """le Stade de France est le plus grand stade français avec 80 698 places en configuration football/rugby. Il se situe dans le quartier de la Plaine Saint-Denis à Saint-Denis, dans la proche banlieue nord de Paris. Il est l'œuvre de quatre architectes : Michel Macary, Aymeric Zublena, Michel Regembal et Claude Costantini. L'architecture de ce stade s'inspire du Worldport de la compagnie aérienne américaine Pan Am qui se situait à l'aéroport international John-F.-Kennedy de New York.
Il est inauguré le 28 janvier 1998 par Jacques Chirac, président de la République, lors du match de football France - Espagne."""
