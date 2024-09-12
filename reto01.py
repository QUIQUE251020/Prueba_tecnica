import sys

def recontruir_oracion(linea):
    
    palabras, indices = linea.split(";")
    
    lista_palabras = palabras.split()
    
    lista_indices = list(map(int, indices.split()))
    
    # Creamos una lista vacía para la oración reconstruida
    oracion_reconstruida = [None] * len(lista_indices)
    
    # Recorremos los índices y las palabras para colocarlas en las posiciones correctas
    for i, indice in enumerate(lista_indices):
        if 1 <= indice <= len(lista_palabras):
            oracion_reconstruida[indice - 1] = lista_palabras[i]

    return ' '.join(oracion_reconstruida)

def main(archivo):
    
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminamos cualquier espacio en blanco extra
            linea = linea.strip()
            # Reconstruimos y mostramos la oración
            print(recontruir_oracion(linea)) 
            
if __name__ == '__main__':
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        main(archivo)
    else:
        print("proporciona un archivo")
        sys.exit(1)