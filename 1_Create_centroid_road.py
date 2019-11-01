#find mid points of raod segment
#Richard

import pandas as pd
import geopandas as gpd
import numpy as np
import timeit
import multiprocessing

#read file
rl = gpd.read_file('../Shp_Study_Area_Richard/Road_Line/Road_line.shp')

def getXY(pt):
    return (pt.x, pt.y)

def gen_center_point(line):
    #get the center points' lat and long
    centroidseries = line['geometry'].centroid
    x,y = [list(t) for t in zip(*map(getXY, centroidseries))]
    #get Road point ID
    rid = line['ID']
    #get State
    st = line['STATEFP']
    df = pd.DataFrame({'RDID': rid, 'STATE': st, 'Long': x, 'Lat': y})
    return df

#devide the road line shape file into 8 parts in
def parallelize_pdf(pdf, func):
    num_cores = 10  #leave one free to not freeze machine
    num_partitions = num_cores #number of partitions to split dataframe\

    pdf_split = np.array_split(pdf, num_partitions)
    
    pool = multiprocessing.Pool(num_cores)
    pdf = pd.concat(pool.map(func, pdf_split))
    return pdf

    pool.close()
    pool.join()

def to_gpd(data):
    from shapely.geometry import Point
    # combine lat and lon column to a shapely Point() object
    data['geometry'] = data.apply(lambda x: Point((float(x.Long), float(x.Lat))), axis=1)
    geo_rp = gpd.GeoDataFrame(data, geometry='geometry')
    return geo_rp

if __name__=='__main__':
    print('Start Running...')
    start_time = timeit.default_timer()
    #test
    #test1000 = rl[:10000]
    #test_r = parallelize_pdf(test1000, gen_center_point)
    #to geodata frame
    #test_g = to_gpd(test_r)
    #save
    #print('Saving file...')
    #test_g.to_file('test_road_point.shp',driver ='ESRI Shapefile')
    #whole dataframe
    rp = parallelize_pdf(rl, gen_center_point)
    #to gpd
    rp_g = to_gpd(rp)
    rp_g.shape
    #save
    print('Saving file...')
    rp_g.to_file('road_points_Aug_Richard.shp',driver ='ESRI Shapefile')                     
    elapsed = timeit.default_timer() - start_time
    print('job total time (seconds):', elapsed)