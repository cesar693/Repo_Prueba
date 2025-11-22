#import zipfile
'''
mi_zip=zipfile.ZipFile('archivo_comprimido.zip','w')
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')
mi_zip.close()

zip_abierto=zipfile.ZipFile('archivo_comprimido.zip','r')
zip_abierto.extractall()
'''
import shutil
#carpeta_origen='C:\\Users\\user\\Downloads\\carpeta_superior'
#archivo_destino='todo_comprimido'
#shutil.make_archive(archivo_destino,'zip',carpeta_origen)
shutil.unpack_archive('todo_comprimido.zip','extraccion_terminada','zip')