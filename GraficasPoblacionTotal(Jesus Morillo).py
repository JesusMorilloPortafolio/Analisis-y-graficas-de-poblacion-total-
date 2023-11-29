#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd #libreria para grafcias y datos
import cufflinks as cf #libreria para grafcias, datos, estilo
from IPython.display import display,HTML

cf.set_config_file(sharing='public',theme='ggplot',offline=True)


# In[32]:


pd.read_csv('population_total.csv') #Aqui se llama al archivo excel 


# In[39]:


df_population = pd.read_csv('population_total.csv')
df_population = df_population.dropna() #aqui se limpian o borran los valores nulos que caunsan problemas 

df_population = df_population.pivot(index='year', columns='country', #aqui se le da forma al data frame 
                                    values='population')
df_population = df_population[['United States', 'India', 'China', #para armar la estructura de datos
                             'Indonesia', 'Russia', 'Mexico', 'Chile', 'Argentina', 'Brazil', 'Peru', 'Ecuador', 'Colombia', 'Venezuela']] 
df_population


# # 1 Grafico de lineas

# In[40]:


#En este grafico veremos la disparidad demográfica entre naciones de gran extensión territorial y países latinoamericanos.
df_population.iplot(kind='line', xTitle='Años', yTitle='Popularidad', #Titulos para el eje X y eje Y
                   title='Disparidad demográfica entre naciones de gran extensión territorial y países latinoamericanos.') 


# # Grafico de barras

# In[43]:


#En este lugar, únicamente analizaremos la totalidad de habitantes correspondiente al año 2020.
df_population_2020 = df_population[df_population.index.isin([2020])]#Aqui filtramos el año 2020
df_population_2020 = df_population_2020.T#Aqui se cambian filas y columnas 

df_population_2020.iplot(kind='bar', xTitle='Paises', yTitle='Popularidad', #Titulos para el eje X y eje Y
                           title='Totalidad de habitantes correspondiente al año 2020.', color='red')


# # Graficos de barras multiples
# 

# In[49]:


#En este lugar, únicamente analizaremos el inicio de las ultimas decadas.
df_population_sample = df_population[df_population.index.isin([1980, 1990, 2000, 2010, 2020])]#Aqui filtramos el año 2020

df_population_sample.iplot(kind='bar', xTitle='Paises', yTitle='Popularidad', #Titulos para el eje X y eje Y
                           title='Totalidad de habitantes en las ultimas decadas.')


# # Diagramas de caja
 

# In[ ]:




