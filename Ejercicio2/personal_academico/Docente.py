class Docente(object):								# Creamos un objeto de tipo Docente
	def __init__(self,n,a,t):						# Constructor de la clase Docente
		self.nombre = n 							# Atributos de la clase
		self.apellido = a
		self.titulo = t

	def setNombre(self,n):							# Metodo Set 
		self.nombre = n

	def setApellido(self,a):
		self.apellido = a

	def setTitulo(self,t):
		self.titulo = t

	def getNombre(self):							# Metodos get
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getTitulo(self):
		return self.titulo
	
	def presentarDatos(self):						# Metodo que presenta datos de la clase docente
		cadena = "- Docente: %s %s\n- Titulo: %s"%(self.getNombre(),self.getApellido(),self.getTitulo())
		return cadena

		