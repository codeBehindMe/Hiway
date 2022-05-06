import streamlit as st
from src.containers.header import header
from src.containers.journey_planner import journey_planner
import os
import plotly.express as px


px.set_mapbox_access_token(os.environ["MAPBOX_TOKEN"])
st.set_page_config(layout="wide")


if __name__ == "__main__":
    header()
    journey_planner()
