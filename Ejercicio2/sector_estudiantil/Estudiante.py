from personal_academico.Docente import *				# Importamos el modulo Docente
	
class Alumno(object):									# Creamos una clase Alumno

	def __init__(self, n,dm,ds):						# Constructor de la clase Alumno
		self.nombre = n 								# Atributos de la clase Alumno
		self.docente_matematica=dm
		self.docente_sociales=ds

	def setNombre(self,n):								# Metodos Set
		self.nombre=n

	def setDocenteMatematicas(self, dm):
		self.docente_matematica= dm

	def setDocenteSociales(self,ds):
		self.docente_sociales = ds

	def getNombre(self):								# Metodos Get
		return self.nombre

	def getDocenteMatematicas(self):
		return self.docente_matematica.presentarDatos()

	def getDocenteSociales(self):
		return self.docente_sociales.presentarDatos()

	def presentarDatos(self):							# Metodo que presenta datos de la Clase Alumno
		cadena="\nEstudiante: %s\n\tDOCENTES:\n%s\n%s\n"%(self.getNombre(),self.getDocenteMatematicas(),self.getDocenteSociales())
		return cadena

		