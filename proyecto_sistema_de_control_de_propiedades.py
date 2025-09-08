import random
import modulos_inmuebles

def cantidad_azar_inmuebles (matriz_cantidad):
    for i in range (len(matriz_cantidad)):
        for j in range (len(matriz_cantidad[0])):
            numero = random.randint (1, 99)
            while numero in matriz_cantidad[i]:
                numero = random.randint (1,99)
            matriz_cantidad[i][j] = numero
            
def mostrar_zonas (zonas):
    print ("Número de zona", end="")
    print ("%22s" % "Zona")
    for i in range (len(zonas)):
        print ("%8d"% (i+1), end= "")
        print ("\t", "%32s"% zonas[i])

def mostrar_operacion (operaciones):
    print ("Número de operación", end="")
    print ("%20s" % "Operación")
    for i in range (len(operaciones)):
        print ("%8d" % (i+1), end= "")
        print ("\t", "%38s" % operaciones[i])

def asignacion_precio (precio_inmueble, zonas, operacion):
    valor = 0
    print ()
    print ("Se le pedirá al usuario que ingrese un precio promedio para cada zona y tipo de operación (no ingrese un mismo precio para dos operaciones diferentes que se encuentran en la mismas zona).")
    for i in range (len(zonas)):
        for j in range (len(operacion)):
            valor = float(input(f"Ingrese un precio promedio para la operación {operacion[j]} en la zona {zonas[i]}: "))
            while valor <= 0:
                print ("Usted a ingresado inválido. Vuelva a ingresar otro")
                valor = float(input(f"Ingrese un precio promedio para la operación {operacion[j]} en la zona {zonas[i]}: "))
            precio_inmueble[i][j] = valor

def main():
    zonas_geograficas = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    tipos_operaciones = ["Alquiler", "Venta", "Permuta"]
    
    cant_inmuebles_por_tipo_zona = [[0]*len(tipos_operaciones) for i in range (len(zonas_geograficas))]
    precio_inmueble_por_tipo_zona = [[0]*len(tipos_operaciones) for i in range (len(zonas_geograficas))]
    
    print("A continuación, se le mostrará al usuario, el número de zona que representará a cada zona: ")
    print()
    mostrar_zonas (zonas_geograficas)
        
    print()
    print("Ahora, se le mostrará al usuario, el número de operación, que representará a cada tipo de operación: ")
    print ()
    mostrar_operacion (tipos_operaciones)
        
    cantidad_azar_inmuebles (cant_inmuebles_por_tipo_zona)
    asignacion_precio (precio_inmueble_por_tipo_zona, zonas_geograficas, tipos_operaciones)
    
    departamento_maximo_por_zona = modulos_inmuebles.operacion_maxima_por_zona (cant_inmuebles_por_tipo_zona)
    departamento_minimo_por_zona = modulos_inmuebles.operacion_minima_por_zona (cant_inmuebles_por_tipo_zona)
    
    sumas_por_zona = modulos_inmuebles.suma_zonas (cant_inmuebles_por_tipo_zona)
    sumas_por_operacion = modulos_inmuebles.suma_operaciones (cant_inmuebles_por_tipo_zona)
    
    precio_prom_zona = modulos_inmuebles.precio_promedio_por_zona(precio_inmueble_por_tipo_zona)
    precio_prom_operacion = modulos_inmuebles.precio_promedio_por_operaciones (precio_inmueble_por_tipo_zona)
    
    orden_desc_maximos = modulos_inmuebles.ordenamiento_descendente_maximo (departamento_maximo_por_zona, zonas_geograficas)
    orden_desc_minimos = modulos_inmuebles.ordenamiento_descendente_minimo (departamento_minimo_por_zona, zonas_geograficas)
    
    zona = 0
    operacion = 0
    while zona != -1 and operacion != -1:
        zona = int(input("Ingrese la zona que desea conocer la cantidad de inmuebles que se encuentra allí (el programa finaliza cuando se ingrese -1): "))
        while zona > 5 or (zona <= 0 and zona != -1):
            print ("Error al ingresar la zona. Se le mostrará nuevamente el número que representa cada zona.")
            mostrar_zonas (zonas_geograficas)
            print()
            zona = int(input("Ingrese la zona que desea conocer la cantidad de inmuebles que se encuentra allí (el programa finaliza cuando se ingrese -1): "))
        if zona != -1:
            print (f"La zona {zonas_geograficas[zona-1]}, tiene un total de {sumas_por_zona[zona-1]} inmuebles.")
            
            operacion = int(input("Ingrese el tipo de operación que desea conocer dentro de la zona especificada (el programa finaliza cuando se ingrese -1): "))
            if operacion != -1:
                while operacion > 3 or (operacion <= 0 and zona != -1):
                    print ("Error al ingresar la operación. Se le mostrará nuevamente el númeor que representa cada operación.")
                    mostrar_operacion (tipos_operaciones)
                    operacion = int(input("Ingrese el tipo de operación que desea conocer dentro de la zona especificada (el programa finaliza cuando se ingrese -1): "))
                if operacion != -1:
                    print (f"El tipo de operación {tipos_operaciones[operacion-1]}, en la zona {zonas_geograficas[zona-1]} hay un total de {cant_inmuebles_por_tipo_zona[zona-1][operacion-1]}, y su precio promedio es de {precio_inmueble_por_tipo_zona [zona-1][operacion-1]}")
                    
                    print ()
                    print (f"El precio promedio total de todas las operaciones de la zona {zonas_geograficas[zona-1]}, es de ${precio_prom_zona[zona-1]}, con un total de {round(sumas_por_zona[zona-1],2)} departamentos.")
                    print ()
                    print (f"El precio promedio total de la operación {tipos_operaciones[operacion-1]} en todas las zonas geográficas, es de ${precio_prom_operacion[operacion-1]}, con un total de {round(sumas_por_operacion[operacion-1],2)} departamentos")
                    print ()
        print ()
    
    print ("A continuación se mostrará el siguiente informe:")
    print ("\nInforme 1: Cuadro donde se reflecta la cantidad de departamentos según su zona geográfica y tipo de operación: ")
    print ()
    print ("%-40s%s" % ("Operación", "Zonas Geográficas"))
    print ("%17s" % "", end="") 
    for zona in zonas_geograficas:
        print ("\t", zona, end="")
    print()
    for i in range (len(tipos_operaciones)):
        print ("%-17s" % tipos_operaciones[i], end="")
        for j in range (len(zonas_geograficas)):
            print ("\t", cant_inmuebles_por_tipo_zona[j][i], end="")
        print ()
    
    print ("\nInforme 2: Cuadro dende se reflecta el precio promedio de cada departamento según su zona geográfica y tipo de operación: ")
    print ()
    print ("%-40s%s" % ("Operación", "Zonas Geográficas"))
    print ("%17s" % "", end="")
    for zona in zonas_geograficas:
        print ("\t",zona, end= "")
    print ()
    for i in range (len(tipos_operaciones)):
        print (tipos_operaciones[i].ljust(15), end= "")
        for j in range (len(zonas_geograficas)):
            print ("\t", str( precio_inmueble_por_tipo_zona[j][i]).center(10), end = "")
        print ()
            
    print ("\nInforme 3: Precios promedios totales de cada operación, tomando en cuenta todas las zonas geográficas: ")
    print ()
    for i in range (len(tipos_operaciones)) :
        print (f"La cantidad total de inmuebles que su tipo de operación es {tipos_operaciones[i]} es de {sumas_por_operacion[i]}")
    
    print ("\nInforme 4: Precios promedios totales de cada zona geográfica, tomando en cuenta todos los tipos de operaciones que se realizan allí: ")
    for i in range (len(zonas_geograficas)):
        print (f"La cantidad total de inmuebles en la zona geográfica {zonas_geograficas[i]} es de {sumas_por_zona[i]}")
           
    print ("\nInforme 5: Cuadro mostrando el tipo de operación que más se realiza en cada zona, ordenado de manera descendente: ")
    print ()
    print ("Operación \tZona   \tCantidad")
    for zonas, lista in orden_desc_maximos:
        cantidad = lista
        zon = zonas_geograficas.index(zonas)
        posicion_max = cant_inmuebles_por_tipo_zona[zon].index(cantidad)
        print ("%-15s" % tipos_operaciones[posicion_max], end = "")
        print ("\t", zonas, "\t", lista)

    print ("\nInforme 6: Cuadro mostrando el tipo de operación que menos se realiza en cada zona, ordenado de manera descendente: ")
    print ()
    print ("Operación   \tZona   \tCantidad")
    for zonas, lista in orden_desc_minimos:
        cantidad = lista
        zon = zonas_geograficas.index(zonas)
        posicion_min = cant_inmuebles_por_tipo_zona[zon].index(cantidad)
        print ("%-15s" % tipos_operaciones[posicion_min], end= "")
        print ("\t", zonas, "\t", lista)

        
main()  