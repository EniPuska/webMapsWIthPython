import folium
import pandas

map = folium.Map(location= [80, -100])
map.save("map.html")
'''data = pandas.read_csv("Volcanoes.txt")
latitude = list(data("LON"))
longitude = list(data("LAT"))'''