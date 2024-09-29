import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

#llamamos a las imágenes
ruta_imagen_tif = "C:/Users/carlos.chumacero/Pictures/5000orig"
ruta_guardar_imagen = "C:/Users/carlos.chumacero/Documents/PaginaPedregal/imagenNDVI"
def leerImagenTifANDVI(ruta_imagen):
    with rasterio.open(ruta_imagen) as src:
        blue = src.read(1).astype('float64')  # Banda 1
        green = src.read(2).astype('float64')  # Banda 2
        red = src.read(3).astype('float64')    # Banda 3
        nir = src.read(4).astype('float64')    # Banda 4
        rededge=src.read(5).astype('float64')
    
    ndvi = (nir-red)/(nir +red)
    return ndvi

for archivo in os.listdir(ruta_imagen_tif):
    nombre_archivo, extension_imagen = os.path.splitext(archivo)
    if extension_imagen.lower() == ".tif":
        ruta_imgen_rgb = os.path.join(ruta_imagen_tif, archivo)
        rgb_tif = leerImagenTifANDVI(ruta_imgen_rgb)
        
        plt.imsave(ruta_guardar_imagen+"/"+nombre_archivo+".png", rgb_tif)




# for archivo in os.listdir(ruta_imagen_tif):
#     nombre_arvhivo, extension_imagen = os.path.splitext(archivo)
#     if extension_imagen.lower() == ".tif":
#         ruta_imagen_ndvi = os.path.join(ruta_imagen_tif, archivo)
#         ndvi_tif = leerImagenTifANDVI(ruta_imagen_ndvi)
#         plt.colorbar()
#         plt.imsave(ruta_guardar_iamgen+"/"+nombre_arvhivo+".png", ndvi_tif)


# with rasterio.open(ruta_imagen) as src:
#     blue = src.read(1).astype('float64')  # Banda 1
#     green = src.read(2).astype('float64')  # Banda 2
#     red = src.read(3).astype('float64')    # Banda 3
#     nir = src.read(4).astype('float64')    # Banda 4
#     rededge=src.read(5).astype('float64')


# ndvi = (nir-red)/(nir +red)

# # Mostrar la imagen y permitir al usuario seleccionar una región
# plt.figure(figsize=(6, 5))
# plt.imshow(ndvi, cmap='RdYlGn')
# plt.colorbar()
# plt.title("NDVI")


# plt.show()