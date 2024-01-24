import numpy as np
import matplotlib.pyplot as plt

def main(modis_stack, change_map, years, etiqueta2):
    cambio=[[0 for k in range(5)] for o in range(5)]
    come=[[0 for k in range(5)] for o in range(5)]

    for a in range(len(years)-1):
        for i in range(483):
            for j in range(689):
                if change_map[a][0,i,j]!=0 and modis_stack[a][0,i,j]!=-30 and modis_stack[a+1][0,i,j]!=-30:
                    cambio[modis_stack[a][0,i,j]-1][modis_stack[a+1][0,i,j]-1]+=1
                    come[modis_stack[a+1][0,i,j]-1][modis_stack[a][0,i,j]-1]+=1

    list_time_series=[[0 for k in range(len(years))] for i in range(len(etiqueta2))]
    for a in range(len(years)):
        for i in range(483):
            for j in range(689):
                if modis_stack[a][0,i,j]!=-30:
                    list_time_series[modis_stack[a][0,i,j]-1][a]+=1

    landcover=list(range(5))
    X_axis = np.arange(len(landcover)) 

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

    illogical_positions=[]
    for a in range(len(years)-1):
        for i in range(483):
            for j in range(689):
                if modis_stack[a][0,i,j]==1 and modis_stack[a+1][0,i,j]==4:
                    print("En la posicion ("+str(i)+","+str(j)+") ha cambiado de forest a waterbody")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==2 and modis_stack[a+1][0,i,j]==4:
                    print("En la posicion ("+str(i)+","+str(j)+") ha cambiado de grassland a waterbody")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==3 and modis_stack[a+1][0,i,j]==4:
                    print("En la posicion ("+str(i)+","+str(j)+") ha cambiado de cropland a waterbody")
                    illogical_positions.append([years[a],i,j])
                elif modis_stack[a][0,i,j]==4 and modis_stack[a+1][0,i,j]==1:
                    print("En la posicion ("+str(i)+","+str(j)+") ha cambiado de waterbody a forest")
                    illogical_positions.append([years[a],i,j])
    try:
        return(illogical_positions)
    except:
        print("no se ha podido pasar")
