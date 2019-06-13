import turtle
import urllib.request
import json
## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## json 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press the ENTER key to continue')  

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set the resolution

screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))

iss.penup()
iss.goto(lon, lat)

## My location
yellowlat = 39.4
yellowlon = -77.7
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

{
  "message": "success",
  "request": {
    "altitude": 100,
    "datetime": 1527395287,
    "latitude": 39.4,
    "longitude": -77.7,
    "passes": 5
  },
  "response": [
    {
      "duration": 641,
      "risetime": 1527406615
    },
    {
      "duration": 602,
      "risetime": 1527412410
    },
    {
      "duration": 261,
      "risetime": 1527418311
    },
    {
      "duration": 570,
      "risetime": 1527472536
    }
  ]
}

turtle.mainloop() # <-- this line should ALWAYS be at the bottom of your script. It prevents the graphic from closing!!!
