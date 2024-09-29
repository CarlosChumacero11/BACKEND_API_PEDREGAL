import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

ruta_imagen = 'C:/Users/carlos.chumacero/Pictures/5000orig'

ruta_guardar_imagen="C:/Users/carlos.chumacero/Documents/PaginaPedregal/imagenRGB"
# Función para calcular el NDVI
def calcular_ndvi(nir_band, red_band):
    # Evitar división por cero usando np.where
    ndvi = np.where((nir_band + red_band) == 0, 0, (nir_band - red_band) / (nir_band + red_band))
    return np.clip(ndvi, -1, 1)  # El NDVI está limitado entre -1 y 1

def leerImagenTif(ruta_imagen):
    with rasterio.open(ruta_imagen) as src:
        blue = src.read(1)  # Banda 1
        green = src.read(2)  # Banda 2
        red = src.read(3)    # Banda 3
        nir = src.read(4)    # Banda 4
        rededge=src.read(5) 

        ndvi = calcular_ndvi(nir, red)
        rgb = np.stack((red, green, blue), axis=-1)
        rgb_normalized = np.clip((rgb / rgb.max()) * 255, 0, 255).astype(np.uint8)

        return rgb_normalized

for archivo in os.listdir(ruta_imagen):
    nombre_archivo, extension_imagen = os.path.splitext(archivo)
    if extension_imagen.lower() == ".tif":
        ruta_imgen_rgb = os.path.join(ruta_imagen, archivo)
        rgb_tif = leerImagenTif(ruta_imgen_rgb)
        plt.imsave(ruta_guardar_imagen+"/"+nombre_archivo+".png", rgb_tif)

# for archivo in os.listdir(ruta_imagen):
#     ruta_imagen_tif = os.path.join(ruta_imagen, archivo)
#     print(ruta_imagen_tif)


    

# # Abrir la imagen TIFF
# with rasterio.open(ruta_imagen) as src:
#     blue = src.read(1)  # Banda 1
#     green = src.read(2)  # Banda 2
#     red = src.read(3)    # Banda 3
#     nir = src.read(4)    # Banda 4
#     rededge=src.read(5)
#     # Calcular el NDVI para la imagen completa
#     ndvi = calcular_ndvi(nir, red)

#     # Crear una imagen RGB normalizada para la visualización
#     rgb = np.stack((red, green, blue), axis=-1)
#     rgb_normalized = np.clip((rgb / rgb.max()) * 255, 0, 255).astype(np.uint8)

# # Configurar la visualización de la ortofoto
# plt.imshow(rgb_normalized)
# # fig, ax = plt.subplots(figsize=(10, 10))
# # ax.imshow(rgb_normalized)
# plt.axis("off")
# plt.imsave("IMG_0195.png",rgb_normalized)

