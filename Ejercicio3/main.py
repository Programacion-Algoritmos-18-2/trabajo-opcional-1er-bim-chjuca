from paquete.Ejercicio3 import *					# Se importa El modulo Ejercicio 3

g1=Garante("Israel","Ortiz",380)					# Se crea un Objeto de Tipo Garante
p=Prestamo("Carlos Juca",384,10290,12, 6,g1)		# Se crea un objeto tipo prestamo
pv=PrestamosAutomovil("Gerson Santos",2344,20000,12,9,g1,"Automovil","BMW",Garante("David","Lopez",2344))	# Se crea un Objeto tipo PrestamoAutomovil 

print(p.presentarDatos())			# Se presenta los datos de Prestamo
print("\n")
print(pv.presentarDatos())			# Se presenta los datos de PrestamoAutomovil