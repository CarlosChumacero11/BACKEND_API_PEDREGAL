import os 
from PIL import Image
ruta_imagen = "C:/Users/carlos.chumacero/Pictures/5000orig"

numero_imagen = 80
for archivo in os.listdir(ruta_imagen):
    nombre_archivo, extension_imagen = os.path.splitext(archivo)
    if extension_imagen.lower() == ".tif" and str(numero_imagen) in nombre_archivo:
        ruta_imagen = os.path.join(ruta_imagen, archivo)
        print(ruta_imagen)


imagen = Image.open("C:/Users/carlos.chumacero/Pictures/5000orig/IMG_0080.tif")
print(imagen)