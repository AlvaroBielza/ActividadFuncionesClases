

def funcion(num):
    return num*num

lista=[1,2,3,4,5,6]
lista2=[]
def funcionlista(funcion,lista):

    for i in lista:
        lista2.append(funcion(i))
    return lista2

print(funcionlista(funcion,lista))
