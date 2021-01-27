import requests
import pprint
import json


gsradius = 1000
gslimit = 10
request = 'trouver+opéra+garnier+paris'


def get_wiki_answer(lat, lng):
    """
    This function sends a GET request to the Wikipedia API with various parameters.
    In the parameters are included the latitude and longitude the function got from the Google_Api class.
    The answer received here should be a json file with different wikipedia articles located in a specified
    perimeter around the geographic coordinates sent in the request. If no articles are found around,
    then the file is returned empty.
    """
    parameters = {'action': 'query', 'format': 'json', 'list': 'geosearch', 'gscoord': str(lat) + '|' + str(lng),
                  'gsradius': gsradius, 'gslimit': gslimit}
    url = 'https://fr.wikipedia.org/w/api.php'
    try:
        r = requests.get(url=url, params=parameters)
        result = r.json()
        return result
    except json.decoder.JSONDecodeError:
        print('The json file returned from Wikipedia is empty! It can be due to a HTTP error, check the url passed in requests.')
        exit()
    except requests.exceptions.ConnectionError:
        print('A connection error occured')
        exit()


def search_for_correspondence(request, answer):
    """
    This function has the objective to determine if the answers we got from Wikipedia are matching with the request.
    It checks the words sent to GoogleMaps and the titles of the 10 closest wikipages found around the geographic coordinates sent.
    """
    result = answer['query']['geosearch'][0]['title']
    print(result)
    treated_request = request.split('+')
    i = 0
    split_title = result['title'].split(' ')
    for word in split_title:
        if word.lower() in treated_request:
            i += 1
    if i > 1:
        return 1
    else:
        return 0


def get_wikipedia_explanations(answer):
    """
    """
    results = answer['query']['geosearch'][0]['title']
    id_page = answer['query']['geosearch'][0]['pageid']
    parameters = {'action': 'query', 'format': 'json', 'prop': 'extracts', 'exintro': True, 'explaintext': True,
                  'redirects': 1, 'titles': results}
    url = 'https://fr.wikipedia.org/w/api.php'
    r = requests.get(url=url, params=parameters).json()
    # pprint.pprint(r['query']['pages'][str(id_page)]['extract'])
    return r['query']['pages'][str(id_page)]['extract']


def wiki_process(request, lat, lng):
    """
    """
    one = get_wiki_answer(lat, lng)
    two = search_for_correspondence(request, one)
    explanations = get_wikipedia_explanations(one)
    return explanations, two


# pprint.pprint(wiki_process(request, 48.87194,2.33222))
# pprint.pprint(wiki_process(request, 48.87194, 2.33222))
