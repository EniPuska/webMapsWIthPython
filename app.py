import folium
import pandas

def setIconColor(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

def setMap():
    data = pandas.read_csv("Volcanoes.txt")
    worldData = open("world.json", 'r', encoding='utf-8-sig')
    lat = list(data["LAT"])
    lon = list(data["LON"])
    elev = list(data["ELEV"])

    map = folium.Map(location=[38.58, -99.09], zoom_start=6)
    featureGroup = folium.FeatureGroup(name = "My Map")
    for lt, ln, el in zip(lat, lon, elev):
        featureGroup.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " m", icon = folium.Icon(color = setIconColor(el))))
        #featureGroup.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " m", 
    featureGroup.add_child(folium.GeoJson(data = (worldData).read()))
    map.add_child(featureGroup)
    map.save("map.html")

setMap()