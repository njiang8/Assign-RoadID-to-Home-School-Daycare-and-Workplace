import geopandas as gpd
import pandas as pd
import numpy as np
import timeit

print("Reading Data...")
#Raod Data
rp = gpd.read_file('/scratch/njiang8/edu/road_w_census.shp')
#rp = rp.drop(['fid'], 1)
rp = rp.set_index('RPID')
#Population Data
pop = gpd.read_file('/scratch/njiang8/edu/daycare_wid.shp')

def gen_road(pop, road):
    p = []
    r = []
    
    for i in pop.index:
        #print('\n This is loop ', i)
        #Buffer
        buff = pop.loc[i,'geometry'].buffer(0.001)
        #Find Intersected points
        r_in = road[road.intersects(buff)]
        #print('first buffer', r_in.shape)
        
        if r_in.empty:
            buff = pop.loc[i,'geometry'].buffer(0.02)
            r_in = road[road.intersects(buff)]
            #print('2nd buffer', r_in.shape)
            h_dist = r_in.distance(pop.loc[i,'geometry']).sort_values().reset_index()
            pid = pop.loc[i,'dcID']
            #print('2nd pid', pid)
            rid = h_dist.iloc[0,0]

        else:
            h_dist = r_in.distance(pop.loc[i,'geometry']).sort_values().reset_index()
            pid = pop.loc[i,'dcID']
            #print('2nd pid', pid)
            rid = h_dist.iloc[0,0]

        
        p.append(pid)
        r.append(rid)


    prid = pd.DataFrame({'dcID': p, 'rdID': r})
    return prid

if __name__=='__main__':
    print('Start running...')
    #set timer
    start_time = timeit.default_timer()
    
    #Apply gen_road Function
    df = gen_road(pop, rp)
    
    print('Saving...')
    df.to_csv('/scratch/njiang8/edu/daycare_rid.csv')
    
    #End timer
    elapsed = timeit.default_timer() - start_time
    print('job total time (seconds):', elapsed)
    print('End program')
