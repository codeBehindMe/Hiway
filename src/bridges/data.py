import geopandas as gpd


class BridgeData:
    def __init__(self, path_to_file: str) -> None:
        self.bridges: gpd.GeoDataFrame = gpd.read_file(path_to_file)

    def get_processed_df(self) -> gpd.GeoDataFrame:
        """
        Returns a dataframe, but adds a few columns such as lat and long for
        convenience.
        """
        self.bridges["lng"] = self.bridges["geometry"].apply(lambda p: p.x)
        self.bridges["lat"] = self.bridges["geometry"].apply(lambda p: p.y)

        return self.bridges
