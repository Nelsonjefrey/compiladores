from Manejador_Archivo import archivo
from logica_lexer import Lexer
import pyttsx3
engine = pyttsx3.init()
engine.say('Good morning.')
engine.runAndWait()
 
file = archivo(input("ingrese el nombre del archivo :"))
l = Lexer()
for x in range(0,file.numero_lineas()):
	data = file.dame_linea()

	lista = l.prueba(data,x+1)
	for s in lista:
		print(s,"\n")
