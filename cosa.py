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

def table_X(rf, ilpo, modis_stack_NDVI, years, modis_stack_drought, modis_stack_elevation, modis_stack_DSMP):
    X_illo=[["NDVI","Drought","Elevation","DSMP"]]
    for i in range(len(ilpo)):
        r=[]
        if math.isnan(float(modis_stack_NDVI[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==False:
            r.append(modis_stack_NDVI[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        if math.isnan(float(modis_stack_NDVI[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]]))==True:
            r.append(0)
        r.append(modis_stack_drought[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        r.append(modis_stack_elevation[0,ilpo[i][1],ilpo[i][2]])
        r.append(modis_stack_DSMP[years.index(ilpo[i][0])][0,ilpo[i][1],ilpo[i][2]])
        X_illo.append(r)

    nombres_columnas = X_illo[0]

    X_illo = pd.DataFrame(X_illo[1:], columns=nombres_columnas)

    Y=rf.predict(X_illo)
    
    return Y

def NumberIllogical(ilpo, modis_stack, years, Y):
    num_iltra=0
    for i in ilpo:
        if modis_stack[years.index(i[0])][0,i[1],i[2]]!=Y[ilpo.index(i)]:
            num_iltra+=1
    return num_iltra

def main(rf, years, modis_stack, modis_stack_NDVI, modis_stack_drought, modis_stack_elevation, modis_stack_DSMP):
    

    ilpo=illogical_positions(modis_stack, years)

    Y=table_X(rf, ilpo, modis_stack_NDVI, years, modis_stack_drought, modis_stack_elevation, modis_stack_DSMP)

    num_iltra=NumberIllogical(ilpo, modis_stack, years, Y)   

    modis_stack_final=modis_stack
    for i in ilpo:
        modis_stack_final[years.index(i[0])][0,i[1],i[2]]=Y[ilpo.index(i)] 

    while len(ilpo) > 40:
        ilpo=illogical_positions(modis_stack_final, years)
        print(ilpo[1])
        Y=table_X(rf, ilpo, modis_stack_NDVI, years, modis_stack_drought, modis_stack_elevation, modis_stack_DSMP)
        num_iltra=NumberIllogical(ilpo, modis_stack_final, years, Y)
        print("There are"+str(len(ilpo))+" illogical positions")
        for i in ilpo:
            modis_stack_final[years.index(i[0])][0,i[1],i[2]]=Y[ilpo.index(i)]
    
    return modis_stack_final

    
        

    

