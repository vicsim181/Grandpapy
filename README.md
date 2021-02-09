# **Ask for a particular place to Grandpy, he will know it for sure!**
(Well he will try at least)

## What is the objective of this application? 

When on the main page (and only), users can ask Grandpy about a specific place, precising the city and the country will help the exactness of the result.

## How does it work?

The application uses the APIs of GoogleMaps and Wikipedia. 
It treats the request of the user and send it to those two APIs.
It gets geographic coordinates as an answer from Google Maps, as well as an address.
These coordinates are used to make a geographical research on Wikipedia.
Wikipedia is supposed to give back the closest page registered from the geographic coordinates.
Unfortunately it seems this research with the Wikipedia API is not great and therefore not totally reliable.

# **How to use the app?**

## Install it

**To install a development version runing with flask, check the flask branch.**
**To install a production version runing on Heroku, check the main branch.**

Fork the repo or download the files and install the dependencies with:
```bash
> pip install -r requirements.txt
```

## The APIs

To communicate with the different APIs of Google Maps and Wikipedia, you will need the Requests library.
You can install it with 
```bash
> python -m pip install requests
```
For more informations, check the [documentation](https://requests.readthedocs.io/en/master/).

There are two Google Maps API used in this project.
The first one is the [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview?hl=fr).
The second one is the [Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started).
You will need to set an API key on the [Google Cloud Platform](https://console.cloud.google.com/getting-started) in order to use them.

It's recommended to use two API keys, one for the back-end and one for the front-end.
The back-end key can be restricted to the Geocoding API use only, it will be set as an environment variable on your machine and won't appear in the code.
The front-end key can be restricted to the Maps Embed API use only, but also with the HTTP url of your heroku page once deployed. 

For the Wikipedia part you will interact with its [API](https://www.mediawiki.org/wiki/API:Main_page).
There is no need of API key to use the Wikipedia one.

In this project those keys have been set as Environment Variables, they are imported in the scripts a follow:
```python
import os
api_key = os.environ['environment_variable_name']
```

(Same principle for the flask secret key in the config.py file.)

