import numpy as np
import matplotlib.pyplot as plt

def main(modis_stack, change_map, years, etiqueta2):
    cambio=[[0 for k in range(5)] for o in range(5)]
    come=[[0 for k in range(5)] for o in range(5)]

    
    #create a list that compares each year with the year before
    #in cambio it saves the pixels that in the beginning they were this landcover and it stop being this landcover
    #in come it saves the pixels that in the beginning they weren't this landcover and it start being this landcover
    
    for a in range(len(years)-1):
        for i in range(483):
            for j in range(689):
                if change_map[a][0,i,j]!=0 and modis_stack[a][0,i,j]!=-30 and modis_stack[a+1][0,i,j]!=-30:
                    cambio[modis_stack[a][0,i,j]-1][modis_stack[a+1][0,i,j]-1]+=1
                    come[modis_stack[a+1][0,i,j]-1][modis_stack[a][0,i,j]-1]+=1

    #a time series with the number of pixels they have
    list_time_series=[[0 for k in range(len(years))] for i in range(len(etiqueta2))]
    for a in range(len(years)):
        for i in range(483):
            for j in range(689):
                if modis_stack[a][0,i,j]!=-30:
                    list_time_series[modis_stack[a][0,i,j]-1][a]+=1

    landcover=list(range(5))
    X_axis = np.arange(len(landcover)) 

    #plots with the bar plots and the graphics of the time series
    for i in range(5):
        plt.subplot(121)
        plt.plot(years,np.array(list_time_series[i], dtype=int))
        plt.xlabel("Year")
        plt.ylabel(etiqueta2[i])
        plt.title("Time serie")

        plt.subplot(122)
        plt.bar(X_axis-0.2, cambio[i], width = 0.4, label="Have gone")
        plt.bar(X_axis+0.2, come[i], width = 0.4, label="Have come")
        plt.xlabel("Landcover")
        plt.ylabel("Pixels")
        plt.title("Change of landcover")
        plt.legend()

        plt.suptitle("Landcover change of "+etiqueta2[i])
        plt.show()

    #a list that saves the positions of the illogical transformations
    illogical_positions=[]
    illogical_changes=[]
    for a in range(len(years)-1):
        for i in range(483):
            for j in range(689):
                if modis_stack[a][0,i,j]==1 and modis_stack[a+1][0,i,j]==4:
                    print("In the position ("+str(i)+","+str(j)+"), it has changed from forest to waterbody")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==2 and modis_stack[a+1][0,i,j]==4:
                    print("In the position ("+str(i)+","+str(j)+"), it has changed from grassland to waterbody")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==3 and modis_stack[a+1][0,i,j]==4:
                    print("In the position ("+str(i)+","+str(j)+"), it has changed from cropland to waterbody")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==4 and modis_stack[a+1][0,i,j]==1:
                    print("In the position ("+str(i)+","+str(j)+"), it has changed from waterbody to forest")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==5 and modis_stack[a+1][0,i,j]==1:
                    print("In the position ("+str(i)+","+str(j)+"), it has changed from built-up to forest")
                    illogical_positions.append([years[a],i,j])
    try:
        return(illogical_positions)
    except:
        print("no se ha podido pasar")
