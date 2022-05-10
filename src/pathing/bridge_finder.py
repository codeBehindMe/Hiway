from typing import Any, List, Tuple
import pandas as pd
from src.models.path import Path, Point, Segment


class BridgeFinder:
    def __init__(self, bridges_df: pd.DataFrame, tau: float) -> None:
        """Finds the bridges that intersect in a given path.


        Args:
            bridges_df (pd.DataFrame): Dataframe containing the bridge data.
            tau (float): Tolerance to within which bridges should be included.
        """
        self.bridges_df = bridges_df
        self.tau = tau

    def _find_bridges_in_segment(self, segment: Segment) -> List:
        """Find bridges in the segment

        Args:
            segment (Segment): Segment in which bridges to be found.

        Returns:
            List: List of bridges.
        """

        # First let's truncate our bridge list to only a small search space around
        # the line. This is going to be bound inside a box, which can be defined
        # as x- tau from left most point, y+ tau from the upper most point which
        # forms the top left cordinate and conversely the x + tau and y - tau of
        # the right and bottom most points.

        lng_min = segment.extreme_left() - self.tau
        lng_max = segment.extreme_right() + self.tau

        lat_min = segment.extreme_bottom() - self.tau
        lat_max = segment.extreme_top() + self.tau

        bridges_in_segment = self.bridges_df[
            (self.bridges_df["lng"] < lng_max)
            & (self.bridges_df["lng"] > lng_min)
            & (self.bridges_df["lat"] > lat_min)
            & (self.bridges_df["lat"] < lat_max)
        ]

        # FIXME: The distance is a large box, so not very accurate. Update.
        return bridges_in_segment

    def find_bridges_in_path(self, path: Path) -> Any:

        bridges = []
        for segment in path.segments:
            bridges.append(self._find_bridges_in_segment(segment))

        bridges_df: pd.DataFrame = pd.concat(bridges)
        # FIXME: Need to get unique bridge IDs only.
        return bridges_df
