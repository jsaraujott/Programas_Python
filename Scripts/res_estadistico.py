# Cargar librerias
import pandas as pd
import argparse

#Crear un parser y definir un parametro que corresponde al nombre de un archivo
parser = argparse.ArgumentParser()
parser.add_argument("file", type = str)

args = parser.parse_args()
file = args.file

#Carga el archivo de datos
datos = pd.read_csv(file, header=None)

#Transformar los datos en una serie
serie = datos.iloc[:,0]

# Generar estadística descriptiva
n = serie.count()
prom = serie.mean()
med = serie.median()
q1 = serie.quantile(0.25)
q3 = serie.quantile(0.75)
iqr = q3 - q1

#Guardar estadísticas coomo dataframe e imprimir
resumen = pd.DataFrame({
    "n":n,
    "Promedio":round(prom,1),
    "Mediana":round(med,1),
    "Cuartil_1":round(q1,1),
    "Cuartil_3":round(q3,1),
    "IQR":round(iqr,1)
}, index = [""])

print(resumen)