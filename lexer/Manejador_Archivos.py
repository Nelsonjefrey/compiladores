class Manejador_archivo():
	def __init__(self, archivo):
		self.archivo=archivo


	def leer(self):
		l = open(self.archivo , "r")
		contenido=l.read()
		print (contenido)
		l.close()	

	def escribir(self):
		f = open("texto.txt","w")
		f.write()
		nuevo_arcivo=f.read()
		print("Archivo Editado" , nuevo_arcivo)
		f.close()



