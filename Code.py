import folium
import pandas as pd
my_map=folium.Map(
    location=[20.593683,78.962883], zoom_start=5,
    tiles="cartodbdark_matter"
)
my_map
states = pd.read_csv('INDIA STATES LATLONG1.csv')
states.head(30)
my_map=folium.Map(location=[20.593683,78.962883], zoom_start=5)

for _, state in states.iterrows():
    folium.Marker(
        location=[state['latitude'], state['longitude']],
        popup=state['information'],
        tooltip=state['name'],
        icon=folium.Icon(color=state['color']),
    ).add_to(my_map)
folium.TileLayer('stamentoner').add_to(my_map)
my_map
