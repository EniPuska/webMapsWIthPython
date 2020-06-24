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
    featureGroupForVolcanoes = folium.FeatureGroup(name = "Volcanoes")
    for lt, ln, el in zip(lat, lon, elev):
        featureGroupForVolcanoes.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " m", icon = folium.Icon(color = setIconColor(el))))
          
    featureGroupForPopullation = folium.FeatureGroup(name = "Popullation")
    featureGroupForPopullation.add_child(folium.GeoJson(data = (worldData).read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    map.add_child(featureGroupForVolcanoes)
    map.add_child(featureGroupForPopullation)
    map.add_child(folium.LayerControl())
    map.save("map.html")
setMap()