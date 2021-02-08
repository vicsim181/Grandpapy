import requests
import os
import json


class Googlemaps():
    """
    Class holding the GoogleMaps section, calling the API and treating the answer.
    """

    GMAPS_KEY = os.environ['GOOGLE_MAPS_KEY']

    def __init__(self):
        pass

    def get_google_geocoding_answer(self, input_request):
        """
        This function sends a GET request to the Google Maps Geocoding API with various parameters.
        In the parameters is included the treated request received from the form in the web page.
        The answer of the request should be a json with datas about the place asked in the treated request.
        """
        parameters = {'address': input_request, 'key': Googlemaps.GMAPS_KEY}
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        try:
            r = requests.get(url=url, params=parameters)
            self.result = r.json()
            return self.result
        except json.decoder.JSONDecodeError:
            print('The json file returned from Google Maps is empty! It can be due to a HTTP error, check the url passed in requests.')
            exit()
        except requests.exceptions.ConnectionError:
            print('A connection error occured')
            exit()

    def get_google_reverse_geocoding_answer(self, lat, lng):
        """
        We use the reverse geocoding process to get the address of the searched place, in order to give a precise place to the user on our website.
        The geographic coordinates obtained previously are sent back to GoogleMaps, which gives us a precise address.
        """
        parameters = {'latlng': str(lat) + ',' + str(lng), 'key': Googlemaps.GMAPS_KEY}
        self.reverse = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=parameters).json()
        return self.reverse

    def treat_geocoding_answer(self):
        """
        In this function we get the previous json from calling the GMaps Geocoding API and treat it.
        The objective is to get the latitude and longitude infos, which are located in a precise place in the json.
        """
        results = self.result.get('results')
        geometry = results[0]['geometry']['location']
        self.latitude = geometry['lat']
        self.longitude = geometry['lng']
        return self.latitude, self.longitude

    def treat_reverse_geocoding(self):
        self.reverse_treated = self.reverse['results'][0]['formatted_address']
        return self.reverse_treated

    def google_process(self, input_request):
        """
        Function that executes the two above functions in the order.
        First we get the result from GoogleMaps depending on the input request.
        Then we treat the result and get the latitude and longitude, we return those two values.
        """
        self.get_google_geocoding_answer(input_request)
        self.treat_geocoding_answer()
        return self.latitude, self.longitude
