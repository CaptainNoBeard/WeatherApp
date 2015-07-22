import urllib2
import json

def get_weather(city='nyc'):
    url = 'http://api.openweathermap.org/data/2.5/find?q=' + city
    u = urllib2.urlopen( url )
    result = json.loads(u.read())

    print result    
    return result['list'][0]['main']['temp']

