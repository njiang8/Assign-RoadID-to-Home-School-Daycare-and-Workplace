# Assign RoadID for Home,School,Daycare and workplaces
How:
My idae
* 1 Buffer each household's, schoo's , and daycare's geometry points
* 2 Find how many road points intersect with the Buffer and calculate the distances, assign the closest one
* 3 Create a new column in the dataset by returning the results of road ID
* 4 Using multiprocessing to release the intensive calculation

## Package Usage
```
import geopandas as gpd
import pandas as pd
import numpy as np
import timeit
import multiprocessing
from math import sin, cos, sqrt, atan2, radians
```

## Data
* RaodID: point data extract from each road segment (.shp)
* Householde, School, Daycare and work places: points data(.shp)

## Main Function
New Distance function
```
def new_distance(x1, y1, x2, y2):
    # approximate radius of earth in km
    R = 6373.0
    
    lat1 = radians (x1)
    long1 = radians (y1)
    lat2 = radians(x2)
    long2 = radians(y2)
    
    dlon = long2 - long1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
```
