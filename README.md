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

## The APIs

To communicate with the different APIs of Google Maps and Wikipedia, you will need the Requests library.
You can install it with 
```bash
> python -m pip install requests
```
For more informations, check the documentation: https://requests.readthedocs.io/en/master/



