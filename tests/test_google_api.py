import json
from my_app.google_api import Googlemaps


class Test_Google_Maps():
    """
    Class holding the test functions about the GoogleMaps script (google_api.py).
    """
    def mock_get_google_geocoding_answer(self):
        with open('tests/maps_geocoding_mock.json', 'r', encoding='utf-8') as file:
            self.answer = json.load(file)

    def test_google_process(self):
        """
        In this test we use the fake json answer given by the mock_get_google_geocoding_answer function above.
        It replaces the answer we get from the GMaps API with the input of 'donner+adresse+stade+france'.
        We test the function treat_google_answer() which receives the json received from the API and its result.
        """
        googlemaps_test = Googlemaps()
        self.mock_get_google_geocoding_answer()
        googlemaps_test.result = self.answer
        result = googlemaps_test.treat_geocoding_answer()
        assert result == (48.9244592, 2.3601645)

    def mock_get_google_reverse_geocoding_answer(self):
        with open('tests/maps_reverse_geocoding_mock.json', 'r', encoding='utf-8') as file:
            self.reverse_answer = json.load(file)

    def test_treat_google_api_reverse(self):
        """
        In this function we test the 'get_google_reverse_geocoding_answer' from the Googlemaps class.
        """
        googlemaps_reverse = Googlemaps()
        self.mock_get_google_reverse_geocoding_answer()
        googlemaps_reverse.reverse = self.reverse_answer
        result = googlemaps_reverse.treat_reverse_geocoding()
        assert result == '360 Avenue du Président Wilson, 93200 Saint-Denis, France'
