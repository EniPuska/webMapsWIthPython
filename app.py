import folium
import pandas

map = folium.Map(location=[37.963792, 23.722097], zoom_start=18)
featureGroup = folium.FeatureGroup(name = "My Map")
featureGroup.add_child(folium.Marker(location=[37.963792, 23.722097], popup="I m a Marker", icon=folium.Icon(color='green')))
map.add_child(featureGroup)
map.save("map.html")
'''data = pandas.read_csv("Volcanoes.txt")
latitude = list(data("LON"))
longitude = list(data("LAT"))'''