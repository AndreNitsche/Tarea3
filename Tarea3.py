# Andre Nitsche Rodriguez - B55067 - Grupo 1 

# Librerias
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

# Importamos los datos
xy=pd.read_csv('xy.csv')
xyp=pd.read_csv('xyp.csv')

# Pregunta 1

# En seguida realizamos la sumatoria de las columnas y de las filas
fX=np.sum(xy, axis=1)
fY=np.sum(xy, axis=0)
#Y las imprimimos para verificar
print('fX = ',fX)
print('fy = ',fY)

# Procedemos a crear los vectores de X y de Y
Xs=np.linspace(5,15,11)
Ys=np.linspace(5,25,21)
#Y las imprimimos para verificar
print(Xs)
print(Ys)

# Ahora graficamos fX
plt.plot(Xs, fX)
plt.savefig('CurvafX.jpg')
plt.grid(True)
plt.title('PMF de X')
plt.ylabel('Probabilidad de ocurrencia')
plt.xlabel('X')
plt.cla()

#En seguida graficamos fY
plt.plot(Ys, fY[1:])
plt.savefig('CurvafY.jpg')
plt.grid(True)
plt.title('PMF de Y')
plt.ylabel('Probabilidad de ocurrencia')
plt.xlabel('Y')
plt.cla()

# Podemos observar que ambas presentan una distribuicion similar a la gaussiana

# Ahora definimos la funcion de la campana de Gauss
def gaussiana(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

# Utilizamos el curvefit para obtener mu y sigma
parametroX , _ = curve_fit(gaussiana, Xs, fX)
gaussianaX = gaussiana(Xs, parametroX[0], parametroX[1])
#Comprobamos los valores de mu y sigma para X
print(parametroX)

parametroY , _ = curve_fit(gaussiana, Ys, fY[1:])
gaussianaY = gaussiana(Ys, parametroY[0], parametroY[1])
# Comprobamos los valores de mu y sigma para Y
print(parametroY)

# A continuacion realizamos la curva de mejor ajuste para la funcion marginal de X
plt.cla()
plt.plot(Xs, gaussianaX)
plt.savefig('CurvaMejorAjusteX.jpg')
plt.grid(True)
plt.title('Curva de mejor ajuste para la funcion marginal de X')
plt.ylabel('Probabilidad de ocurrencia')
plt.xlabel('X')
plt.cla()


# En seguida realizamos la curva de mejor ajuste para la funcion marginal de Y
plt.plot(Ys, gaussianaY)
plt.savefig('CurvaMejorAjusteY.jpg')
plt.grid(True)
plt.title('Curva de mejor ajuste para la funcion marginal de Y')
plt.ylabel('Probabilidad de ocurrencia')
plt.xlabel('Y')
plt.cla()

# Pregunta 2
# Si tenemos que las variables X y Y son independientes
# La expresion de la funcion de densidad conjunta que modela los datos es:
# fX,Y(X,Y)=fX(X)*fY(Y)
# En este caso, las curvas de mejor ajuste nos permiten obtener las ecuaciones tanto de fX y fY
# Al obtener los valores de mu y sigma en cada caso, se puede obtener la expresion


# Pregunta 3
# Para la correlacion 

#Ahora definimos los valores de x, y y p dentro de los datos xyp
xa = xyp["x"]
ya = xyp["y"]
pa = xyp["p"]
 
# Iniciamos el valor de correlacion en 0
Correl = 0

for i in range(len(xyp)):
    Correl = Correl + xa[i]*ya[i]*pa[i]
 
print('La correlacion es: ', Correl)

#Ahora para la covarianza
mu_x = parametroX[0]
mu_y = parametroY[0]
Productomus = mu_x * mu_y

Covar = Correl - Productomus

print('La covarianza es: ', Covar)

#Ahora para el coeficiente de covarianza
sigma_x = parametroX[1]
sigma_y = parametroY[1]

CoefCorrel = Covar/(4*sigma_x*sigma_y)

print('El coeficiente de correlacion es: ', CoefCorrel)

# Pregunta 4
# Ahora procedemos a graficar las funciones de densidad marginales
# Dichas funciones (2D), ya se habian graficado
# Estan guardadas como CurvafX y CurvafY

# Procedemos entonces a graficar la funcion de densidad conjunta (3D)
plt.cla()
ax = plt.axes(projection='3d')
ax.plot_trisurf(xa, ya, pa, cmap='viridis')
plt.savefig('Grafica3D')