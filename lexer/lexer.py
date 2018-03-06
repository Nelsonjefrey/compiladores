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
			for frase in lista:
				print(frase,cont)
				cont=+1
				if re.match(self.diccionary(cont),frase):
					print ("valido ", frase)
				

					
	def S_():
		return r"S_"

	def SN_():
		return "ELSE"
	def P_():
		return "FOR"
	def E_():
		return "WHILE"
	def L_():
		return "LEER"
	def _I():
		return "INICIO"
	def _F():
		return "FIN"
	def VOID():
		return "NULL"

	def diccionary(self,argumento):
		return{
			1:"P_",
			2:"E_",
			3:"L_",
			4:"S_",
			5:"S_",
			6:"*P",
			7:"*F",
			8:"VOID"	
		}.get(argumento, "no valido")

