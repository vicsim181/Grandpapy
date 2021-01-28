# import json
import requests
import os
import json
import pprint


gmaps_key = os.environ['google_maps_key']


def get_google_geocoding_answer(input_request):
    """
    This function sends a GET request to the Google Maps Geocoding API with various parameters.
    In the parameters is included the treated request received from the form in the web page.
    The answer of the request should be a json with datas about the place asked in the treated request.
    """
    parameters = {'address': input_request, 'key': gmaps_key}
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    try:
        r = requests.get(url=url, params=parameters)
        result = r.json()
        return result
    except json.decoder.JSONDecodeError:
        print('The json file returned from Google Maps is empty! It can be due to a HTTP error, check the url passed in requests.')
        exit()
    except requests.exceptions.ConnectionError:
        print('A connection error occured')
        exit()


def get_google_reverse_geocoding_answer(lat, lng):
    parameters = {'latlng': str(lat) + ',' + str(lng), 'key': gmaps_key}
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=parameters).json()
    return r['results'][0]['formatted_address']


def treat_geocoding_answer(input_request):
    """
    In this function we get the previous json from calling the GMaps Geocoding API and treat it.
    The objective is to get the latitude and longitude infos, which are located in a precise place in the json.
    """
    answer = get_google_geocoding_answer(input_request)
    results = answer.get('results')
    geometry = results[0]['geometry']['location']
    latitude = geometry['lat']
    longitude = geometry['lng']
    return latitude, longitude


# essai = 'savoir+opéra+garnier+paris'

# pprint.pprint(get_google_reverse_geocoding_answer(48.87194, 2.33222))
