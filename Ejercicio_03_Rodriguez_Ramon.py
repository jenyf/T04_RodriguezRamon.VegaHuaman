#Ejercicio_03
#Detector nota aprobatoria
nombre_del_alumno,nota_1,nota_2,nota_3,promedio="","","","",0

# INPUT
nombre_del_alumno=input("Ingrese el nombre del alumno:")
nota_1=int(input("Ingrese nota 1:"))
nota_2=int(input("Ingrese nota 2:"))
nota_3=int(input("Ingrese nota 3:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3

# DETECTOR
# Sera nota aprobatoria si el promedio > 11
nota_aprobatoria=(promedio > 11)

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# nombre del alumno : ",nombre_del_alumno,"  #")
print("# nota 1: ",nota_1,"        #")
print("# nota 2: ",nota_2,"        #")
print("# nota 3: ",nota_3,"        #")
print("###########################")
print("promedio:",promedio,"      #")
print("# nota aprobatoria: ",nota_aprobatoria,  "#")
print("###########################")

