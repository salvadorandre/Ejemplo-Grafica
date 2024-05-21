import matplotlib.pyplot as mat
import numpy as np

valor_graficar = input('Ingrese una funcion de x "ejemplo, x**2 + 2*x - 1": ')

def grafico(x):
    return eval(valor_graficar)
x = np.linspace(-5, 5, 400)  

y = grafico(x)

mat.plot(x, y, label= f'f(x) = {valor_graficar}')

mat.title(f'Gráfica de la función f(x) = {valor_graficar}')
mat.xlabel('x')
mat.ylabel('f(x)')


mat.legend()

mat.grid(True)
mat.show()
