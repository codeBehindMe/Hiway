from typing import Any
import streamlit as st
from src.pathing.address_finder import AddressFinder
from src.pathing.path_finder import PathFinder
import plotly.express as px
import src.config as config

import pandas as pd


def _route_information(col: Any):
    col.markdown(
        """
    ## Your journey information
    """
    )

    origin_addr = col.text_input("Origin address")
    dest_addr = col.text_input("Destination address")

    if origin_addr and dest_addr:
        af = AddressFinder(config.GOOGLE_MAPS_KEY)
        valid_origin = af.find_address(origin_addr)
        valid_destination = af.find_address(dest_addr)

        pf = PathFinder(config.GOOGLE_MAPS_KEY)
        path_df: pd.DataFrame = pf.get_path_points_df(valid_origin, valid_destination)

        # FIXME: Chart Title
        col.plotly_chart(px.line_mapbox(path_df, lat="lat", lon="lng"))


def _vehicle_information(col: Any):

    col.markdown(
        """
    ## Your vehicle information 
    """
    )

    v_length = col.text_input("Length (m)")
    v_width = col.text_input("Width (m)")
    v_height = col.text_input("Height (m)")

    v_num_axles = col.text_input("Number of axles")
    v_dist_extreme_axles = col.text_input("Dicol.nce between extreme axles (m)")


def journey_planner():

    st.header("Journey Planner")
    with st.container():

        col1, col2 = st.columns(2)

        _route_information(col1)
        _vehicle_information(col2)
