import geopandas as gpd
import pandas as pd
import numpy as np
import timeit


print('Reading Data...')
#read Data
rp = gpd.read_file('/scratch/njiang8/roadid/road_pa.shp')
rp = rp.set_index('RPID')

hp = gpd.read_file('/scratch/njiang8/roadid/home_pa.shp')
hp.columns = ["ID", "hhold", "Lat", "Long", "geometry"]

print('Ready to Run...')

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

if __name__=='__main__':
    print('Start running...')
    #set timer
    start_time = timeit.default_timer()
    
    
    #Apply gen_road Function
    df = gen_road(hp,rp)
    
    print('Saving...')
    df.to_csv('home_rid_pa.csv')
    
    #End timer
    elapsed = timeit.default_timer() - start_time
    
    print('job total time (seconds):', elapsed)
    print('End program')
