#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import io
import re

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
	# Contar frecuencia de datos, por atributo
	for col in data_set:
		file.write("\n")
		file.write(str(col) + " HEAD" + "\n")
		file.write(str(data_set[col].value_counts(dropna=False).head()) + "\n")
		file.write("\n")
		file.write(str(col) + " TAIL" + "\n")
		file.write(str(data_set[col].value_counts(dropna=False).tail()) + "\n")	
	file.close

def chequeo_patron(data_set, atributo, patron):
	cantidad = 0
	rows_failed = list()
	for row in data_set.iterrows():
		dato = row[1][atributo]
		if not(bool(patron.match(dato))):
			cantidad += 1
			print(dato)
			rows_failed.append(row)
	print(cantidad)
	return cantidad

def graficar_recorridos(data_set):

	# Hist de Edad	
	data_set["bici_edad"].plot('hist', color='#86bf91')
	plt.xlabel('Edad')
	plt.ylabel('Cantidad de viajes')
	plt.show()
	
	# Bar graph de Edad Mayores
	data_mayores = data_set['bici_edad'].value_counts(dropna=False).tail(n=20)
	data_mayores.plot('bar')
	plt.xlabel('Edad')
	plt.ylabel('Cantidad de viajes')
	plt.show()

	# Bar graph de Estacion_Nombre_Origen
	data_set["bici_nombre_estacion_origen"].value_counts(dropna=False).plot('bar')
	plt.xlabel('Estaciones')
	plt.ylabel('Cantidad de viajes')
	plt.show()

	# Bar graph de Estacion_Nombre_Destino
	data_set["bici_nombre_estacion_destino"].value_counts(dropna=False).plot('bar')
	plt.xlabel('Estaciones')
	plt.ylabel('Cantidad de viajes')
	plt.show()

def graficar_usuarios(data_set):
	
	# Bar graph de Edad 
	data_set['usuario_edad'].value_counts(dropna=False)[0:45].plot('bar', color='#8B0000')
	plt.xlabel('Edad')
	plt.ylabel('Cantidad de usuarios')
	plt.show()

	data_set['usuario_edad'].value_counts(dropna=False)[46:91].plot('bar', color='#8B0000')
	plt.xlabel('Edad')
	plt.ylabel('Cantidad de usuarios')
	plt.show()
	

if __name__ == "__main__":
	# Atributos recorridos: bici_id_usuario, bici_Fecha_hora_retiro, bici_tiempo_uso, bici_nombre_estacion_origen, bici_estacion_origen, bici_nombre_estacion_destino, bici_estacion_destino, bici_sexo, bici_edad
	filename_recorridos = 'data_set/recorridos-realizados-2018.csv'
	data_recorridos = pd.read_csv(filename_recorridos)
	# Atributos usuarios: usuario_id, usuario_sexo, usuario_edad, fecha_alta, hora_alta	
	filename_usuarios = 'data_set/usuarios-ecobici-2018.csv'
	data_usuarios = pd.read_csv(filename_usuarios)

	analisis_dataset(data_recorridos, "resumen_recorridos.txt")
	# Chequeo patron
	patron = re.compile('2018-*')
	assert chequeo_patron(data_recorridos, 'bici_Fecha_hora_retiro', patron) == 0
	# Chequeo patron fecha, formato esperado: [0-3][0-9]-[0-1][1-9]-2018
	patron = re.compile('[0-3][0-9]/[0-1][0-9]/2018')
	assert chequeo_patron(data_usuarios, 'fecha_alta', patron) == 0
	analisis_dataset(data_usuarios, "resumen_usuarios.txt")
	# Chequeo patron hora, formato esperado: [0-3][0-9]-[0-1][1-9]-2018
	patron = re.compile('5:[0-5][0-9]:[0-5][0-9]')
	assert chequeo_patron(data_usuarios, 'hora_alta', patron) == 0
	analisis_dataset(data_usuarios, "resumen_usuarios.txt")
	
	graficar_recorridos(data_recorridos)
	graficar_usuarios(data_usuarios)

