diccionario= {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4}
def califica_palabras(diccionario):
    for asignaturas in diccionario:
        if(diccionario[asignaturas]<5):
            diccionario[asignaturas]='suspenso'
        elif(5<=diccionario[asignaturas]<7):
            diccionario[asignaturas]='aprobado'
        elif(7<=diccionario[asignaturas]<9):
            diccionario[asignaturas]='notable'
        elif(9<=diccionario[asignaturas]<=10):
            diccionario[asignaturas]='sobresaliente'
        elif(diccionario[asignaturas]>10):
            diccionario[asignaturas] = 'Error'
    return diccionario
print(califica_palabras(diccionario))