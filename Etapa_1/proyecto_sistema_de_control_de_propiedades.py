import random
import modulos_inmuebles

def cantidad_azar_inmuebles(matriz_cantidad):
    for i in range(len(matriz_cantidad)):
        for j in range(len(matriz_cantidad[0])):
            numero = random.randint(1, 99)
            while numero in matriz_cantidad[i]:
                numero = random.randint(1, 99)
            matriz_cantidad[i][j] = numero

def mostrar_zonas(zonas):
    print("Número de zona", end="")
    print("%22s" % "Zona")
    for i in range(len(zonas)):
        print("%8d" % (i+1), end="")
        print("\t", "%32s" % zonas[i])

def mostrar_operacion(operaciones):
    print("Número de operación", end="")
    print("%20s" % "Operación")
    for i in range(len(operaciones)):
        print("%8d" % (i+1), end="")
        print("\t", "%38s" % operaciones[i])

def asignacion_precio(precio_inmueble, zonas, operaciones):
    print()
    print("Se le pedirá al usuario que ingrese un precio promedio para cada zona y tipo de operación (el precio debe ser un número entero).")
    for i in range(len(zonas)):
        for j in range(len(operaciones)):
            valor = input(f"Ingrese un precio promedio para la operación {operaciones[j]} en la zona {zonas[i]}: ")
            while not (valor.isdigit() and int(valor) > 0):
                print ("Error: Se requiere ingresar un número entero mayor que 0.")
                valor = input(f"Ingrese un precio promedio para la operación {operaciones[j]} en la zona {zonas[i]}: ")
            precio_inmueble[i][j] = int(valor)

def inicializar_matrices(zonas, operaciones):
    cant_inmuebles = [[0] * len(operaciones) for _ in range(len(zonas))]
    precios = [[0] * len(operaciones) for _ in range(len(zonas))]
    return cant_inmuebles, precios

def mostrar_menu(zonas, operaciones):
    print("A continuación, se le mostrará el número de zona que representará a cada zona:")
    print()
    mostrar_zonas(zonas)
    print()
    print("Ahora, se le mostrará el número de operación que representará a cada tipo de operación:")
    print()
    mostrar_operacion(operaciones)

def consultas_interactivas(zonas, operaciones, cant_inmuebles, precios, sumas_zona, sumas_operacion, precio_prom_zona, precio_prom_operacion):
    zona = 0
    operacion = 0
    while zona != -1 and operacion != -1:
        zona = int(input("Ingrese la zona que desea conocer (-1 para salir): "))
        while zona > len(zonas) or (zona <= 0 and zona != -1):
            print("Error. Zona inválida.")
            mostrar_zonas(zonas)
            zona = int(input("Ingrese la zona que desea conocer (-1 para salir): "))
        if zona != -1:
            print(f"La zona {zonas[zona-1]} tiene un total de {sumas_zona[zona-1]} inmuebles.")
            operacion = int(input("Ingrese el tipo de operación que desea conocer (-1 para salir): "))
            if operacion != -1:
                while operacion > len(operaciones) or (operacion <= 0 and operacion != -1):
                    print("Error. Operación inválida.")
                    mostrar_operacion(operaciones)
                    operacion = int(input("Ingrese el tipo de operación que desea conocer (-1 para salir): "))
                if operacion != -1:
                    print(f"El tipo de operación {operaciones[operacion-1]} en la zona {zonas[zona-1]} tiene {cant_inmuebles[zona-1][operacion-1]} inmuebles, precio promedio {precios[zona-1][operacion-1]}")
                    print()
                    print(f"El precio promedio total de todas las operaciones de la zona {zonas[zona-1]} es ${precio_prom_zona[zona-1]}, con un total de {round(sumas_zona[zona-1], 2)} departamentos.")
                    print()
                    print(f"El precio promedio total de la operación {operaciones[operacion-1]} en todas las zonas es ${precio_prom_operacion[operacion-1]}, con un total de {round(sumas_operacion[operacion-1], 2)} departamentos.")

def informe_cantidades(zonas, operaciones, cant_inmuebles):
    print("\nInforme 1: Cantidad de departamentos por zona y operación\n")
    print("%-40s%s" % ("Operación", "Zonas Geográficas"))
    print("%17s" % "", end="")
    for zona in zonas:
        print("\t", zona, end="")
    print()
    for i in range (len(operaciones)):
        print("%-17s" % operaciones[i], end="")
        for j in range(len(zonas)):
            print("\t", cant_inmuebles[j][i], end="")
        print()

def informe_precios(zonas, operaciones, precios):
    print("\nInforme 2: Precio promedio por zona y operación\n")
    print("%-40s%s" % ("Operación", "Zonas Geográficas"))
    print("%17s" % "", end="")
    for zona in zonas:
        print("\t", zona, end="")
    print()
    for i in range (len(operaciones)):
        print(operaciones[i].ljust(15), end="")
        for j in range(len(zonas)):
            print("\t", str(precios[j][i]).center(10), end="")
        print()

def informe_totales(operaciones, zonas, sumas_operacion, sumas_zona):
    print("\nInforme 3: Totales por operación\n")
    for i in range (len(operaciones)):
        print (f"La cantidad total de inmuebles que su tipo de operación es {operaciones[i]} es de {sumas_operacion[i]}")
    
    print("\nInforme 4: Totales por zona geográfica\n")
    for i in range (len(zonas)):
        print (f"La cantidad total de inmuebles en la zona geográfica {zonas[i]} es de {sumas_zona[i]}")

def informe_max_min(zonas, operaciones, cant_inmuebles, orden_max, orden_min):
    print("\nInforme 5: Operación más frecuente por zona (descendente)\n")
    print("Operación \tZona \tCantidad")
    for zona, lista in orden_max:
        cantidad = lista
        zon = zonas.index(zona)
        posicion_max = cant_inmuebles[zon].index(cantidad)
        print("%-15s" % operaciones[posicion_max], end= "")
        print("\t", zona, "\t", lista)

    print("\nInforme 6: Operación menos frecuente por zona (descendente)\n")
    print("Operación \tZona \tCantidad")
    for zona, lista in orden_min:
        cantidad = lista
        zon = zonas.index(zona)
        posicion_min = cant_inmuebles[zon].index(cantidad)
        print("%-15s" % operaciones[posicion_min], end= "")
        print ("\t", zona, "\t", lista)

def main():
    zonas = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    operaciones = ["Alquiler", "Venta", "Permuta"]

    cant_inmuebles, precios = inicializar_matrices(zonas, operaciones)
    mostrar_menu(zonas, operaciones)

    cantidad_azar_inmuebles(cant_inmuebles)
    asignacion_precio(precios, zonas, operaciones)

    maximos = modulos_inmuebles.operacion_maxima_por_zona(cant_inmuebles)
    minimos = modulos_inmuebles.operacion_minima_por_zona(cant_inmuebles)

    sumas_zona = modulos_inmuebles.suma_zonas(cant_inmuebles)
    sumas_operacion = modulos_inmuebles.suma_operaciones(cant_inmuebles)

    precio_prom_zona = modulos_inmuebles.precio_promedio_por_zona(precios)
    precio_prom_operacion = modulos_inmuebles.precio_promedio_por_operaciones(precios)

    orden_max = modulos_inmuebles.ordenamiento_descendente_maximo(maximos, zonas)
    orden_min = modulos_inmuebles.ordenamiento_descendente_minimo(minimos, zonas)

    consultas_interactivas(zonas, operaciones, cant_inmuebles, precios, sumas_zona, sumas_operacion, precio_prom_zona, precio_prom_operacion)
    informe_cantidades(zonas, operaciones, cant_inmuebles)
    informe_precios(zonas, operaciones, precios)
    informe_totales(operaciones, zonas, sumas_operacion, sumas_zona)
    informe_max_min(zonas, operaciones, cant_inmuebles, orden_max, orden_min)

if __name__ == "__main__":
    main()

