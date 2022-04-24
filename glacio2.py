from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
from datetime import datetime, timedelta
import pandas as pd

# Returns a datetime object containing the local date and time
dateTimeObj = datetime.now()-timedelta(days=1)
dateObj = dateTimeObj.date()
# Print the date object

dom_img = pd.read_excel(io='dominio.xlsx', sheet_name='Sheet1')
#print(dom_img.head(5))  # print first 5 rows of the dataframe
x=[]
x.append(dom_img['Dom1'])
cantidad=int(len(x[0])/4)
for borde in range(cantidad):
    #Terra721
    ancho=int((x[0][4*borde+3]-x[0][4*borde+2])/0.004394)
    alto=int((x[0][4*borde]-x[0][4*borde+1])/0.004394)
    my_url= 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME='+str(dateObj)+'T00:00:00Z&BBOX='+str(x[0][4*borde+1])+','+str(x[0][4*borde+2])+','+str(x[0][4*borde])+','+str(x[0][4*borde+3])+'&CRS=EPSG:4326&LAYERS=MODIS_Terra_CorrectedReflectance_Bands721,Coastlines_15m&WRAP=day,x&FORMAT=image/tiff&WIDTH='+str(ancho)+'&HEIGHT='+str(alto)+''
    img1 = uReq(my_url)
    print("Bajando TERRA721 sector"+str(borde+1)+"..")
    imagefile = open(".\Terra721_sector"+str(borde+1)+".tiff",'wb')
    imagefile.write(img1.read())
    imagefile.close()
    # Terra367
    my_url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME='+str(dateObj)+'T00:00:00Z&BBOX='+str(x[0][4*borde+1])+','+str(x[0][4*borde+2])+','+str(x[0][4*borde])+','+str(x[0][4*borde+3])+'&CRS=EPSG:4326&LAYERS=MODIS_Terra_CorrectedReflectance_Bands367,Coastlines_15m&WRAP=day,x&FORMAT=image/tiff&WIDTH='+str(ancho)+'&HEIGHT='+str(alto)+''
    img2 = uReq(my_url)
    print("Bajando TERRA367 sector"+str(borde+1)+"..")
    imagefile = open(".\Terra367_sector"+str(borde+1)+".tiff", 'wb')
    imagefile.write(img2.read())
    imagefile.close()

    # TerraVis
    my_url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME=' + str(dateObj) + 'T00:00:00Z&BBOX='+str(x[0][4*borde+1])+','+str(x[0][4*borde+2])+','+str(x[0][4*borde])+','+str(x[0][4*borde+3])+'&CRS=EPSG:4326&LAYERS=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines_15m&WRAP=day,x&FORMAT=image/tiff&WIDTH='+str(ancho)+'&HEIGHT='+str(alto)+''
    img3 = uReq(my_url)
    print("Bajando TERRA VIS sector"+str(borde+1)+"..")
    imagefile = open(".\TerraVIS_sector"+str(borde+1)+".tiff", 'wb')
    imagefile.write(img3.read())
    imagefile.close()

    # AquaVis
    my_url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME=' + str(dateObj) + 'T00:00:00Z&BBOX='+str(x[0][4*borde+1])+','+str(x[0][4*borde+2])+','+str(x[0][4*borde])+','+str(x[0][4*borde+3])+'&CRS=EPSG:4326&LAYERS=MODIS_Aqua_CorrectedReflectance_TrueColor,Coastlines_15m&WRAP=day,x&FORMAT=image/tiff&WIDTH='+str(ancho)+'&HEIGHT='+str(alto)+''
    img4 = uReq(my_url)
    print("Bajando AQUA VIS sector"+str(borde+1)+"..")
    imagefile = open(".\AquaVIS_sector"+str(borde+1)+".tiff", 'wb')
    imagefile.write(img4.read())
    imagefile.close()

    # Aqua721
    my_url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME=' + str(dateObj) + 'T00:00:00Z&BBOX='+str(x[0][4*borde+1])+','+str(x[0][4*borde+2])+','+str(x[0][4*borde])+','+str(x[0][4*borde+3])+'&CRS=EPSG:4326&LAYERS=MODIS_Aqua_CorrectedReflectance_Bands721,Coastlines_15m&WRAP=day,x&FORMAT=image/tiff&WIDTH='+str(ancho)+'&HEIGHT='+str(alto)+''
    img5 = uReq(my_url)
    print("Bajando AQUA721 sector"+str(borde+1)+"..")
    imagefile = open(".\Aqua721_sector"+str(borde+1)+".tiff", 'wb')
    imagefile.write(img5.read())
    imagefile.close()


print("Ya terminó con todo, revisar si descargó")