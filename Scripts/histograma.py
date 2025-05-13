# Carga de librerias
import numpy as np
import pandas as pd
import argparse

# Crear un objeto de Parsing
parser = argparse.ArgumentParser(description = "Este comando genera un histograma")
parser.add_argument("media", help = "La media de los datos")
parser.add_argument("desv", help = "La desviacion estandar de los datos")
parser.add_argument("--n", default = 100, help = "La cantidad de datos")

args = parser.parse_args()

# Definición de parametros
n = int(args.n)
media = float(args.media)
desv = float(args.desv)

#Crear valores aleatorios
datos = np.random.normal(size = n, loc = media, scale = desv)
datos = datos.round(0).astype(int)

# Eliminar valores extremos
datos_trim = []
for i in range(len(datos)):
    if datos[i] <= abs(media) + 2 * desv or datos[i] >= abs(media) - 2 * desv:
        datos_trim.append(datos[i])

# Transformar datos en un dataframe
datos_trim = pd.DataFrame(datos_trim)
datos_trim.columns = ["Datos"]
histograma = datos_trim.groupby('Datos').size() 

# Resumir informacion
for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )