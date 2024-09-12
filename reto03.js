const fs = require('fs');

const monedas = [1, 5, 10, 25, 50];
// Variable global para almacenar los resultados
let resultados = [];

// Función recursiva para encontrar las combinaciones
function encontrarCombinaciones(sumatoria, start, combinacionActual, cantidad) {
    if (sumatoria === cantidad) {
        resultados.push(combinacionActual.join("+"));
        return;
    }

    for (let i = start; i < monedas.length; i++) {
        const moneda = monedas[i];
        if (sumatoria + moneda <= cantidad) {
            // Llamada recursiva con la nueva sumatoria y manteniendo el índice para permitir reutilización de la misma moneda
            encontrarCombinaciones(sumatoria + moneda, i, combinacionActual.concat(moneda), cantidad);
        }
    }
}

function encontrarTodasLasCombinaciones(cantidad) {
    resultados = [];
    encontrarCombinaciones(0, 0, [], cantidad);
    return resultados;
}

// Función para procesar el archivo de entrada
function procesarArchivo(rutaArchivo) {
    fs.readFile(rutaArchivo, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error al leer el archivo: ${err.message}`);
            return;
        }

        // Dividimos el archivo en líneas y procesamos cada una
        const lineas = data.split('\n').filter(linea => linea.trim() !== '');
        lineas.forEach((linea, index) => {
            const cantidad = parseInt(linea.trim(), 10);
            
            if (!isNaN(cantidad)) {
                console.group(`Caso ${index + 1}:`);
                resultados = encontrarTodasLasCombinaciones(cantidad);
                console.log(`Combinaciones posibles:\n${resultados.join("\n")}`);
                console.log(`Hay ${resultados.length} maneras de hacer ${cantidad} centavos.`);
                console.groupEnd();
            } else {
                console.log(`Línea ${index + 1} no es un número válido: "${linea}"`);
            }
        });
    });
}

// Ejemplo de llamada a la función procesarArchivo con una ruta de archivo
// procesarArchivo('archivo_de_entrada.txt');


// Verificación de argumentos
if (process.argv.length < 3) {
	console.log("Uso: node reto01.js archivo_de_entrada.txt");
	process.exit(1);
}

// Tomamos el archivo de entrada del argumento
const archivoEntrada = process.argv[2];
procesarArchivo(archivoEntrada);