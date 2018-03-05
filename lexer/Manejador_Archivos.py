class Manejador_archivo():
	def __init__(self, archivo):
		global f
		self.archivo = archivo
		f = open(self.archivo + ".gh","rt")	

	def leer_lineas(self):
		linea = f.readline()
		return linea
		
	def lineas_archivo(self):
		fi = open(self.archivo + ".gh","rt")
		lineas = len(fi.readlines())
		fi.close()	
		return lineas
	def cerrar_archivo():
		f.close()
