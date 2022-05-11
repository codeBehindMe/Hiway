from typing import Tuple
import googlemaps as gmaps
import pandas as pd
from src.models.path import Path, Point, Segment
from src.pathing.address_finder import ValidAddress


class PathFinder:
    def __init__(self, google_maps_key: str) -> None:
        self.client = gmaps.Client(key=google_maps_key)

    @staticmethod
    def _get_path_from_directions_response(res: dict) -> Path:

        segments = []
        for step in res[0]["legs"][0]["steps"]:
            segments.append(
                Segment(
                    Point(step["start_location"]["lat"], step["start_location"]["lng"]),
                    Point(step["end_location"]["lat"], step["end_location"]["lng"]),
                )
            )

        return Path(segments)

    def get_path(self, start_loc: ValidAddress, end_loc: ValidAddress) -> Path:
        res = self.client.directions(
            (start_loc.LAT, start_loc.LNG), (end_loc.LAT, end_loc.LNG), mode="driving"
        )
        return self._get_path_from_directions_response(res)

    def get_path_points_df(self, start_loc: ValidAddress, end_loc: ValidAddress):

        return self.get_path(start_loc, end_loc).to_dataframe()
