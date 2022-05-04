from requests import head
import streamlit as st
from src.containers.header import header
import os
import gmaps 
import streamlit.components.v1 as components
import plotly.express as px

from ipywidgets import embed

gmaps.configure(api_key=os.environ["GOOGLE_MAPS_KEY"])
px.set_mapbox_access_token(os.environ["MAPBOX_TOKEN"])


#Define location 1 and 2
Durango = (37.2753,-107.880067)
SF = (37.7749,-122.419416)
#Create the map
fig = gmaps.figure()
#create the layer
layer = gmaps.directions.Directions(Durango, SF,mode='car')
#Add the layer
fig.add_layer(layer=layer)

snippet = embed.embed_snippet(views=fig)
print(snippet)
html = embed.html_template.format(title="foo",snippet=snippet)


if __name__ == "__main__":
    header()
    components.html(html)