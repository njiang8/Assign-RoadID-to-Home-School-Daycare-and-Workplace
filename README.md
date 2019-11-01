# Assign RoadID for Home,School,Daycare and workplaces
How:
* 1 Buffer each household's, schoo's , and daycare's geometry points
* 2 Find road points intersecting the Buffer zone and calculate the distances, assign the closest road point ID
* 3 Create a new column in the dataset by returning the results of road point ID
* 4 Using multiprocessing to release the intensive calculation

## Overall workflow
* 1 Create the center point of each road segments by using the road point ID as the key
* 2 Assign Road ID to School, Daycare, Workplaces, Home
* 3 For the Home, extra efforts are needed, assgin the road point ID to each agent

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
