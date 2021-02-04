import requests
import json


class Wikipedia():
    """
    Class holding the functions and elements linked to Wikipedia, calling the API and treating the answer.
    """
    GSRADIUS = 1000
    GSLIMIT = 10

    def __init__(self):
        pass

    def get_wiki_answer(self, lat, lng):
        """
        This function sends a GET request to the Wikipedia API with various parameters.
        In the parameters are included the latitude and longitude the function got from the Google_Api class.
        The answer received here should be a json file with different wikipedia articles located in a specified
        perimeter around the geographic coordinates sent in the request. If no articles are found around,
        then the file is returned empty.
        """
        parameters = {'action': 'query', 'format': 'json', 'list': 'geosearch', 'gscoord': str(lat) + '|' + str(lng),
                      'gsradius': Wikipedia.GSRADIUS, 'gslimit': Wikipedia.GSLIMIT}
        url = 'https://fr.wikipedia.org/w/api.php'
        try:
            r = requests.get(url=url, params=parameters)
            self.result = r.json()
        except json.decoder.JSONDecodeError:
            print('The json file returned from Wikipedia is empty! It can be due to a HTTP error, check the url passed in requests.')
            exit()
        except requests.exceptions.ConnectionError:
            print('A connection error occured')
            exit()

    def search_for_correspondence(self, request):
        """
        This function has the objective to determine if the answer we got from Wikipedia is matching with the request.
        It checks the words sent to GoogleMaps and the title of the closest wikipedia page obtained with the geographic coordinates.
        """
        result = self.result['query']['geosearch'][0]['title']
        treated_request = request.split('+')
        i = 0
        split_title = result.split(' ')
        for word in split_title:
            if word.lower() in treated_request:
                i += 1
        if i > 1:
            return 1
        else:
            return 0

    def get_wikipedia_explanations(self):
        """
        We get the first 5 sentences (or less) of the description of the previous obtained wikipedia page.
        In order to do so, we send another request to wikipedia, with the title of the wanted page.
        We also need the id of the page to sort the informations in the json returned by wikipedia.
        """
        results = self.result['query']['geosearch'][0]['title']
        id_page = self.result['query']['geosearch'][0]['pageid']
        parameters = {'action': 'query', 'format': 'json', 'prop': 'extracts', 'exintro': True, 'explaintext': True,
                      'redirects': 1, 'exsentences': 5, 'titles': results}
        url = 'https://fr.wikipedia.org/w/api.php'
        r = requests.get(url=url, params=parameters).json()
        final_result = r['query']['pages'][str(id_page)]['extract']
        detailed_result = list(final_result)
        detailed_result[0] = detailed_result[0].lower()
        self.final_result = "".join(detailed_result)

    def wiki_process(self, request, lat, lng):
        """
        Here we execute the above functions in the good order, we send geographic coordinates to get the closest wikipedia article.
        We check if the title of the article matches with the words of the request.
        We get the 5 first sentences of the description part of the article.
        We return the description and the number 1 or 0 depending on the title and the request.
        """
        self.get_wiki_answer(lat, lng)
        correspondence = self.search_for_correspondence(request)
        self.get_wikipedia_explanations()
        return self.final_result, correspondence
