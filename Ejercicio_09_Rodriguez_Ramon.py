#Ejercicio_09
#Detector de comprador compulsivo
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto1=input("Ingrese producto 1:")
producto2=input("Ingrese producto 2:")
cant_de_producto1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto2=int(input("Ingrese cantidad de producto 2:"))
costo_uni1=float(input("Ingrese costo unitario 1:"))
costo_uni2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto1*cost_uni1+cant_de_producto2*costo_uni2

# DETECTOR
# Sera comprador compulsivo si el total > 260
comprador_compulsivo=(total < 260)

# OUTPUT
print("###########################")
print("#   PRODUCTO DE BELLEZA   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto1,"        #")
print("# Producto 2: ",producto2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto2," #")
print("# Costo Unitario 1: S/. ",costo_uni1," #")
print("# Costo Unitario 2: S/. ",costo_uni2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador compulsivo: ",comprador_compulsivo,  "#")
print("###########################")
