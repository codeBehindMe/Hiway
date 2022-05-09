from typing import List, Dict
import googlemaps as gmaps
from dataclasses import dataclass


@dataclass
class ValidAddress:
    FORMATTED_ADDRESS: str
    LAT: float
    LNG: float


class AddressFinder:
    def __init__(self, google_maps_key: str) -> None:
        self.client = gmaps.Client(key=google_maps_key)

    def _is_partial_match(res_dict: Dict) -> bool:
        if "partial_match" in res_dict.keys():
            return True
        return False

    def find_address(self, addr: str) -> ValidAddress:
        # Indexing to zero as it returns as a json list.
        # So far i've only ever noticed 1 element in this list.
        res: Dict = self.client.geocode(addr, components={"country": "au"})[0]

        # FIXME: Implement partial match logic
        return ValidAddress(
            res["formatted_address"],
            res["geometry"]["location"]["lat"],
            res["geometry"]["location"]["lng"],
        )
