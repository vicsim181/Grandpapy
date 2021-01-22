# import json
import requests
# import pprint
from .input_parser import parse


def get_google_geocoding_answer(input_request):
    r = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={input_request}&key=AIzaSyAstsdkCuu_k4i-V4ZNVW6WTZkYEeMvV1c').json()
    return r


def get_google_reverse_geocoding_answer(lat, lng):
    r = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key=AIzaSyAstsdkCuu_k4i-V4ZNVW6WTZkYEeMvV1c').json()
    return r


def treat_geocoding_answer(answer):
    results = answer.get('results')
    geometry = results[0]['geometry']['location']
    latitude = geometry['lat']
    longitude = geometry['lng']
    return 'lat: ', latitude, 'long: ', longitude


# def treat_reverse_answer(answer):

