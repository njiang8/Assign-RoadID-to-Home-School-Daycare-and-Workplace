# Assign_RoadID_Home_School_Daycare
Assign Road ID to each individual household, school, and daycare.
How:
My idae
*1 Buffer each household's, schoo's , and daycare's geometry points
*2 Find how many road points intersect with the Buffer and calculate the distances, assign the closest one
*3 Return a data with hholdID, RoadID, Long, Lat

##Package Usage
```
import geopandas as gpd
import pandas as pd
import numpy as np
import timeit
```

##Data
RaodID: point data extract from each road segment (.shp)
Householde, School, and Daycare: points data(.shp)

##Main Function
```
def gen_road(home, road):
    h = []
    r = []
    long = []
    lat = []
    
    for i in hp.index:
        buff = home.loc[i,'geometry'].buffer(0.01)
        r_in = road[road.intersects(buff)]
        h_dist = r_in.distance(home.loc[i,'geometry']).sort_values().reset_index()
        
        hid = home.loc[i,'hhold']
        rid = h_dist.iloc[0,0]
        lg = r_in.loc[rid, 'Long']
        lt = r_in.loc[rid, 'Lat']
        
        h.append(hid)
        r.append(rid)
        long.append(lg)
        lat.append(lt)
    
    hrid = pd.DataFrame({'hhold': h, 'SrdID': r, 'Long': long, 'Lat': lat})
    return hrid
```
