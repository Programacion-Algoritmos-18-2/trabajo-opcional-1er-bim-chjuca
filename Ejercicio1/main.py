from paquete.ejercicio1 import *							# Importamos el modulo ejercicios1		

e = Equipo("Manchester United", "Inglaterra")				# Creamos un Objeto de tipo Equipo

f = Futbolista("Antonio","Valencia")						# Creamos un Objeto de tipo Futbolista
f.setEquipo(e)												# Agregamos valor a los atributos que faltan
f.setPosicion("lateral")
f.setDorsal(25)


e2 = Equipo("Nexaca","Mexico")								# Creamos un objeto de tipo Equipo
f2 = Futbolista("Alex","Aguinaga",e,"mediocentro")			# Creamos un Objeto de tipo Futbolista
f2.setDorsal(7)												# Agregamos valor a los atributos que faltan

e3 = Equipo("Lazio","Italia")								# Creamos un objeto de tipo Equipo
f3 = Futbolista("Felipe","Caicedo",e2)						# Creamos un Objeto de tipo Futbolista
f3.setPosicion("delantero")									# Agregamos valor a los atributos que faltan
f3.setDorsal(32)		


print(f.presentarDatos())									# Presentamos los objetos antes creados
print(f2.presentarDatos())
print(f3.presentarDatos())