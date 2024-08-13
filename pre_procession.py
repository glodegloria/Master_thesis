import rasterio
from rasterio.plot import show, show_hist
from matplotlib import pyplot
import numpy as np
from utilities import change_label
import math
import csv
import matplotlib.pyplot as plt



senegal_coordinates = (-17.535, 12.332, -11.345, 16.691)

print("start connecting")
modis_stack = []
years=list(range(1992,2021))
for i in years:
        with rasterio.open(f'landcover/landcover_cambiada_{i}.tif') as src:
            data = src.read().astype(np.int16)  # Lee la primera banda y convierte a int16
            modis_stack.append(data)
       # length()
print("Se ha cargado Lancover")

print(modis_stack[years.index(2003)])

print("start connecting")
modis_stack_NDVI = []
years=list(range(1992,2021))
for i in years:
        with rasterio.open(f'NDVI/NDVI_{i}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_NDVI.append(data)
       # length()
print("Se ha cargado el NDVI")

print("start connecting")
modis_stack_precipitation = []
for j in years:
     with rasterio.open(f'precipitation/volume_{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_precipitation.append(data)
       # length()
print("Se ha cargao la precipitation")

print("start connecting")
modis_stack_temperature = []
for j in years:
     with rasterio.open(f'temperature/atmosphere_{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_temperature.append(data)
       # length()
print("Se ha cargado la temperature")

print("start connecting")
modis_stack_drought = []
for j in years:
     with rasterio.open(f'drought/drought_severity{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_drought.append(data)
       # length()
print("Se ha cargado el drought")

print("start connecting")
modis_stack_production = []
for j in years:
     with rasterio.open(f'primary_production/net_{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_production.append(data)
       # length()
print("Se ha cargado la production")

print("start connecting")
modis_stack_radiation = []
for j in years:
     with rasterio.open(f'solar_radiation/radiation{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_radiation.append(data)
       # length()
     print(j)
print("Se ha cargado la radiation")

print("start connecting")
modis_stack_elevation = []
j=0
with rasterio.open(f'elevation.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_elevation=data
       # length()
print("Se ha cargado la elevation")

print("start connecting")
modis_stack_radiation = []
for j in years:
     with rasterio.open(f'solar_radiation/radiation{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_radiation.append(data)
       # length()
print("Se ha cargado la solar radiation")

print("start connecting")
modis_stack_production = []
for j in years:
     with rasterio.open(f'primary_production/net_{j}.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_production.append(data)
       # length()
print("Se ha cargao la npp")

print("start connecting")
modis_stack_DSMP = []
years2=list(range(1992,2014))
for j in years2:
     with rasterio.open(f'datos_dsmp/dsmp_{j}_100m.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_DSMP.append(data)
       # length()
print("Se ha cargao la dsmp")

print("start connecting")
modis_stack_population = []
years3=[1995,2010]
for j in years3:
     with rasterio.open(f'asentamientos/poblacion_{j}_100m.tif') as src:
            data = src.read().astype(np.float16)
            modis_stack_population.append(data)
       # length()
print("Se ha cargao la population")


#we save in a vector the pixels that doesn't have changed from one year to the next one

difference=[]
change_map=[]
for a in range(len(years)-1):
    diff = np.abs(modis_stack[a] - modis_stack[a + 1]).astype(np.int16)
    difference.append(diff)
    change_map.append(np.where(difference[a] > 0, 1, 0))
print(change_map[0].shape)

#we save in a vector the pixels that doesn't have changed from 1990 to 2010

change_total=np.zeros([4823,6886], dtype=int)
for i in range(4823):
    for j in range(6886):
        for a in range(len(years)-1):#len(years) because there have been 1 less change than the number of years
            if change_map[a][0,i,j]!=0:
                change_total[i,j]+=1#it's greater than 1 if there is change, it's 0 if there is not change

print("se ha hecho change_total")

change_positions=[]
a=0
for i in range(4823):
    for j in range(6886):
        if change_total[i,j]==0: 
            change_positions.append([i,j])
            #print(change_positions[a])

print(f'There are {len(change_positions)} who has not have changed')

#measures how many points are of each area in year 2003 (we have selected this year because itt is in the middle between 1992 and 2010)

total_terrestrial=0
total_landcover=np.zeros(6, dtype=int)
for i in range(4823):
    for j in range(6886):
        #if modis_stack[years.index(2003)][0,i,j]!=-30:
            total_landcover[modis_stack[years.index(2003)][0,i,j]]+=1
            total_terrestrial+=1

print("Porcentaje of each area")

porcentaje_landcover=[x / (total_terrestrial) * 100 for x in total_landcover]

print(total_landcover)
print(porcentaje_landcover)

print("we measure how much area there is where it doesn't have changed")

total_terrestrial_equal=0
total_landcover_equal=np.zeros(6, dtype=int)
for i in change_positions:#if the point doesn't have changed
    #print(modis_stack[years.index(2003)][0,i,j])
    total_landcover_equal[modis_stack[years.index(2003)][0,i[0],i[1]]]+=1
    total_terrestrial_equal+=1
porcentaje_landcover_equal=[x / total_terrestrial_equal * 100 for x in total_landcover_equal]
print(total_landcover_equal)
print(porcentaje_landcover_equal)

etiqueta2=['forest', 'cropland', 'grassland', 'waterbody', 'built_up']
for i in range(5):
    print(etiqueta2[i]+"The percentage of the selected is:" +str(porcentaje_landcover_equal[i+1])+" the percentage without processing is "+str(porcentaje_landcover[i+1]))

print("create a matrix with the inputs and the outputs of each pixel")

#We create a new array for each variable where it appears, in each position, the mean of all the values that are in the same position

print("Mean of NDVI")

NDVI = np.array(modis_stack_NDVI, dtype=np.float16)

#  Calculate the media in the first axis
media_NDVI = np.mean(NDVI, axis=0)



#Mean of the drought of the soil

print("Mean of the drought")
drought = np.array(modis_stack_drought, dtype=np.float16)

media_drought = np.mean(drought, axis=0)

#Mean of the luminosity (DSMP)
print("Mean of DSMP")
DSMP = np.array(modis_stack_DSMP, dtype=np.float16)

media_DSMP = np.mean(DSMP, axis=0)

#Mean of the radiation

print("Mean of radiation")

Rad = np.array(modis_stack_radiation[3:], dtype=np.float16)#It starts in 3, because the all the other data has nan in all the positions

# Calculamos la media a lo largo del primer eje (axis=0)
media_rad = np.mean(Rad, axis=0)

#Mean of the precipitation volume

print("Mean of precipitation")

prep = np.array(modis_stack_precipitation[3:], dtype=np.float16)#We start in 3 for the same reason as in radiation

media_prep = np.mean(prep, axis=0)

#Mean of the atmospheric temperature

print("Mean of temperature")

temp = np.array(modis_stack_temperature, dtype=np.float16)

# Calculamos la media a lo largo del primer eje (axis=0)
media_temp = np.mean(temp, axis=0)

print(media_temp.shape)

#Mean of the net primary production

print("Mean of npp")

prod = np.array(modis_stack_production, dtype=np.float16)

media_prod = np.mean(prod, axis=0)

print(media_prod.shape)

print("Creamos tabla")

information=[["NDVI","Drought","Elevation","DSMP","Population","Radiation","Precipitation","Temperature","Production","Fragmentation","Position","Landcover"]]
j=0
for i in change_positions:
    r=[]
    j+=1
    if math.isnan(float(media_temp[0,i[0],i[1]]))==False and math.isnan(float(media_rad[0,i[0],i[1]]))==False:
        if math.isnan(float(media_NDVI[0,i[0],i[1]]))==False:
            r.append(media_NDVI[0,i[0],i[1]])
        if math.isnan(float(media_NDVI[0,i[0],i[1]]))==True:
            r.append(0)
        r.append(media_drought[0,i[0],i[1]])
        if math.isnan(float(modis_stack_elevation[0,i[0],i[1]]))==False:
            r.append(modis_stack_elevation[0,i[0],i[1]])
        if math.isnan(float(modis_stack_elevation[0,i[0],i[1]]))==True:
            r.append(0)
        r.append(media_DSMP[0,i[0],i[1]])
        r.append(modis_stack_population[0][0,i[0],i[1]])
        if math.isinf(float(media_rad[0,i[0],i[1]]))==False:
            r.append(media_rad[0,i[0],i[1]])
        if math.isinf(float(media_rad[0,i[0],i[1]]))==True:
            r.append(0)
        if math.isnan(float(media_prep[0,i[0],i[1]]))==False:
            r.append(media_prep[0,i[0],i[1]])
        if math.isnan(float(media_prep[0,i[0],i[1]]))==True:
            r.append(0)
        if math.isnan(float(media_temp[0,i[0],i[1]]))==False:
            r.append(media_temp[0,i[0],i[1]])
        if math.isnan(float(media_temp[0,i[0],i[1]]))==True:
            r.append(0)
        if math.isnan(float(media_prod[0,i[0],i[1]]))==False:
            r.append(media_prod[0,i[0],i[1]])
        if math.isnan(float(media_prod[0,i[0],i[1]]))==True:
            r.append(0)
        r.append(i)
        r.append(modis_stack[years.index(2003)][0,i[0],i[1]])
        information.append(r)

print("Guardamos en excel")
with open('information.csv', 'w', newline='') as file:
    # Step 4: Using csv.writer to write the list to the CSV file
    writer = csv.writer(file)
    writer.writerows(information) # Use writerows for nested list





