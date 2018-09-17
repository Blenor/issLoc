import json
import turtle
import tkinter as tk
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
    print(p['name'], 'on board', p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
#screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.png')

