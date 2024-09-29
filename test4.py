import rasterio
import numpy as np
import matplotlib.pyplot as plt


#llamamos a las imágenes
ruta_imagen = "D:/5000orig/IMG_0020.tif"

with rasterio.open(ruta_imagen) as src:
    blue = src.read(1).astype('float64')  # Banda 1
    green = src.read(2).astype('float64')  # Banda 2
    red = src.read(3).astype('float64')    # Banda 3
    nir = src.read(4).astype('float64')    # Banda 4
    rededge=src.read(5).astype('float64')


ndvi = (nir-red)/(nir +red)
print(ndvi)

# Mostrar la imagen y permitir al usuario seleccionar una región
plt.figure(figsize=(6, 5))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()
plt.title("NDVI")


plt.show()