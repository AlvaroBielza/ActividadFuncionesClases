def palabras_longitud(frase):
    frase_separada=frase.split(' ')
    dicc = {}
    for i in frase_separada:

        dicc[i]=len(i)
    print(dicc)
frase='hola y adios'
palabras_longitud(frase)