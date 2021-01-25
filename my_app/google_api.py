# import json
import requests
import os


gmaps_key = os.environ['google_maps_key']


def get_google_geocoding_answer(input_request):
    parameters = {'address': input_request, 'key': gmaps_key}
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=parameters).json()
    return r


def get_google_reverse_geocoding_answer(lat, lng):
    parameters = {'latlng': str(lat) + ',' + str(lng), 'key': gmaps_key}
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=parameters).json()
    return r


def treat_geocoding_answer(input_request):
    answer = get_google_geocoding_answer(input_request)
    results = answer.get('results')
    geometry = results[0]['geometry']['location']
    latitude = geometry['lat']
    longitude = geometry['lng']
    return latitude, longitude


stade_france = 'donner+adresse+stade+france'

print(treat_geocoding_answer(stade_france))
