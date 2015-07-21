from flask import Flask, render_template, request
import util

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def root( ):
    if request.method=="POST":
        city=request.form["city"]
        while " " in city:
            city=city[:city.find(" ")]+"_"+city[city.find(" ")+1:]
    else:
        city="nyc"
    temp = util.get_weather(city)
    temp = (temp-273.15)*1.8+32
    while "_" in city:
            city=city[:city.find("_")]+" "+city[city.find("_")+1:]
    if temp <=0:
        planet = "Pluto"
    elif temp >0 and temp <= 20:
        planet = "Uranus"
    elif temp >20 and temp <= 40:
        planet = "Neptune"
    elif temp >40 and temp <= 50:
        planet = "Saturn"
    elif temp >50 and temp <= 60:
        planet = "Mars"
    elif temp >60 and temp <= 70:
        planet = "Earth"
    elif temp >70 and temp <= 80:
        planet = "Mercury"
    elif temp > 80 and temp <= 90:
        planet = "Venus"
    elif temp > 90 and temp <= 100:
        planet = "Jupiter"
    elif temp >100:
        planet = "Sun"
    d = { 'city':city, 'temp':temp }
    return render_template( 'index.html', d = d, planet = planet)

if __name__ == '__main__':
    app.debug = True
    app.run( port = 5000 )
