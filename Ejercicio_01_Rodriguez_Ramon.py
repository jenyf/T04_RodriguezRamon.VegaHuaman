#Ejercicio_01
#Detector de calidad de algodon
cliente,producto_1,producto_2,cant_1,cant_2,costo_uni_1,costo_uni_2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
cant_1=int(input("Ingrese cantidad 1:"))
cant_2=int(input("Ingrese cantidad 2:"))
costo_uni_1=float(input("Ingrese costo uni 1:"))
costo_uni_2=float(input("Ingrese costo uni 2:"))

# PROCESSING
total=cant_1*costo_uni_1+cant_2*costo_uni_2

# DETECTOR
# Sera calidad de algodon cuando el total > 180
calidad_de_algodon=(total > 180)

# OUTPUT
print("###########################")
print("#     FACTURA     #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Cantidad 1: ",cant_1,"           #")
print("# Cantidad 2: ",cant_2," #")
print("# CostoUnitario 1: S/. ",costo_uni_1," #")
print("# CostoUnitario 2: S/. ",costo_uni_2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# Calidad de algodon: ",calidad_de_algodon,  "#")
print("###########################")
