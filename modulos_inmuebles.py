"""MODULO CON FUNCIONES"""
def operacion_maxima_por_zona (matriz):
    operaciones_maximas = []
    for i in range (len(matriz)):
        numero = max(matriz[i])
        operaciones_maximas.append(numero)
    return operaciones_maximas

def operacion_minima_por_zona (matriz):
    operaciones_minimas = []
    for i in range (len(matriz)):
        numero  = min(matriz[i])
        operaciones_minimas.append(numero)
    return operaciones_minimas

suma_zonas = lambda matriz: [sum(fila) for fila in matriz]

suma_operaciones = lambda matriz: [sum(matriz[fila][columna] for fila in range (len(matriz))) for columna in range (len(matriz[0]))]

def precio_promedio_por_zona (matriz_valor):
    precio_promed_zona = []
    for i in range (len(matriz_valor)):
        precio_promed_zona.append(sum(matriz_valor[i]) / len(matriz_valor[i]))
    return precio_promed_zona

def precio_promedio_por_operaciones (matriz_valor):
    precio_promed_operacion = []
    suma = 0
    num_filas = len(matriz_valor)
    num_columnas = len(matriz_valor[0]) 
    for i in range(num_columnas):
        for j in range (num_filas):
            suma += matriz_valor [j][i]
        promedio = suma / num_filas
        precio_promed_operacion.append(round(promedio,2))
        suma= 0
        promedio = 0
    return precio_promed_operacion
    
def ordenamiento_descendente_maximo (lista_maximos, zonas):
    cantidad_maxima_por_zona = list(zip(zonas, lista_maximos))
    cantidad_maxima_por_zona.sort (key = lambda x: x[1])
    cantidad_maxima_por_zona_desc = cantidad_maxima_por_zona [:: -1]
    return cantidad_maxima_por_zona_desc

def ordenamiento_descendente_minimo (lista_minimo, zonas):
    cantidad_minima_por_zona = list(zip(zonas, lista_minimo))
    cantidad_minima_por_zona.sort (key = lambda x: x[1])
    cantidad_minima_por_zona_desc = cantidad_minima_por_zona [:: -1]
    return cantidad_minima_por_zona_desc
    

        

       
