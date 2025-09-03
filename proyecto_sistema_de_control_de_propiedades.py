import random

zonas_geograficas = ["norte", "sur", "este", "oeste", "centro"]
tipos_operaciones = ["alquiler", "venta", "permuta"]

cant_inmuebles_por_tipo_zona = [[0]*len(tipos_operaciones) for i in range (len(zonas_geograficas))]
precio_inmuebles_por_tipo_zona = [[0]* len(tipos_operaciones) for i in range (len(zonas_geograficas))]

print (cant_inmuebles_por_tipo_zona)