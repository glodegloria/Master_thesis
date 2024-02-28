import math
import pandas as pd

def illogical_positions(modis_stack, years):
    ilpo=[]
    for a in range(len(years)-1):
        for i in range(483):
            for j in range(689):
                if modis_stack[a][0,i,j]==1 and modis_stack[a+1][0,i,j]==4:
                    ilpo.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==2 and modis_stack[a+1][0,i,j]==4:
                    ilpo.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==3 and modis_stack[a+1][0,i,j]==4:
                    ilpo.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==4 and modis_stack[a+1][0,i,j]==1:
                    ilpo.append([years[a],i,j])
    return ilpo

def table_X(rf, ilpo, modis_stack_NDVI, years, modis_stack_population, modis_stack_radiation, modis_stack_DSMP, modis_stack_precipitation, modis_stack_temperature, modis_stack_production, modis_stack_fragmentation):
    from cosa import main as ReductionIllogical

    X_illo=[["NDVI","DSMP","Population","Radiation","Precipitation","Temperature","Production","Fragmentation"]]
    for i in range(len(ilpo)):
        r=[]
        if math.isnan(float(modis_stack_NDVI[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_NDVI[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_NDVI[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        r.append(modis_stack_DSMP[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        r.append(modis_stack_population[0][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_radiation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_radiation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_radiation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        if math.isnan(float(modis_stack_precipitation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_precipitation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_precipitation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        if math.isnan(float(modis_stack_temperature[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_temperature[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_temperature[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        if math.isnan(float(modis_stack_production[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_production[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_production[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        if math.isnan(float(modis_stack_fragmentation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_fragmentation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_fragmentation[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        X_illo.append(r)
        nombres_columnas = X_illo[0]

        X_rata = pd.DataFrame(X_illo[1:], columns=nombres_columnas)

    Y=rf.predict(X_rata)
    
    return Y

def NumberIllogical(ilpo, modis_stack, years, Y):
    num_iltra=0
    for i in ilpo:
        if modis_stack[years.index(i[0])][0,i[1],i[2]]!=Y[ilpo.index(i)]:
            num_iltra+=1
    return num_iltra

def main(rf, years, modis_stack, modis_stack_NDVI, modis_stack_population, modis_stack_radiation, modis_stack_DSMP, modis_stack_precipitation, modis_stack_temperature, modis_stack_production, modis_stack_fragmentation):
    
    print ("aaaaaaaaa")
    ilpo=[]
    illo=illogical_positions(modis_stack, years)
    ilpo.append(illogical_positions(modis_stack, years))

    Y=table_X(rf, illo, modis_stack_NDVI, years, modis_stack_population, modis_stack_radiation, modis_stack_DSMP, modis_stack_precipitation, modis_stack_temperature, modis_stack_production, modis_stack_fragmentation)


    modis_stack_final=modis_stack
    #print(modis_stack_final[years.index(illo[0][0])][0,illo[0][1],illo[0][2]])
    for i in illo:
        modis_stack_final[years.index(i[0])][0,i[1],i[2]]=Y[illo.index(i)]

    
    j=0

    while len(ilpo[j]) > 40 and j<60:
        illo=illogical_positions(modis_stack_final, years)
        ilpo.append(illo)
        print(str(ilpo[j][1])+"aaa")
        Y=table_X(rf, illo, modis_stack_NDVI, years, modis_stack_population, modis_stack_radiation, modis_stack_DSMP, modis_stack_precipitation, modis_stack_temperature, modis_stack_production, modis_stack_fragmentation)
        #num_iltra=NumberIllogical(ilpo[j], modis_stack_final, years, Y)
        print("There are"+str(len(ilpo[j]))+" illogical positions")
        for i in illo:
            
            modis_stack_final[years.index(i[0])][0,i[1],i[2]]=Y[illo.index(i)]
        j+=1
    
    return modis_stack_final, ilpo

    
        

    

