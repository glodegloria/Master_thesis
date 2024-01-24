def change_label(modis_stack):
    etiqueta=['EvergreenConiferousForest', 'OpenDeciduousBroadleafForest', 'Shrubland', 'Mangrove', 'OpenDeciduousConiferousForest', 'WaterBody', 'BareArea', 'ClosedDecidousBroadleafForest', 'ClosedDeciduousConiferousForest', 'BeachDuneAndSand', 'Grassland', 'OpenSavanna', 'DeciduousBroadleafforest', 'sparseShrubCover', 'artificialSurface', 'OpenEvergreenConiferousForest', 'SparseTreeCover', 'NonIrregatedArableLandHerbaceous', 'closedEvergreenConiferousforest', 'NonIrrigatedArableLand', 'ClosedSavanna', 'AgriculturalLandWithNaturalVegetation', 'evergreeenBroadleadForest', 'PermanentlyIrrigatedArableLand', 'DeciduousConferousForest', 'MixedForest', 'ComplexCultivationPatternedLand', 'InlandSwamp', 'GlacierPerpetualSnow', 'evergreenShrubland', 'LichenMoss', 'DeciduousShrubland', 'BareRock', 'SparseVegetation', 'SparseHerbaceousCover', 'PermanentCropland', 'Wetland']
    print(len(etiqueta))

    forest=[]
    cropland=[]
    grassland=[]
    waterbody=[]
    built_up=[]

    forest.append(etiqueta.index("EvergreenConiferousForest"))
    forest.append(etiqueta.index("OpenDeciduousBroadleafForest"))
    grassland.append(etiqueta.index("Shrubland"))
    forest.append(etiqueta.index("Mangrove")) 
    forest.append(etiqueta.index("OpenDeciduousConiferousForest"))
    waterbody.append(etiqueta.index("WaterBody"))
    grassland.append(etiqueta.index("BareArea"))
    forest.append(etiqueta.index("ClosedDecidousBroadleafForest"))
    forest.append(etiqueta.index("ClosedDeciduousConiferousForest"))
    waterbody.append(etiqueta.index("BeachDuneAndSand"))
    grassland.append(etiqueta.index("Grassland"))
    grassland.append(etiqueta.index("OpenSavanna"))
    forest.append(etiqueta.index("DeciduousBroadleafforest"))
    grassland.append(etiqueta.index("sparseShrubCover"))
    built_up.append(etiqueta.index("artificialSurface"))
    forest.append(etiqueta.index("OpenEvergreenConiferousForest"))
    grassland.append(etiqueta.index("SparseTreeCover"))
    cropland.append(etiqueta.index("NonIrregatedArableLandHerbaceous"))
    forest.append(etiqueta.index("closedEvergreenConiferousforest"))
    cropland.append(etiqueta.index("NonIrrigatedArableLand"))
    grassland.append(etiqueta.index("ClosedSavanna"))
    cropland.append(etiqueta.index("AgriculturalLandWithNaturalVegetation"))
    forest.append(etiqueta.index("evergreeenBroadleadForest"))
    cropland.append(etiqueta.index("PermanentlyIrrigatedArableLand"))
    forest.append(etiqueta.index("DeciduousConferousForest"))
    forest.append(etiqueta.index("MixedForest")) 
    cropland.append(etiqueta.index("ComplexCultivationPatternedLand"))
    waterbody.append(etiqueta.index("InlandSwamp"))
    grassland.append(etiqueta.index("GlacierPerpetualSnow"))
    grassland.append(etiqueta.index("evergreenShrubland"))
    grassland.append(etiqueta.index("LichenMoss"))
    grassland.append(etiqueta.index("DeciduousShrubland"))
    grassland.append(etiqueta.index("BareRock"))
    grassland.append(etiqueta.index("SparseVegetation"))
    grassland.append(etiqueta.index("SparseHerbaceousCover"))
    cropland.append(etiqueta.index("PermanentCropland"))
    waterbody.append(etiqueta.index("Wetland"))

    for i in range(483):
        for j in range(689):
            for a in range(len(modis_stack)):
                if modis_stack[a][0,i,j] in forest:
                    modis_stack[a][0,i,j]=1
                elif modis_stack[a][0,i,j] in cropland:
                    modis_stack[a][0,i,j]=2
                elif modis_stack[a][0,i,j] in waterbody:
                    modis_stack[a][0,i,j]=4
                elif modis_stack[a][0,i,j] in built_up:
                    modis_stack[a][0,i,j]=5
                elif modis_stack[a][0,i,j] in grassland:
                    modis_stack[a][0,i,j]=3

    return modis_stack


