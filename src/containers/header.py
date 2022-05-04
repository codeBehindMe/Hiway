import streamlit as st
import plotly.express as px
import geopandas as gpd
from src.bridges.data import BridgeData


def _plot_bridge_map(bridge_df: gpd.GeoDataFrame):
    return px.scatter_mapbox(
        bridge_df,
        lat="lat",
        lon="lng",
        hover_name="FEATURE_CROSSED",
        color="BRIDGE_RATING",
        title="Victorian Bridges",
    )


def header():

    with st.container():
        st.header("HiWay")

        st.markdown(
            """
      ## Automated heavy vehicle route planning
      > Technology demonstrator only, not for actual use
      """
        )

        # FIXME: Floating file reference literal, refactor.
        bridge_df = BridgeData("vic_bridges.geojson").get_processed_df()

        st.plotly_chart(_plot_bridge_map(bridge_df))
