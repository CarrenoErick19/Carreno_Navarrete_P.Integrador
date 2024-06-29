#1. Este archivo será el punto de entrada de tu proyecto y desde 
# donde importarás las funciones necesarias de los otros archivos.

# main.py

from load_data import mostrar_datos_csv
from clean_data import limpiar_datos

def main():
    # Mostrar datos del CSV
    mostrar_datos_csv()
    
    # Limpiar datos
    limpiar_datos()

if __name__ == "__main__":
    main()
