from personal_academico.Docente import *			# Importamos el modulo Docente
from sector_estudiantil.Estudiante import *			# Importamos el modulo Estudiante

n=input("Nombre del Docente Matematicas: ")			# Leemos de Teclado los Datos del Docente de Matematicas
a=input("Apellido del Docente Matematicas: ")
t=input("Titulo del Docente: ")
dm=Docente(n,a,t)									# Creamos un objeto de tipo docente y le enviamos los parametros antes leidos
print("_________________________________")

n1=input("Nombre del Docente Sociales: ")			# Leemos de Teclado los Datos del Docente de Sociales
a1=input("Apellido del Docente Sociales: ")
t1=input("Titulo del Docente: ")
ds=Docente(n1,a1,t1)								# Creamos un objeto de tipo docente y le enviamos los parametros antes leidos
print("_________________________________")

n=input("Nombre del Alumno: ")						# Leemos el nombre del estudiante
a=Alumno(n,dm,ds)									# Creamos un objeto de tipo estudiante y enviamos como parametro el nombre y los 2 ojetos tipo docente creados anteriormente

print("_________________________________")
print(a.presentarDatos())							#Presentamos Datos del objeto Estudiante