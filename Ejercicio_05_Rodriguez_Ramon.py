#Ejercicio_05
#Detector de adiccion de las redes sociales
usuario,red_social_1,red_social_2,red_social_3,cant_de_hora_diarias_1,cant_de_hora_diarias_2,cant_de_hora_diarias_3,total_de_horas_por_dia="","","","",0,0,0,0

# INPUT
usuario=input("Ingrese nombre del usuario:")
red_social_1=input("Ingrese red social 1:")
red_social_2=input("Ingrese red social 2: ")
red_social_3=input("Ingrese red social 3:")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))
cant_de_hora_diarias_3=int(input("Ingrese cantidad de horas diarias 3:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2+cant_de_hora_diarias_3

# DETECTOR
# Sera adiccion de las redes sociales si el total de horas por dia > 15
adiccion_de_las_redes_sociales=(total_de_horas_por_dia > 15)

# OUTPUT
print("###########################")
print("#       RED SOCIAL        #")
print("###########################")
print("# Usuario: ",usuario,"  #")
print("# red social 1: ",red_social_1,"        #")
print("# red social 2: ",red_social_2,"        #")
print("# red social 3: ",red_social_3,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("# cantidad de horas diarias 3: ",cant_de_hora_diarias_3,"        #")
print("###########################")
print("total de horas por dia:",total_de_horas_por_dia,"      #")
print("# adiccion de las redes sociales : ",adiccion_de_las_redes_sociales,  "#")
print("###########################")
