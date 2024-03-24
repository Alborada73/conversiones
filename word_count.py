
#Ejercicio: Se solicita que el programa lea y cuente cuantas letras contiene el fichero lorem_ipsum.txt
#1ero podemos abrir el fichero con la función open() y como argumento la ruta del fichero que queremos abrir:
lorem_ipsum = open("/Users/yasnaangulo/Python_2024/MODULO_PYTHON/dia_12/lorem_ipsum.txt")
#con read()podemos imprimir el contenido de todo el fichero
#print(lorem_ipsum.read())

   
with open("/Users/yasnaangulo/Python_2024/MODULO_PYTHON/dia_12/lorem_ipsum.txt", "r") as lorem_ipsum:
    texto = lorem_ipsum.read()
    #print(texto)
    #len cuenta la cantidad total de caracteres del texto
    #len(texto)
    #print(len(texto))
    texto.split()
    len(texto)
    print(texto.split())
    #no se cómo contar caracteres distintos !=

