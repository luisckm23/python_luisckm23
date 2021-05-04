import os, shutil 

# Crear una carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# Eliminar carpeta
#os.rmdir("./mi_carpeta")

# Copiar una carpeta

ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

shutil.copyfile(ruta_original, ruta_nueva)