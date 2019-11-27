#Ejercicio_04
## Declaracion de variables de visita compulsiva a una libreria
cliente,cantidad_de_libros,visita_por_semana,total_de_visita="",0,0,0

# INPUT
cliente=input("Ingrese nombre del cliente:")
cantidad_de_libros=int(input("Ingrese cantidad de libros:"))
visita_por_semana=int(input("Ingrese visita por semana:"))

# PROCESSING
total_de_visita=cantidad_de_libros*visita_por_semana

# OUTPUT
print("###########################")
print("#     LIBRERIA      #")
print("###########################")
print("# Cliente: ",cliente,"  #")
print("# cantidad de libros: ",cantidad_de_libros,"        #")
print("# visita por semana: ",visita_por_semana,"        #")
print("###########################")
print("total de visita:",total_de_visita,"      #")
print("# visita compulsiva a una libreria: ",visita_compulsiva_a_una_libreria,  "#")
print("###########################")
