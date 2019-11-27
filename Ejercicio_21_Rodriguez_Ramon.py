#Ejercicio_10
# Declaracion de variables de comprador pasivo
cliente,producto_1,producto_2,cant_de_producto_1,cant_de_producto_2,cost_uni_1,cost_uni_2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
producto_2=input("Ingrese producto 2:")
cant_de_producto_1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto_2=int(input("Ingrese cantidad de producto 2:"))
costo_uni_1=float(input("Ingrese costo unitario 1:"))
costo_uni_2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto_1*cost_uni_1+cant_de_producto2*costo_uni_2

# OUTPUT
print("###########################")
print("#   PRODUCTO DE GOLOSINAS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Producto 2: ",producto_2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto_2," #")
print("# Costo Unitario 1: S/. ",costo_uni_1," #")
print("# Costo Unitario 2: S/. ",costo_uni_2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador pasivo: ",comprador_pasivo,  "#")
print("###########################")
