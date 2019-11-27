#Ejercicio_08
#Detector de bajo rendimiento academico
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0

# INPUT
alumno=input("Ingrese alumno:")
horas_dedicadas_al_estudio_por_dia=int(input("Ingrese horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7

# DETECTOR
# Sera bajo rendimiento academico si el total de horas por semana < 35
bajo_rendimiento_academico=(total_de_horas_por_semana < 35)

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
