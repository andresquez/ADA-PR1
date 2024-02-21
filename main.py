# Universidad del Valle de Guatemala
# Analisis y Diseño de Algoritmos
# Proyecto 1
# Grupo A1

# Librerías
import time
import json
import itertools

# Archivos de entrada
cadena_entrada = 'cadena.txt'
configuracion_archivo = 'config.json'

posicion_inicial = 1

class MaquinaTuring:
    def __init__(self, cinta, tabla_turing, posicion_inicial=1) -> None:
        self.cinta = cinta
        self.posicion = posicion_inicial
        self.tabla_turing = tabla_turing
        self.valor = self.cinta[self.posicion]
        self.estado = "0"

    def mover(self) -> None:
        self.valor = self.cinta[self.posicion]

        nueva = self.tabla_turing[self.estado][self.valor]

        self.estado = nueva[0]
        self.cinta[self.posicion] = nueva[1]
        self.posicion += nueva[2]

        cinta_str = ''.join(self.cinta).replace("X", "□")
        cabeza_str = ''.join([' ']*(self.posicion+1)) + '\u2193'
        if self.posicion < len(cinta_str):
            visualizacion_cinta = cinta_str[:self.posicion]+"["+cinta_str[self.posicion]+"]" + cinta_str[self.posicion +1:]
        else:
            visualizacion_cinta = cinta_str[:self.posicion]+"[ ]" + cinta_str[self.posicion:]
        print(cabeza_str)
        print(visualizacion_cinta)
        print(f"Estado: {self.estado}")
        print()

    def ejecutar(self) -> (str, float):
        tiempo_inicio = time.time()
        while self.estado != "18":
            self.mover()
        tiempo_transcurrido = time.time() - tiempo_inicio
        print("Tiempo transcurrido: %s segundos" % tiempo_transcurrido)
        return ("".join(self.cinta).replace("X", "") + " = " + str(self.cinta.count("1")), tiempo_transcurrido)

def read_multiple_lines(nombre_archivo, archivo_configuracion):
    archivo = open(archivo_configuracion)
    datos = json.load(archivo)
    tabla_turing = datos["transitions"]
    lista_lineas = []
    lista_resultados = []

    with open(nombre_archivo, 'r') as archivo_entrada:
        for linea in archivo_entrada:
            lista_lineas.append(linea.strip())

    if len(lista_lineas) == 1:
        cinta = ["X"] + list(itertools.chain(*lista_lineas[0])) + ["X"]
        resultado, tiempo_transcurrido = MaquinaTuring(cinta, tabla_turing).ejecutar()
        lista_resultados.append(resultado + ' - Tiempo: ' + str(tiempo_transcurrido) + ' segundos\n')
    else:
        for i in lista_lineas:
            cinta = ["X"] + list(itertools.chain(*i)) + ["X"] * 50 * ((len(lista_lineas)) * 2 - 2)
            resultado, tiempo_transcurrido = MaquinaTuring(cinta, tabla_turing).ejecutar()
            lista_resultados.append(resultado + ' - Tiempo: ' + str(tiempo_transcurrido) + ' segundos\n')

    with open('resultado.txt', 'a') as archivo_salida:
        archivo_salida.truncate(0)
        archivo_salida.writelines(lista_resultados)

read_multiple_lines(cadena_entrada, configuracion_archivo)
