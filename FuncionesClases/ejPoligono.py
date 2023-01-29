import math


class Poligono:
    def __init__(self, num_lados):
        if num_lados < 3 :
            raise ValueError('Minimo 3 lados')
        self.num_lados = num_lados
        self.lados = []
        for i in range(num_lados):
            self.lados.append(0)
        return

    def darlados(self):
        for i in range(self.num_lados):
            str = input(f'Introduce el valor del lado {i+1}:')
            try:
                n = int(str)
                self.lados[i] = n
            except Exception as e:
                print('Debes introducir un número')
                return False
        return True

    def verlados(self):
        print(f'Los lados de este poligono son {self.num_lados}: ')
        for i in self.lados:
            print(i,' ', end = '')
        print()


class Triangulo(Poligono):

    def __init__(self):
        Poligono.__init__(self,3)

    def area(self):
        semiperimetro = self.perimetro()/2
        #Heron formula
        a=math.sqrt(semiperimetro*(semiperimetro-self.lados[0])*(semiperimetro-self.lados[1])*(semiperimetro-self.lados[2]))
        return a
    def perimetro(self):
        p = 0
        for l in self.lados:
            p += l
        return p

triangulo1 = Triangulo()
triangulo1.darlados()
triangulo1.verlados()
area = triangulo1.area()
perimetro = triangulo1.perimetro()
print ('el area es: ',area,' y el perimetro es: ',perimetro)