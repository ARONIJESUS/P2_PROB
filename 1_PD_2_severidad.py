# -*- coding: utf-8 -*-
"""
PRÁCTICA DIRIGIDA N°2 MODELOS DE FRECUENCIA Y SEVERIDAD

*SEVERIDAD
Created on Tue Sep 27 17:41:20 2022

@Integrantes: 
    -Sebastian Cuentas 
    -Jesús Aroni
"""

# In[1]:


import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from random import random


# In[2]:

### 1. Se genera el vector de 5,000 filas cada uno con distribución Pareto y Gamma
###(para el caso de grupo de 2 integrantes, elija una de ellas y solo genere un vector de 5000 filas).
# Se genera el vector con distribución Pareto utilizando el método de la inversa
lst = []
 
for i in range(5000):
  lst.append(random())

lst = np.asarray(lst)
beta=150            
alpha=25.5
e=math.e
x=e**((alpha*np.log(beta)-np.log(1-lst))/alpha)      #Este va a ser el vector de 5000 observaciones
print(x)


# In[3]:


#Gráfico de como sale el vector de 5000 filas
plt.hist(x=x, bins = 10, color='#F2AB6D', rwidth=0.85)
plt.show()


# ### 2

# In[4]:


###Estime la media, varianza, el percentil 25 y 75
media = np.mean(x)
varianza = np.var(x)
percentil_25 = np.percentile(x, 25)
percentil_75 = np.percentile(x, 75)
print(media, varianza, percentil_25, percentil_75)


# ### 3

# In[5]:


###Genere los siguientes vectores:

#Pago por pérdida para un deducible igual al percentil 25
pago_perdida= list(map(lambda x: x-percentil_25 if x>percentil_25 else 0, x))
pago_perdida = np.asarray(pago_perdida)
#Pago por pago para un deducible igual al percentil 25
pago_pago = x[x>percentil_25]
pago_pago= list(map(lambda x: x-percentil_25, pago_pago))
pago_pago = np.asarray(pago_pago)
#Pago por pérdida para un límite igual al percentil 75
pago_perdida_limite = np.minimum(x, percentil_75)
#Pago por pérdida para un deducible igual al percentil 25 y un límite igual al percentil 75
pago_perdida_deducible_limite = pago_perdida_limite
pago_perdida_deducible_limite= list(map(lambda x: x-percentil_25 if x>percentil_25 else 0, pago_perdida_deducible_limite))
pago_perdida_deducible_limite = np.asarray(pago_perdida_deducible_limite)
#Pago por pago para un deducible igual al percentil 25 y un límite igual al percentil 75
pago_pago_deducible_limite = pago_perdida_limite
pago_pago_deducible_limite = pago_pago_deducible_limite[pago_pago_deducible_limite>percentil_25]
pago_pago_deducible_limite= list(map(lambda x: x-percentil_25, pago_pago_deducible_limite))
pago_pago_deducible_limite = np.asarray(pago_pago_deducible_limite)


# ### 4

# In[6]:


###Estime la media y varianza de las variables con coberturas modificadas.
lista = [pago_perdida, pago_pago, pago_perdida_limite, pago_perdida_deducible_limite, pago_pago_deducible_limite]

for i in lista: 
    print(np.mean(i), np.var(i))


# ### 5

# In[7]:


###Ordene las variables modificadas por valor de la media. ¿Cuál es más costosa?
a = ["Pago por pérdida de límite", 'Pago por pago solo deducible', 'Pago por pérdida solo deducible', "Pago por pago de deducible y límite", "Pago por pérdida de deducible y límite"]
b = [np.mean(pago_perdida_limite), np.mean(pago_pago), np.mean(pago_perdida), np.mean(pago_pago_deducible_limite), np.mean(pago_perdida_deducible_limite)]
d = {'METODO': a, 'MEDIA': b}
df = pd.DataFrame(data=d)
df


# ### 6

# In[8]:


###Ordene las variables modificadas por valor de la varianza. ¿Cuál es más costosa? (considerando que a 
###mayor varianza mayor costo).
df["VARIANZA"] = [np.var(pago_perdida_limite), np.var(pago_pago), np.var(pago_perdida), np.var(pago_pago_deducible_limite), np.var(pago_perdida_deducible_limite)]
df.sort_values(by=['VARIANZA'], ascending = False)

#La más costosa por la varianza es el método pago por pago de solo el deducible


# ### 7

# La variable más costosa es en la que se aplica un límite igual al percentil 75 porque a diferencia de las otras variables
# a esta no se le disminuye el costo de la severidad debido a un deducible, sino que se le impone un tope máximo y como el percentil 75 está muy cerca del monto máximo la disminución del costo no es mucha comparado con las variables en donde se aplica el deducible
