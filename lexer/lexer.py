from Manejador_Archivos import Manejador_archivo
import re

class Lexer():
	def __init__(self):
		global a
		a = Manejador_archivo(input("Nombre del Archivo\n:"))

	def validar(self):	
		cont=1	
		for x in range(0,a.lineas_archivo()):
			cadena = a.leer_lineas()
			lista = cadena.split(" ")
			cont = cont+1
			for frase in lista:
				if re.match(r"amigui",frase):
					print("coincide ",frase)
				if re.match(r"estas", frase):
					print("coincide ",frase)
