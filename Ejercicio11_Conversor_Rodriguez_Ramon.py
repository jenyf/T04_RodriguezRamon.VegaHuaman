                #CONVERSORES

# Ejercicio_1
# Declaracion variables
empleado,nro_dias,costo_por_dia,horas_extra,monto_a_pagar="",0,0.0,0,0.0

# INPUT
empleado="WALTER ORTIZ"
nro_dias=7
costo_por_dia=80
horas_extra=2

# PROCESSING
monto=(nro_dias*costo_por_dia)+(horas_extra*8)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Empleado: ",empleado,"   #")
print("# Nro Dias   : ",nro_dias,"          #")
print("# Costo por Dia : ",costo_por_dia,"         #")
print("# Horas Extra: ",horas_extra,"           #")
print("###########################")
print("# Monto a Pagar: ",monto_a_pagar,"     #")
print("###########################")

# Ejercicio_2
# Declaracion variables
cliente,producto_1,producto_2,producto_3,costo_uni_1,costo_uni_2,costo_uni_3,cant_de_producto_1,cant_de_producto_2,cant_de_producto_3,total="","","","",0.0,0.0,0.0,0,0,0,0.0

# INPUT
cliente="Maribel Yaipen"
producto_1="Cafe"
producto_2="Cocoa"
producto_3="Leche"
costo_uni_1=1.20
costo_uni_2=1.00
costo_uni_3=4.50
cant_de_producto_1=3
cant_de_producto_2=2
cant_de_producto_3= 1

# PROCESSING
total=(costo_uni_1*cant_de_producto1)+(costo_uni_2*cant_de_producto_2)+(costo_uni_3*cant_de_producto_3)

# OUTPUT
print("###########################")
print("#     BOLETA DE VENTA      #")
print("###########################")
print("# Cliente: ",cliente,"   #")
print("# Producto 1   : ",producto_1,"          #")
print("# Producto 2   : ",producto_2,"          #")
print("# Producto 3   : ",producto_3,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Costo Unitario 3: ",costo_uni_3,"         #")
print("# Cantidad de Producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de Producto 2: ",cant_de_producto_2,"           #")
print("# Cantidad de Producto 3: ",cant_de_producto_3,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")


# Ejercicio_3
# Declaracion variables
alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

# INPUT
alumno="Kinyu Rodriguez"
nota_1=13
nota_2=15
nota_3=18

# PROCESSING
total=(nota_1+nota_2+nota_3)/3

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# Alumno: ",alumno,"   #")
print("# Nota 1   : ",nota_1,"          #")
print("# Nota 2   : ",nota_2,"          #")
print("# Nota 3   : ",nota_3,"          #")
print("###########################")
print("# Promedio: ",promedio,"     #")
print("###########################")

# Ejercicio_4
# Declaracion variables
cliente,producto_1,producto_2,producto_3,costo_uni_1,costo_uni_2,costo_uni_3,cant_de_producto_1,cant_de_producto_2,cant_de_producto_3="","","","",0.0,0.0,0.0,0,0,0,0.0

# INPUT
cliente="Gabriel Velasquez"
producto_1="wafer"
producto_2="Choco Soda"
producto_3="Oreo"
costo_uni_1=0.60
costo_uni_2=0.70
costo_uni_3=0.80
cant_de_producto_1=25
cant_de_producto_2=38
cant_de_producto_3=50

# PROCESSING
total=(costo_uni_1*cant_de_producto1)+(costo_uni_2*cant_de_producto_2)+(costo_uni_3*cant_de_producto_3)

# OUTPUT
print("###########################")
print("#     FACTURA     #")
print("###########################")
print("# Cliente: ",cliente,"   #")
print("# Producto 1   : ",producto_1,"          #")
print("# Producto 2   : ",producto_2,"          #")
print("# Producto 3   : ",producto_3,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Costo Unitario 3: ",costo_uni_3,"         #")
print("# Cantidad de Producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de Producto 2: ",cant_de_producto_2,"           #")
print("# Cantidad de Producto 3: ",cant_de_producto_3,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")

# Ejercicio_5
# Declaracion variables
paciente,medicamento_1,medicamento_2,medicamento_3,cant_de_medicamento_1_por_dia,cant_de_medicamento_2_por_dia,cant_de_medicamento_3_por_dia,total_de_medicamentos_por_semana="","","","",0,0,0,0

# INPUT
paciente="Barbara Perez"
medicamento_1="ibuprofeno"
medicamento_2="diclofenaco"
medicamento_3="paracetamol"
cant_de_medicamento_1_por_dia=3
cant_de_medicamento_2_por_dia=2
cant_de_medicamento_3_por_dia=1

# PROCESSING
total=cant_de_medicamento_1_por_dia+cant_de_medicamento_2_por_dia+cant_de_medicamento_3_por_dia

# OUTPUT
print("###########################")
print("#    RECETA MEDICA   #")
print("###########################")
print("# Paciente: ",paciente,"   #")
print("# Medicamento 1   : ",medicamento_1,"          #")
print("# Medicamento 2   : ",medicamento_2,"          #")
print("# Medicamento 3   : ",medicamento_3,"          #")
print("# Cantidad de Medicamento 1 por Dia: ",cant_de_medicamento_1_por_dia,"           #")
print("# Cantidad de Medicamento 2: ",cant_de_medicamento_2_por_dia,"           #")
print("# Cantidad de Medicamento 3: ",cant_de_medicamento_3_por_dia,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")
