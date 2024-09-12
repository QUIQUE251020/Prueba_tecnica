import sys

def contiene_letras(nombre_vino, letras):
    # Convertimos el nombre del vino y las letras a minúsculas para hacer la comparación insensible a mayúsculas
    nombre_vino = nombre_vino.lower()
    letras = letras.lower()
    
    # Comprobamos si todas las letras están presentes en el nombre del vino
    for letra in letras:
        if letra not in nombre_vino:
            return False
    return True

def procesar_archivo(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            # Eliminamos los espacios en blanco extra
            linea = linea.strip()
            if not linea:
                continue
            
            # Dividimos la línea en el nombre del vino y las letras recordadas
            try:
                nombre_vino, letras = linea.split('|')
                nombre_vino = nombre_vino.strip()
                letras = letras.strip()
            except ValueError:
                print("Formato de línea incorrecto:", linea)
                continue
            
            # Verificamos si el nombre del vino contiene todas las letras
            if contiene_letras(nombre_vino, letras):
                print(nombre_vino)
            else:
                print("False")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo como argumento.")
        sys.exit(1)
    
    archivo = sys.argv[1]
    procesar_archivo(archivo)
