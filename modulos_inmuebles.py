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

suma_zonas = lambda matriz: [sum(fila) for fila in matriz] #Creada lista que cotenga la suma por zonas

suma_operaciones = lambda matriz: [sum(matriz[fila][columna] for fila in range (len(matriz))) for columna in range (len(matriz[0]))]
#Esta función lambda inicia con el ciclo for para determinar la cantidad de columnas que hay por fila(suponemos que todas las filas tienen la misma contidad de columnas)
#Luego cuando se inicie la iteración de las columnas (valor columna = 0), se inicia el siguiente ciclo, el ciclo de las filas
#Cuando el ciclo de las filas pasa por todas las filas (1 a 4), la suma va a ir sumando todos los elementos de la misma columna en las diferentes filas
#Esto quiere decir que la suma será, en la primea vuelta de los elementos matriz[0][0], matriz [1][0], matriz[2][0], matriz[3][0], matriz[4][0]

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
    
def ordenamiento_desendente_maximo (lista_maximos):
    
"""CREAR UNA FUNCIÓN QUE PUEDA, CON LA FUNCIÓN DE MÁXIMO Y MÍNIMO,
JUNTO A LA LISTA DE ZONAS GEOGRÁFICAS, Y TENER LA DATA DEL TIPO DE OPERACIÓN,
IMPRIMIR DE MAYOR A MENOR, USANDO FUNCIÓN ZIP, Y SLICING LAS ZONAS CON MAYOR PRECIO
DE FORMA DECENDENTE"""

"""Modificar las funciones de máximo y minimo para hacer un zip de la lista, para combinar el tipo de
operacion y el maximo"""

        

       