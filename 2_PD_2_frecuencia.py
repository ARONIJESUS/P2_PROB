# -*- coding: utf-8 -*-
"""
PRÁCTICA DIRIGIDA N°2 MODELOS DE FRECUENCIA Y SEVERIDAD

*SEVERIDAD
Created on Tue Sep 27 17:41:20 2022

@Integrantes: 
    -Sebastian Cuentas 
    -Jesús Aroni
"""

from scipy.stats import nbinom, lomax, stats
import numpy as np
from scipy.special import comb
from random import random

# In[1]:

###### 1. Genere un vector aleatorio de 1000 filas con 
# distribución Binomial Negativa, estime los parámetros 
# de tal manera que el valor esperado sea 5

#longitud del vector
n_filas=1000

# creamos la función para estimar parametros de tal forma que la esperanza de 50

def Estimar_Parametros():    
    rand=random()
    r=50//rand
    beta=50/r    
    p=1/(1+beta)
    return [r,p]

k=Estimar_Parametros()
#parámetros binomial negativa segun la fórmula en python
r, p = k[0], k[1]

#Generando vector aleatorio de 1000 filas
x = nbinom.rvs(r,p,size=n_filas)
beta=(1-p)/p

#Esperanza con los valores y con los parametros estimados
print(x.mean(),k[0]*beta)

#Los parametros son
print(r,beta)

#Los 5 primeros valores simulados del vector de 1000 filas
print(x[0:6])

# In[2]:
###### 2. Estime empíricamente los valores de a y b y compare 
# los resultados con la fórmula cerrada (Opcional según tipo de grupo)


#calculando valores de a y b
a=beta/(1+beta)
b=(r-1)*beta/(1+beta)

###realizando ensayos comparativos


p3_nb=nbinom.pmf(3, r, p, loc=0)/nbinom.pmf(2, r, p, loc=0)
p3_ab=a+b/3

p4_nb=nbinom.pmf(4, r, p, loc=0)/nbinom.pmf(3, r, p, loc=0)
p4_ab=a+b/4


print(p3_nb,p3_ab)
print(p4_nb,p4_ab)

# In[3]:
###### 3. En base a una distribución de Severidad, 
# y para el deducible trabajado, ajuste el parámetro elegido de 
# frecuencia por la aplicación del deducible a la severidad,

#calculando percentiles para una distribución pareto 2p 
alfa, theta = 20, 40
vals = lomax.ppf([0.25, 0.5, 0.75], alfa,scale=theta)

# tomamos el percentil 75
per_75=vals[2]

#calculando la probabilidad del deducible P(X>d)
P_d=1-lomax.cdf(per_75,alfa,scale=theta)

#nuevos parametros para la distribución     
#cambia el parámetro relacionado con la probabilidad
r_x, p_x = 500, 1/(1+beta*P_d)

print(r_x, beta*P_d)

# In[3]:
###### 4. cual sería la probabilidad empírica de tener 3 siniestros si se 
#transforma en una distribución cero-truncada? Compare los 
#resultados con el cálculo teórico

# Ingresamos la cantidad de siniestros
n_siniestros=3

#creamos la función distribucion cero truncada

def BN_cero_truncada(x,r,p):
    if r==0 or r<-1  :
        return "error"

    else:
       beta=(1-p)/p
       y=comb(x+r-1,x)*((beta/(1+beta))**(x))/((1+beta)**r-1)    
    return y


#Probabilidad para 3 siniestros con la distribución
PT=BN_cero_truncada(n_siniestros,r_x,p_x)

#Probabilidad para 3 siniestros a partir de la Binomial negativa
PBN=nbinom.pmf(n_siniestros, r_x, p_x, loc=0)/(1-nbinom.pmf(0, r_x, p_x, loc=0))

print(PT, PBN)