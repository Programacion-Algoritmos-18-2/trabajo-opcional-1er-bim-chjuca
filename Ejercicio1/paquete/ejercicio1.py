class Futbolista(object):								# Creamos una Clase Futbolista
		
	def __init__(self,n="",a="",e=None,p="",d=0):		# Constructor de la Clase
		self.nombre=n 									# Damos valor a los atributos de la clase
		self.apellido=a
		self.equipo=e
		self.posicion=p
		self.dorsal=d
	
	def setNombre(self,n):								# Metodos Set
		self.nombre=n

	def setApellido(self,a):
		self.apellido=a

	def setEquipo(self,e):
		self.equipo=e

	def setPosicion(self,p):
		self.posicion=p

	def setDorsal(self,d):
		self.dorsal=d

	def getNombre(self):								# Metodos Get
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getEquipo(self):
		return self.equipo.presentarDatos()

	def getPosicion(self):
		return self.posicion

	def getDorsal(self):
		return self.dorsal

	def presentarDatos(self):							# Metodos para presentar de la clase Futbolista
		cadena="\n%s %s\n%s\nsu posicion es %s y\nsu dorsal es el numero %d\n"%(self.getNombre(),self.getApellido(),self.getEquipo(),self.getPosicion().upper(),self.getDorsal())
		return cadena

class Equipo(object):									#  Clase la clase Equipo

	def __init__(self, n,p):							# Constructor de la clase Equipo
		self.setNombre(n)								# Atributos de la clase equipo
		self.setPais(p)

	def setNombre(self,n):								# Metodos Set
		self.nombre=n

	def setPais(self,p):
		self.pais=p	

	def getNombre(self):								# Metodos Get
		return self.nombre
	
	def getPais(self):
		return self.pais

	def presentarDatos(self):							# Se presentan los Datos de clase Equipo 
		cadena="pertenece al equipo %s del pais %s,"%(self.getNombre(),self.getPais())
		return cadena

		
