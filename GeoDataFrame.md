**GeoDataFrame**: pandas.DataFrame object that has a column with geometry?

1. What is geometry in literal sense?
2. What is the structure?
3. In mathematical terms and computing terms
4. In my case, how will the GTFS for Kenyan transit matatu system fit in our context
5. Is the object from geopandas where we extend pandas to support geospatial or geographic data?

# More questions:

1. Why does geographic data need new ways in pandas and DB?
2. What is geospatial, geographic, and spatial? Is geo in them from geometry...?

NOTICE: IT TAKES ALOT OF IMPORTING NORMAL, BUILDING AN OBJECT THEN APPENDING ON TO IT WHEN EXTENDING OR BUILDING UPON LIBRARIES.

Saw it here in geodataframe.py of geopandas

```py

def _dataframe_set_geometry(self, col, drop=False, inplace=False, crs=None):
    if inplace:
        raise ValueError(
            "Can't do inplace setting when converting from DataFrame to GeoDataFrame"
        )
    gf = GeoDataFrame(self)
    # this will copy so that BlockManager gets copied
    return gf.set_geometry(col, drop=drop, inplace=False, crs=crs)


DataFrame.set_geometry = _dataframe_set_geometry
```

1. Is it true? Is that how they extend upon thing? Or return entirely new object with appended methods/functionality to an obj
2. Is it the common thing?
3. How is it done and what are best practices?

Is it something I will find myself doing often?
