from typing import List
import pandas as pd
from dataclasses import dataclass


@dataclass
class Point:
    LAT: float
    LNG: float


@dataclass
class Segment:
    START: Point
    END: Point

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(
            [(self.START.LAT, self.START.LNG), (self.END.LAT, self.END.LNG)]
        )

    def extreme_left(self) -> float:
        return min(self.START.LNG, self.END.LNG)

    def extreme_right(self) -> float:
        return max(self.START.LNG, self.END.LNG)

    def extreme_top(self) -> float:
        return min(self.START.LAT, self.END.LAT)

    def extreme_bottom(self) -> float:
        return max(self.START.LAT, self.END.LAT)


class Path:
    def __init__(self, segments: List[Segment]) -> None:
        self.segments = segments

    def to_dataframe(self) -> pd.DataFrame:
        coords = []
        for segment in self.segments:
            coords.append((segment.START.LAT, segment.START.LNG))
            coords.append((segment.END.LAT, segment.END.LNG))

        df = pd.DataFrame(coords)
        df = df.rename(columns={0: "lat", 1: "lng"})
        return df
