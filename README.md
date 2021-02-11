# **Ask for a particular place to Grandpapy, he will know it for sure!**
(Well he will try at least)

## What is the objective of this application? 

When on the main page (and only), users can ask Grandpapy about a specific place, precising the city and the country will help the exactness of the result.

## How does it work?

The application uses the APIs of GoogleMaps and Wikipedia.  
It treats the request of the user and send it to those two APIs.  
It gets geographic coordinates as an answer from Google Maps, as well as an address.  
These coordinates are used to make a geographical research on Wikipedia.  
Wikipedia is supposed to give back the closest page registered from the geographic coordinates.  
Unfortunately it seems this research with the Wikipedia API is not great and therefore not totally reliable.  

# **How to use the app?**

## Install it


**To install a development version runing with flask, check the flask branch, check the [flask documentation](https://flask.palletsprojects.com/en/1.1.x/).**

**To install a production version runing on Heroku, check the main branch, check the [Heroku documentation](https://www.heroku.com/).**
  

Fork the repo or download the files and install the dependencies with:
On Windows:
```bash
> pip install -r requirements.txt
```
On Linux:
```bash
> pip3 install -r requirements.txt
```

## The APIs

To communicate with the different APIs of Google Maps and Wikipedia, you will need the Requests library.  
For more informations, check the [documentation](https://requests.readthedocs.io/en/master/).  

There are two Google Maps API used in this project, the first one is the [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview?hl=fr), the second one is the [Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started).  
You will need to set an API key on the [Google Cloud Platform](https://console.cloud.google.com/getting-started) in order to use them.

It's recommended to use two API keys, one for the back-end and one for the front-end.  
The back-end key can be restricted to the Geocoding API use only, it will be set as an environment variable on your machine and won't appear in the code.  
The front-end key can be restricted to the Maps Embed API use only, but also with the HTTP url of your heroku page once deployed.

For the Wikipedia part you will interact with its [API](https://www.mediawiki.org/wiki/API:Main_page), there is no need of API key to use it.

In this project those keys have been set as Environment Variables, they are imported in the scripts as follow:
```python
import os
api_key = os.environ['environment_variable_name']
```

(Same principle for the flask secret key in the config.py file.)

The interaction with those APIs is managed separately in two scripts, one for the GoogleMaps part and another dedicated to the Wikipedia part.

## On Flask

If you wish to use the flask version, from the flask branch of this project, remember to take off the http restriction on the front-end Google Maps API key.  
In the contrary case the small embed map won't appear in the answer of Grandpapy.

In the index.js file in the static/ folder, be sure to set the url in the 'sendRequest' function as follow:
```javascript
async function sendRequest(request) {
    return $.post(`http://localhost:5000/ajax/${request}`);
}
```

You can then initiate your flask server via the terminal like this:
```bash
>flask run --host=localhost
```

## On Heroku

If you wish to deploy your own version on Heroku, you will need to create an account.  
You can link your Github main/master repo with your project in Heroku.  

You can also settle your environment variables directly in the Heroku dashboard, located in the settings of your Heroku account.  
It is also possible to set the variables directly in the terminal via:
```bash
>heroku config:set MY_KEY=valueofthekey
```

For more information about the Heroku functions and principles, check the [documentation]().  

For the deployment, follow the instructions in the Heroku documentation.
In case of fail, you can check the logs with:
```bash
>heroku logs
```
or
```bash
>heroku logs --tail
```

