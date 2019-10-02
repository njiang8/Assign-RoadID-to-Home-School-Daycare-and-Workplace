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
import multi processing
```

## Data
RaodID: point data extract from each road segment (.shp)
Householde, School, and Daycare: points data(.shp)

## Main Function
```
def assign_rid(data, road):
    
    d_geometry = data.geometry  #location
    #print(d_geometry)
    #Create Buffer for each Home or Work Point
    buff = data.geometry.buffer(0.001)
    #Find Intersected points
    r_in = road[road.intersects(buff)]
    #print(len(r_in))

    if r_in.empty:
        buff = data.geometry.buffer(0.02)
        r_in = road[road.intersects(buff)]
            
        h_dist = r_in.distance(d_geometry).sort_values().reset_index()
        
        return h_dist.iloc[0,0]
    
    else:
        h_dist = r_in.distance(d_geometry).sort_values().reset_index()
        return h_dist.iloc[0,0]
```
