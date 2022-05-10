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
