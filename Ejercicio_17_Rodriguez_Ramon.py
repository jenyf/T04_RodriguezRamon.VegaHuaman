#Ejercicio_06
# Declaracion de variables de gusto por el deporte
nombre,deporte1,deporte2,deporte3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3,total_de_horas_por_semana="","","","",0,0,0,0

# INPUT
nombre=input("Ingrese nombre:")
deporte1=input("Ingrese deporte 1: ")
deporte2=input("Ingrese deporte 2: ")
deporte3=input("Ingrese deporte 3: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))
cant_de_hora_diarias_3=int(input("Ingrese cantidad de horas diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3

# OUTPUT
print("###########################")
print("#       DEPORTE        #")
print("###########################")
print("# Nombre: ",nombre,"  #")
print("# deporte 1: ",deporte1,"        #")
print("# deporte 2: ",deporte2,"        #")
print("# deporte 3: ",deporte3,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("# cantidad de horas diarias 3: ",cant_de_hora_diarias_3,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# gusto por el deporte : ",gusto_por_el_deporte,  "#")
print("###########################")
