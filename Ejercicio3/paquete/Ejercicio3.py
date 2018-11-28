class Garante(object):							# Se crea un Objeto tipo Garante
	def __init__(self, n,a,s):					# Constructor de la clase Garante
		self.nombre = n 						# Atributos de la clase
		self.apellido = a
		self.sueldo = s

	def setNombre(self,n):							# Metodo Set 
		self.nombre = n

	def setApellido(self,a):
		self.apellido = a

	def setSueldo(self,s):
		self.sueldo = s

	def getNombre(self):							# Metodos get
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getSueldo(self):
		return self.sueldo

	def presentarDatos(self):						# Metodo que presenta datos de la clase
		cadena="GARANTE:\n\t- Nombre: %s %s\n\t- Sueldo: %d"%(self.getNombre(),self.getApellido(),self.getSueldo())
		return cadena

class Prestamo(object):							# Clase Prestamo

	def __init__(self, nb,s,mp,i,t,g):			# Constructor de la clase Prestamo
		self.nombreBeneficiario = nb 			# Atributos de la clase
		self.sueldo = s
		self.montoPrestamo = mp
		self.interes = i
		self.tiempo = t
		self.garante1= g

	def setnombreBeneficiario(self,nb):			# Metodos set
		self.nombreBeneficiario = nb
		
	def setsueldo(self,s):
		self.sueldo = s

	def setmontoPrestamo(self,mp):
		self.montoPrestamo = mp

	def setInteres(self,i):
		self.interes = i

	def setTiempo(self,t):
		self.tiempo = t

	def setgarante1(self,g):
		self.garante1 = g

	def getnombreBeneficiario(self):		# Metodos Get
		return self.nombreBeneficiario

	def getSueldo(self):
		return	self.sueldo

	def getmontoPrestamos(self):
		return self.montoPrestamo

	def getInteres(self):
		return self.interes

	def getTiempo(self):
		return self.tiempo

	def getgarante1(self):
		return self.garante1.presentarDatos()

	def presentarDatos(self):				# Metodo para presentar Datos										
		cadena="\nPRESTAMO:\n\tNombre del Beneficiario: %s\n\tSueldo: %d\n\tMonto Prestamos: %d\n\tInteres: %d\n\tTiempo: %d\n\t%s"%(self.getnombreBeneficiario(),self.getSueldo(),self.getmontoPrestamos(),self.getInteres(),self.getTiempo(),self.getgarante1())
		return cadena

class PrestamosAutomovil(Prestamo):									# Clase PrestamoAutomovil que es hijo de Prestamo 

	def __init__(self,nb,s,mp,i,t,g,tv,mv,g2):						#Constructor de la clase
		super(PrestamosAutomovil, self).__init__(nb,s,mp,i,t,g)		# Herencia	
		self.tipoVehiculo = tv 										# Atributos de la clase
		self.marcaVehiculo = mv
		self.garante2 = g2

	def settipoVehiculo(self,tv):			# Metodo setg
		self.tipoVehiculo= tv

	def setmarcaVehiculo(self,mv):
		self.marcaVehiculo = mv

	def setgarante2(self,g2):
		self.garante2 = g2

	def gettipoVehiculo(self):				# Metodo Get
		return self.tipoVehiculo

	def getmarcaVehiculo(self):
		return self.marcaVehiculo

	def getgarante2(self):
		return self.garante2.presentarDatos()

	def presentarDatos(self):				# Metodos para Presentar Datos de la Clase
		cadena="\nPRESTAMO AUTOMOVIL :\n\tNombre del Beneficiario: %s\n\tSueldo: %d\n\tMonto Prestamos: %d\n\tInteres: %d\n\tTiempo: %d\n\tTipo de Vehiculo: %s\n\tMarca Vehiculo: %s\n\t%s\n"%(self.getnombreBeneficiario(),self.getSueldo(),self.getmontoPrestamos(),self.getInteres(),self.getTiempo(),self.gettipoVehiculo(),self.getmarcaVehiculo(),self.getgarante2())
		return cadena