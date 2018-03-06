from Manejador_Archivo import archivo
from logica_lexer import Lexer
file = archivo(input("ingrese el nombre del archivo :"))
l = Lexer()
for x in range(0,file.numero_lineas()):
	data = file.dame_linea()
	lista = l.prueba(data)
	for s in lista:
		print(s,"\n")
