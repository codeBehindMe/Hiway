from typing import Any
import streamlit as st
import random


def _route_information(col: Any):
    col.markdown(
        """
    ## Your journey information
    """
    )


    origin_addr = col.text_input("Origin address") 
    dest_adder = col.text_input("Destination address") 
  

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
