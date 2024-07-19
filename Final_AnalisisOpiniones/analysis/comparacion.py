import json
import os

def guardar_resultados(resultados, file_path='resultados/resultados_actuales.json'):
    print(f"Guardando resultados en {file_path}...")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(resultados, f)
    print(f"Resultados guardados en {file_path}.")

def cargar_resultados(file_path='resultados/resultados_actuales.json'):
    print(f"Cargando resultados de {file_path}...")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            resultados = json.load(f)
        print(f"Resultados cargados de {file_path}.")
        return resultados
    else:
        print(f"No se encontraron resultados anteriores en {file_path}.")
        return None

def comparar_resultados(nuevos_resultados, file_path='resultados/resultados_actuales.json'):
    resultados_anteriores = cargar_resultados(file_path)
    
    if resultados_anteriores:
        comparacion = {
            'nuevos_resultados': nuevos_resultados,
            'resultados_anteriores': resultados_anteriores
        }
    else:
        comparacion = {
            'nuevos_resultados': nuevos_resultados,
            'resultados_anteriores': 'No hay resultados anteriores para comparar.'
        }
    
    guardar_resultados(nuevos_resultados, file_path)
    return comparacion
