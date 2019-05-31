#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import io

def analisis_dataset(data_set, file):
	file = open(file, "w+")
	# Forma
	file.write(str(data_set.shape) + "\n")
	# Atributos
	file.write(str(data_set.columns) + "\n")
	# Info sobre los valores
	buffer = io.StringIO()
	data_set.info(buf=buffer, null_counts=False)
	s = buffer.getvalue()
	file.write(s + "\n")
	# Resumen estadistico
	file.write(str(data_set.describe()) + "\n")
	# Contar frecuencia de datos, por atributo?
	for col in data_set:
		file.write("\n")
		file.write(str(col) + " HEAD" + "\n")
		file.write(str(data_set[col].value_counts(dropna=False).head()) + "\n")
		file.write("\n")
		file.write(str(col) + " TAIL" + "\n")
		file.write(str(data_set[col].value_counts(dropna=False).tail()) + "\n")	
	file.close

# def graficar(data_set):
	# # Histograma por atributo?
	# data_set.COLUMNA.plot('hist')
	# plt.show()

	# # Boxplot
	# data_set.boxplot(column='COLUMNA1', by="COLUMNA2")
	# plt.show()

	# # Scatter: relacion entre dos valores numericos
	# data_set.boxplot(column='COLUMNA1', by="COLUMNA2")
	# plt.show()	

if __name__ == "__main__":
	
	filename_recorridos = 'data_set/recorridos-realizados-2018.csv'
	filename_usuarios = 'data_set/usuarios-ecobici-2018.csv'
	data_recorridos = pd.read_csv(filename_recorridos)
	data_usuarios = pd.read_csv(filename_usuarios)

	# print(data_recorridos['bici_edad'].value_counts(dropna=False).head())
	analisis_dataset(data_recorridos, "resumen_recorridos.txt")
	analisis_dataset(data_usuarios, "resumen_usuarios.txt")

	# # Converting data types
	# data_recorridos['COLUMNA'] = data_recorridos['COLUMNA'].astype(str)
	# data_recorridos['COLUMNA'] = data_recorridos['COLUMNA'].astype('category')
	# data_recorridos['COLUMNA'] = data_recorridos['COLUMNA'].to_numeric()

	# # Map funcion, VER
	# df.apply(cleaning_function, axis=1)

	# # Salvar el dataset
	# df.to_csv['FILENAME']
