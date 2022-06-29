#Se abre un archivo
archivo = open("./data/don_quijote.txt", "r")

#Leo el archivo
texto = archivo.read()

#Se cierra un archivo
archivo.close()

#Crear un archivo de copia
archivo_copia = open("./data/copia.txt", "w")

#Se copia un archivo de un lado a otro
archivo_copia.write(texto)

#Archivo se cierra
archivo_copia.close()