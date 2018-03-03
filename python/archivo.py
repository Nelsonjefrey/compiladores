
def enviar():
		t = open("text.txt","r")
		cadena=t.read()
		print(cadena)
		t.close()
		input()
def leer():
	t = open("nota.txt","w")
	t.write("linea1\nlinea2\nlinea3")
	t.close()
	t.open("nota.txt","r")
	cadena = t.read()
	print(cadena)
	t.close()
	
input()


def copiaArchivo(archViejo, archNuevo):
	
		f1 = open(archViejo , "r")
		f2 = open(archNuevo , "w")

		while 1:
			texto = f1.read(50)
			if texto == "":
				break
		
		f2.write(texto)
		f1.close()
		f2.close()
		input()
		
def funcion1():
	print("nelson")

print("hola")
enviar()
leer()
input()

	


	





				

						

	
		