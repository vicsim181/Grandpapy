import requests
import pprint


gsradius = 500
gslimit = 10
request = 'donner+adresse+stade+france'


def get_wiki_answer(input_request):
    lat, lng = input_request
    parameters = {'action': 'query', 'format': 'json', 'list': 'geosearch', 'gscoord': str(lat) + '|' + str(lng),
                  'gsradius': gsradius, 'gslimit': gslimit}
    r = requests.get('https://fr.wikipedia.org/w/api.php', params=parameters).json()
    return r


def search_for_element_to_display(request, answer):
    results = answer['query']['geosearch']
    treated_request = request.split('+')
    elements_list = []
    for result in results:
        i = 0
        split_title = result['title'].split(' ')
        for word in split_title:
            if word.lower() in treated_request:
                # print(word)
                i += 1
        elements_list.append({'title': result['title'],
                              'i': i,
                              'pageid': result['pageid'],
                              'dist': result['dist']})
    max, y = 0, 0
    for i, dictionnary in enumerate(elements_list):
        if dictionnary['i'] > max:
            max, y = dictionnary['i'], i
    return elements_list[y]['title'], elements_list[y]['dist']


def essai(input):
    one = get_wiki_answer(input)
    two_title, two_dist = search_for_element_to_display(request, one)
    print(two_title, two_dist)


#  essai((48.875067, 2.348973))
essai((48.9244592, 2.3601645))
