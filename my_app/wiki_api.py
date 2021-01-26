import requests
import pprint
import json


gsradius = 1000
gslimit = 10
request = 'donner+adresse+stade+france'


def get_wiki_answer(lat, lng):
    """
    This function sends a GET request to the Wikipedia API with various parameters.
    In the parameters are included the latitude and longitude the function got from the Google_Api class.
    The answer received here should be a json file with different wikipedia articles located in a specified
    perimeter around the geographic coordinates sent in the request. If no articles are found around,
    then the file is returned empty.
    """
    print(lat, lng)
    parameters = {'action': 'query', 'format': 'json', 'list': 'geosearch', 'gscoord': str(lat) + '|' + str(lng),
                  'gsradius': gsradius, 'gslimit': gslimit}
    url = 'https://fr.wikipedia.org/w/api.php'
    try:
        r = requests.get(url=url, params=parameters)
        print(r.url)
        result = r.json()
        return result
    except json.decoder.JSONDecodeError:
        print('The json file returned from Wikipedia is empty! It can be due to a HTTP error, check the url passed in requests.')
        exit()
    except requests.exceptions.ConnectionError:
        print('A connection error occured')
        exit()


def search_for_element_to_display(request, answer):
    results = answer['query']['geosearch']
    treated_request = request.split('+')
    elements_list = []
    for result in results:
        i = 0
        split_title = result['title'].split(' ')
        for word in split_title:
            if word.lower() in treated_request:
                i += 1
        elements_list.append({'title': result['title'],
                              'i': i,
                              'dist': result['dist']})
    max, y = 0, 0
    for index, dictionnary in enumerate(elements_list):
        if dictionnary['i'] > max:
            max, y = dictionnary['i'], index
    # return elements_list[y]['title'], elements_list[y]['dist']
    return elements_list[y]['title']


def get_wikipedia_explanations(element):
    parameters = {'action': 'query', 'format': 'json', 'titles': element}
    url = 'https://fr.wikipedia.org/w/api.php'
    r = requests.get(url=url, params=parameters).json()
    return r


def essai(lat, lng):
    one = get_wiki_answer(lat, lng)
    page_id = search_for_element_to_display(request, one)
    pprint.pprint(get_wikipedia_explanations(page_id))


essai(48.9244592, 2.3601645)
