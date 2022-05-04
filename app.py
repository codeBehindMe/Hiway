import streamlit as st
from src.containers.header import header
import os
import plotly.express as px


px.set_mapbox_access_token(os.environ["MAPBOX_TOKEN"])


if __name__ == "__main__":
    header()
