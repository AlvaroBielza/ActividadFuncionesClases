def histograma(lista_nums):
    c='*'
    for i in lista_nums:
        print(c*i)


numLista_str=input('cuantas filas desea poner')
num_lista=int(numLista_str)
lista=[]
for i in range(num_lista):
    num_str=input('introduce un numero:')
    num=int(num_str)
    lista.append(num)
histograma(lista)

