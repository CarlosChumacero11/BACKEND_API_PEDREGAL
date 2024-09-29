import os
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from PIL import Image
import io
app = FastAPI()
#C:\Users\carlos.chumacero\Pictures\5000orig
RUTA_IMAGENES="C:/Users/carlos.chumacero/Pictures/5000orig"
RUTA_IMAGENES_RGB ="D:/5000orig_rgb"
RUTA_IMAGENES_NDVI="D:/5000orig_ndvi"

EXTENSIONES_VALIDAS=[".png",".tif"]

@app.get("/buscar-imagen")
async def read_root(numero_imagen : int = Query(..., description="Numero para buscar la imagen")):
    for archivo in os.listdir(RUTA_IMAGENES):
        nombre_archivo, extension_imagen = os.path.splitext(archivo)
        if extension_imagen.lower() in EXTENSIONES_VALIDAS and str(numero_imagen) in nombre_archivo:
            ruta_imagen = os.path.join(RUTA_IMAGENES, archivo)

            print(ruta_imagen)
            imagen_tif = Image.open(ruta_imagen)

            buffer = io.BytesIO()
            imagen_tif.save(buffer, format="PNG")
            buffer.seek(0)

            return FileResponse(buffer, media_type="imagen/png")
        
    raise HTTPException(status_code=404, detail="Imagen no encontrada")

@app.get("/buscar-imagen-ndvi")
async def read_root(numero_imagen : int = Query(..., description="Numero para buscar la imagen")):
    for archivo in os.listdir(RUTA_IMAGENES_NDVI):
        nombre_archivo, extension_imagen = os.path.splitext(archivo)
        if extension_imagen.lower() in EXTENSIONES_VALIDAS and str(numero_imagen) in nombre_archivo:
            ruta_imagen = os.path.join(RUTA_IMAGENES_NDVI, archivo)

            return FileResponse(ruta_imagen)
        
    raise HTTPException(status_code=404, detail="Imagen no encontrada")

@app.get("/buscar-imagen-rgb")
async def read_root(numero_imagen : int = Query(..., description="Numero para buscar la imagen")):
    for archivo in os.listdir(RUTA_IMAGENES_RGB):
        nombre_archivo, extension_imagen = os.path.splitext(archivo)
        if extension_imagen.lower() in EXTENSIONES_VALIDAS and str(numero_imagen) in nombre_archivo:
            ruta_imagen = os.path.join(RUTA_IMAGENES_RGB, archivo)

            return FileResponse(ruta_imagen)
        
    raise HTTPException(status_code=404, detail="Imagen no encontrada")

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8084, reload=True)

