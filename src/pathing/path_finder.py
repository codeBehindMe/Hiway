from typing import Tuple
import googlemaps as gmaps
import pandas as pd
from src.models.path import Path, Point, Segment
from src.pathing.address_finder import ValidAddress


class PathFinder:
    def __init__(self, google_maps_key: str) -> None:
        self.client = gmaps.Client(key=google_maps_key)

    @staticmethod
    def _get_points_from_directions_response(res):

        print(res)

        for step in res[0]["legs"][0]["steps"]:
            yield step["start_location"]["lat"], step["start_location"]["lng"]
            yield step["end_location"]["lat"], step["end_location"]["lng"]

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

    def get_path_points_df(self, start_loc: ValidAddress, end_loc: ValidAddress):
        print(start_loc, end_loc)
        res = self.client.directions(
            (start_loc.LAT, start_loc.LNG), (end_loc.LAT, end_loc.LNG), mode="driving"
        )

        pts = self._get_points_from_directions_response(res)
        df = pd.DataFrame(pts)
        df = df.rename(columns={0: "lat", 1: "lng"})
        return df
