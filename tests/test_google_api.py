from my_app.google_api import Googlemaps


class Test_Google_Maps():
    """
    Class holding the test functions about the GoogleMaps script (google_api.py).
    """
    def mock_get_google_geocoding_answer(self, user_input):
        self.answer = {
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

    def test_google_process(self, monkeypatch):
        """
        In this test we use the fake json answer given by the mock_get_google_geocoding_answer function above.
        It replaces the answer we get from the GMaps API with the input of 'donner+adresse+stade+france'.
        We test the function treat_google_answer() which receives the json received from the API and the result it gives us.
        """
        googlemaps_test = Googlemaps()
        user_input = 'donner+stade+france'
        monkeypatch.setattr('my_app.google_api.Googlemaps.get_google_geocoding_answer',
                            self.mock_get_google_geocoding_answer)
        result = googlemaps_test.google_process(user_input)
        assert result == (48.9244592, 2.3601645)

    def mock_get_google_reverse_geocoding_answer(self, lat, lng):
        reverse_answer = {'plus_code': {'compound_code': 'W9F6+Q3 Saint-Denis, France',
                                'global_code': '8FW4W9F6+Q3'},
                  'results': [{'address_components': [{'long_name': '360',
                                                    'short_name': '360',
                                                    'types': ['street_number']},
                                                    {'long_name': 'Avenue du Président Wilson',
                                                    'short_name': 'Avenue du Président '
                                                                    'Wilson',
                                                    'types': ['route']},
                                                    {'long_name': 'Saint-Denis',
                                                    'short_name': 'Saint-Denis',
                                                    'types': ['locality', 'political']},
                                                    {'long_name': 'Seine-Saint-Denis',
                                                    'short_name': 'Seine-Saint-Denis',
                                                    'types': ['administrative_area_level_2',
                                                                'political']},
                                                    {'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']},
                                                    {'long_name': '93200',
                                                    'short_name': '93200',
                                                    'types': ['postal_code']}],
                            'formatted_address': '360 Avenue du Président Wilson, 93200 '
                                                'Saint-Denis, France',
                            'geometry': {'location': {'lat': 48.9248163, 'lng': 2.3612796},
                                        'location_type': 'ROOFTOP',
                                        'viewport': {'northeast': {'lat': 48.92616528029149,
                                                                    'lng': 2.362628580291502},
                                                        'southwest': {'lat': 48.92346731970849,
                                                                    'lng': 2.359930619708498}}},
                            'place_id': 'ChIJP4OczLpu5kcRB_UFOOkFhdc',
                            'plus_code': {'compound_code': 'W9F6+WG Saint-Denis, France',
                                            'global_code': '8FW4W9F6+WG'},
                            'types': ['street_address']},
                            {'address_components': [{'long_name': '21',
                                                    'short_name': '21',
                                                    'types': ['street_number']},
                                                    {'long_name': 'Avenue Jules Rimet',
                                                    'short_name': 'Avenue Jules Rimet',
                                                    'types': ['route']},
                                                    {'long_name': 'Saint-Denis',
                                                    'short_name': 'Saint-Denis',
                                                    'types': ['locality', 'political']},
                                                    {'long_name': 'Seine-Saint-Denis',
                                                    'short_name': 'Seine-Saint-Denis',
                                                    'types': ['administrative_area_level_2',
                                                                'political']},
                                                    {'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']},
                                                    {'long_name': '93200',
                                                    'short_name': '93200',
                                                    'types': ['postal_code']}],
                            'formatted_address': '21 Avenue Jules Rimet, 93200 Saint-Denis, '
                                                'France',
                            'geometry': {'location': {'lat': 48.9246598, 'lng': 2.3625342},
                                        'location_type': 'RANGE_INTERPOLATED',
                                        'viewport': {'northeast': {'lat': 48.9260087802915,
                                                                    'lng': 2.363883180291502},
                                                        'southwest': {'lat': 48.9233108197085,
                                                                    'lng': 2.361185219708498}}},
                            'place_id': 'EjAyMSBBdmVudWUgSnVsZXMgUmltZXQsIDkzMjAwIFNhaW50LURlbmlzLCBGcmFuY2UiGhIYChQKEgkBAWQ8pW7mRxEAMDU0Rg3V9hAV',
                            'types': ['street_address']},
                            {'address_components': [{'long_name': '23',
                                                    'short_name': '23',
                                                    'types': ['street_number']},
                                                    {'long_name': 'Avenue Jules Rimet',
                                                    'short_name': 'Avenue Jules Rimet',
                                                    'types': ['route']},
                                                    {'long_name': 'Saint-Denis',
                                                    'short_name': 'Saint-Denis',
                                                    'types': ['locality', 'political']},
                                                    {'long_name': 'Seine-Saint-Denis',
                                                    'short_name': 'Seine-Saint-Denis',
                                                    'types': ['administrative_area_level_2',
                                                                'political']},
                                                    {'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']},
                                                    {'long_name': '93200',
                                                    'short_name': '93200',
                                                    'types': ['postal_code']}],
                            'formatted_address': '23 Avenue Jules Rimet, 93200 Saint-Denis, '
                                                'France',
                            'geometry': {'bounds': {'northeast': {'lat': 48.9245531,
                                                                    'lng': 2.362558},
                                                    'southwest': {'lat': 48.9243326,
                                                                    'lng': 2.3625436}},
                                        'location': {'lat': 48.9244429, 'lng': 2.3625508},
                                        'location_type': 'GEOMETRIC_CENTER',
                                        'viewport': {'northeast': {'lat': 48.9257918302915,
                                                                    'lng': 2.363899780291502},
                                                        'southwest': {'lat': 48.9230938697085,
                                                                    'lng': 2.361201819708498}}},
                            'place_id': 'ChIJNwQ5I6Vu5kcRUHkXuRAla1g',
                            'types': ['route']},
                            {'address_components': [{'long_name': '93200',
                                                    'short_name': '93200',
                                                    'types': ['postal_code']},
                                                    {'long_name': 'Saint-Denis',
                                                    'short_name': 'Saint-Denis',
                                                    'types': ['locality', 'political']},
                                                    {'long_name': 'Seine-Saint-Denis',
                                                    'short_name': 'Seine-Saint-Denis',
                                                    'types': ['administrative_area_level_2',
                                                                'political']},
                                                    {'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']}],
                            'formatted_address': '93200 Saint-Denis, France',
                            'geometry': {'bounds': {'northeast': {'lat': 48.9520351,
                                                                    'lng': 2.398495},
                                                    'southwest': {'lat': 48.9014716,
                                                                    'lng': 2.3331928}},
                                        'location': {'lat': 48.9315523, 'lng': 2.3563278},
                                        'location_type': 'APPROXIMATE',
                                        'viewport': {'northeast': {'lat': 48.9520351,
                                                                    'lng': 2.398495},
                                                        'southwest': {'lat': 48.9014716,
                                                                    'lng': 2.3331928}}},
                            'place_id': 'ChIJ1VCQXa9u5kcRkIPY4caCCxw',
                            'types': ['postal_code']},
                            {'address_components': [{'long_name': 'Saint-Denis',
                                                     'short_name': 'Saint-Denis',
                                                     'types': ['locality', 'political']},
                                                    {'long_name': 'Seine-Saint-Denis',
                                                     'short_name': 'Seine-Saint-Denis',
                                                     'types': ['administrative_area_level_2',
                                                               'political']},
                                                    {'long_name': 'Île-de-France',
                                                     'short_name': 'IDF',
                                                     'types': ['administrative_area_level_1',
                                                               'political']},
                                                    {'long_name': 'France',
                                                     'short_name': 'FR',
                                                     'types': ['country', 'political']}],
                            'formatted_address': 'Saint-Denis, France',
                            'geometry': {'bounds': {'northeast': {'lat': 48.952109,
                                                                  'lng': 2.3981399},
                                                    'southwest': {'lat': 48.90148199999999,
                                                                  'lng': 2.333227}},
                                        'location': {'lat': 48.936181, 'lng': 2.357443},
                                        'location_type': 'APPROXIMATE',
                                        'viewport': {'northeast': {'lat': 48.952109,
                                                                   'lng': 2.3981399},
                                                        'southwest': {'lat': 48.90148199999999,
                                                                   'lng': 2.333227}}},
                            'place_id': 'ChIJYW0056pu5kcRDeko-brr78c',
                            'types': ['locality', 'political']},
                            {'address_components': [{'long_name': 'Seine-Saint-Denis',
                                                    'short_name': 'Seine-Saint-Denis',
                                                    'types': ['administrative_area_level_2',
                                                                'political']},
                                                    {'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']}],
                            'formatted_address': 'Seine-Saint-Denis, France',
                            'geometry': {'bounds': {'northeast': {'lat': 49.012329,
                                                                    'lng': 2.6032919},
                                                    'southwest': {'lat': 48.8072484,
                                                                    'lng': 2.2883109}},
                                        'location': {'lat': 48.9137455, 'lng': 2.4845729},
                                        'location_type': 'APPROXIMATE',
                                        'viewport': {'northeast': {'lat': 49.012329,
                                                                    'lng': 2.6032919},
                                                        'southwest': {'lat': 48.8072484,
                                                                    'lng': 2.2883109}}},
                            'place_id': 'ChIJTeBXx8Zs5kcRUCuLaMOCCwM',
                            'types': ['administrative_area_level_2', 'political']},
                            {'address_components': [{'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']}],
                            'formatted_address': 'Île-de-France, France',
                            'geometry': {'bounds': {'northeast': {'lat': 49.241504,
                                                                    'lng': 3.5590069},
                                                    'southwest': {'lat': 48.1200811,
                                                                    'lng': 1.44617}},
                                        'location': {'lat': 48.8499198, 'lng': 2.6370411},
                                        'location_type': 'APPROXIMATE',
                                        'viewport': {'northeast': {'lat': 49.241504,
                                                                    'lng': 3.5590069},
                                                        'southwest': {'lat': 48.1200811,
                                                                    'lng': 1.44617}}},
                            'place_id': 'ChIJF4ymA8Th5UcRcCWLaMOCCwE',
                            'types': ['administrative_area_level_1', 'political']},
                            {'address_components': [{'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']}],
                            'formatted_address': 'France',
                            'geometry': {'bounds': {'northeast': {'lat': 51.1241999,
                                                                    'lng': 9.6624999},
                                                    'southwest': {'lat': 41.31433,
                                                                    'lng': -5.5591}},
                                        'location': {'lat': 46.227638, 'lng': 2.213749},
                                        'location_type': 'APPROXIMATE',
                                        'viewport': {'northeast': {'lat': 51.1241999,
                                                                    'lng': 9.6624999},
                                                        'southwest': {'lat': 41.31433,
                                                                    'lng': -5.5591}}},
                            'place_id': 'ChIJMVd4MymgVA0R99lHx5Y__Ws',
                            'types': ['country', 'political']},
                            {'address_components': [{'long_name': 'W9F6+Q3',
                                                    'short_name': 'W9F6+Q3',
                                                    'types': ['plus_code']},
                                                    {'long_name': 'Saint-Denis',
                                                    'short_name': 'Saint-Denis',
                                                    'types': ['locality', 'political']},
                                                    {'long_name': 'Seine-Saint-Denis',
                                                    'short_name': 'Seine-Saint-Denis',
                                                    'types': ['administrative_area_level_2',
                                                                'political']},
                                                    {'long_name': 'Île-de-France',
                                                    'short_name': 'IDF',
                                                    'types': ['administrative_area_level_1',
                                                                'political']},
                                                    {'long_name': 'France',
                                                    'short_name': 'FR',
                                                    'types': ['country', 'political']}],
                            'formatted_address': 'W9F6+Q3 Saint-Denis, France',
                            'geometry': {'bounds': {'northeast': {'lat': 48.9245,
                                                                    'lng': 2.36025},
                                                    'southwest': {'lat': 48.924375,
                                                                    'lng': 2.360125}},
                                        'location': {'lat': 48.9244592, 'lng': 2.3601645},
                                        'location_type': 'ROOFTOP',
                                        'viewport': {'northeast': {'lat': 48.9257864802915,
                                                                    'lng': 2.361536480291502},
                                                        'southwest': {'lat': 48.9230885197085,
                                                                    'lng': 2.358838519708498}}},
                            'place_id': 'GhIJQD7XrVR2SEARCHHl7J3hAkA',
                            'plus_code': {'compound_code': 'W9F6+Q3 Saint-Denis, France',
                                            'global_code': '8FW4W9F6+Q3'},
                            'types': ['plus_code']}],
                'status': 'OK'}
        return reverse_answer


    def test_treat_google_api_reverse(self):
        """
        In this function we test the 'get_google_reverse_geocoding_answer' from the Googlemaps class.

        """
        googlemaps_reverse = Googlemaps()
        googlemaps_reverse.reverse_answer = self.mock_get_google_reverse_geocoding_answer(48.9244592, 2.3601645)
        result = googlemaps_reverse.treat_reverse_geocoding()
        assert result == '360 Avenue du Président Wilson, 93200 Saint-Denis, France'



