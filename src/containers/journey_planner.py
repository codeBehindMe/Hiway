from typing import Any
import streamlit as st
from src.pathing.address_finder import AddressFinder
from src.pathing.path_finder import PathFinder
from src.pathing.bridge_finder import BridgeFinder
from src.bridges.data import bridge_data
import plotly.express as px
import src.config as config

import pandas as pd


def _info():

  col1, col2 = st.columns(2)

  col1.markdown(
  """
  ## Your information here
  """
  )
  with st.form("info_form"):
    origin_addr = col1.text_input("Origin address")
    dest_addr = col1.text_input("Destination address")

    if origin_addr and dest_addr:
        # FIXME: Export to private function
        af = AddressFinder(config.GOOGLE_MAPS_KEY)
        valid_origin = af.find_address(origin_addr)
        valid_destination = af.find_address(dest_addr)

        pf = PathFinder(config.GOOGLE_MAPS_KEY)
        path_df: pd.DataFrame = pf.get_path_points_df(valid_origin, valid_destination)

        # FIXME: Chart Title
        col2.plotly_chart(px.line_mapbox(path_df, lat="lat", lon="lng"))
        bridge_finder = BridgeFinder(bridge_data.get_processed_df(), 0.01)
        # FIXME: Changed to subset of columns in df.
        # FIXME: Dataframe title
        col2.dataframe(
            bridge_finder.find_bridges_in_path(
                pf.get_path(valid_origin, valid_destination)
            )
        )


    v_length = col1.text_input("Length (m)")
    v_width = col1.text_input("Width (m)")
    v_height = col1.text_input("Height (m)")

    v_num_axles = col1.text_input("Number of axles")
    v_dist_extreme_axles = col1.text_input("Dicol.nce between extreme axles (m)")

    v_gross_weight = col1.number_input("Gross weight in kg")

    submitted = st.form_submit_button("Submit")



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
        bridge_finder = BridgeFinder(bridge_data.get_processed_df(), 0.01)
        # FIXME: Changed to subset of columns in df.
        # FIXME: Dataframe title
        col.dataframe(
            bridge_finder.find_bridges_in_path(
                pf.get_path(valid_origin, valid_destination)
            )
        )


def _vehicle_information(col: Any):

    col.markdown(
        """
    ## Your vehicle information 
    """
    )

    with st.form("Vehicle info"):

        v_length = col.text_input("Length (m)")
        v_width = col.text_input("Width (m)")
        v_height = col.text_input("Height (m)")

        v_num_axles = col.text_input("Number of axles")
        v_dist_extreme_axles = col.text_input("Dicol.nce between extreme axles (m)")

        v_gross_weight = col.number_input("Gross weight in kg")

        submitted = st.form_submit_button("Submit")


def journey_planner():

    st.header("Journey Planner")
    with st.container():

        _info()
        # col1, col2 = st.columns(2)

        # _route_information(col1)
        # _vehicle_information(col2)
