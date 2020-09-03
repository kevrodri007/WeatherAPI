# Kevin Rodriguez
# Weather Retriever using AccuWeather API

import urllib.request # imports url grabbing
import json # for reading the pages

api_key = 'eWHuam12nGBG28puvV5X5Ao0PQs3AOj6' # API Key



city = input('What city would you like to receive the weather from?: ') # City Input
city = city.replace(" ", "") # removes any spaces in the city name so the weather API can read it

url = urllib.request.urlopen('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + api_key + '&q=' + city)
data = json.load(url)

city = data[0] # grabs the first search result
cityKey = city['Key'] # grabs the city key from the first search result and assigns it to a string


def returnWeather(cityKey): # returns weather information in dictionary format using cityKey
    url = urllib.request.urlopen('http://dataservice.accuweather.com/currentconditions/v1/'+ cityKey + '?' + 'apikey=' + api_key)
    data = json.load(url)
    print('Temperature is ' + str(data[0]['Temperature']['Imperial']['Value']) + " degrees F, " + str(data[0]['Temperature']['Metric']['Value']) + " degrees C")
    print("Weather Details: " + str(data[0]['WeatherText']))
    print('Precipitation: ' + str(data[0]['HasPrecipitation']))



returnWeather(cityKey) # return weather