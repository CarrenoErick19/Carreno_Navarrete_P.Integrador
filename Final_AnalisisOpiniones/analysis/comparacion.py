import json
import os
import numpy as np

def comparar_resultados(nuevos_resultados):
    resultados_path = 'resultados/resultados_actuales.json'
    
    # Asegurarse de que el archivo de resultados existe y es válido
    if os.path.exists(resultados_path):
        try:
            with open(resultados_path, 'r') as file:
                resultados_anteriores = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error al leer el archivo JSON: {e}")
            resultados_anteriores = {}
    else:
        resultados_anteriores = {}
    
    # Asegurarse de que los resultados nuevos sean serializables
    resultados_comparacion = {
        'emociones_anteriores': resultados_anteriores.get('emociones', {}),
        'emociones_nuevos': {key: list(value) if isinstance(value, np.ndarray) else value for key, value in nuevos_resultados.get('emociones', {}).items()},
        'temas_anteriores': resultados_anteriores.get('temas', []),
        'temas_nuevos': [list(topic) for topic in nuevos_resultados.get('temas', [])]
    }
    
    # Convertir nuevos_resultados a un formato serializable
    serializable_resultados = {
        'emociones': {key: list(value) if isinstance(value, np.ndarray) else value for key, value in nuevos_resultados.get('emociones', {}).items()},
        'temas': [list(topic) for topic in nuevos_resultados.get('temas', [])]
    }
    
    # Guardar los nuevos resultados en el archivo JSON
    try:
        with open(resultados_path, 'w') as file:
            json.dump(serializable_resultados, file)
    except TypeError as e:
        print(f"Error al escribir el archivo JSON: {e}")
    
    return resultados_comparacion
