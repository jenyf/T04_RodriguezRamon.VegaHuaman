#Ejercicio_08
# Declaracion de variables de bajo rendimiento academico
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0

# INPUT
alumno=input("Ingrese alumno:")
horas_dedicadas_al_estudio_por_dia=int(input("Ingrese horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7

# OUTPUT
print("###########################")
print("#  RENDIMIENTO ACADEMICO  #")
print("###########################")
print("# alumno: ",alumno,"  #")
print("# horas dedicadas al aestudio por dia: ",horas_dedicadas_al_estudio_por_dia,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# bajo rendimiento academico : ",bajo_rendimiento_academico,  "#")
print("###########################")
