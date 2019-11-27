#Ejercicio_07
#Detector de automedicacion
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia,total_de_medicamentos_por_semana="","","",0,0,0

# INPUT
paciente=input("Ingrese paciente:")
medicamento_1=input("Ingrese medicamento 1: ")
medicamento_2=input("Ingrese medicamento 2: ")
cant_de_medicamento1_por_dia=int(input("Ingrese cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=int(input("Ingrese cantidad de medicamento 2 por dia:"))

# PROCESSING
total_de_medicamentos_por_semana=cant_de_medicamento1_por_dia*7+cant_de_medicamento2_por_dia*7

# DETECTOR
# Sera automedicacion si el total de medicamento por semana > 20
automedicacion=(total_de_medicamentos_por_semana > 20 )

# OUTPUT
print("###########################")
print("#       MEDICAMENTOS       #")
print("###########################")
print("# Paciente: ",paciente,"  #")
print("# medicamento 1: ",medicamento_1,"        #")
print("# medicamento 2: ",medicamento_2,"        #")
print("# cantidad de medicamento 1 por dia : ",cant_de_medicamento1_por_dia,"        #")
print("# cantidad de medicamento 2 por dia : ",cant_de_medicamento2_por_dia,"        #")
print("###########################")
print("total de medicamento por semana:",total_de_medicamentos_por_semana,"      #")
print("# automedicacion : ",automedicacion,  "#")
print("###########################")
