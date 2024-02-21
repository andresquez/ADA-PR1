# Universidad del Valle de Guatemala
# Analisis y Diseño de Algoritmos
# Proyecto 1
# Grupo A1

# librerias
import itertools
import time
import json

# importar archivos de cadena y configuración
filee = 'cadena.txt'
config_file = 'config.json'

initial_pos = 1

class Turing:
    def __init__(self, tape, turing_table, initial_pos=1) -> None:
        self.tape = tape
        self.pos = initial_pos
        self.turing_table = turing_table
        self.value = self.tape[self.pos]
        self.state = "0"

    def move(self) -> None:
        self.value = self.tape[self.pos]

        new = self.turing_table[self.state][self.value]

        self.state = new[0]
        self.tape[self.pos] = new[1]
        self.pos += new[2]

        # Se imprime el movimiento de la máquina
        # Dependiendo el número de espacios en la máquina se cambian por _
        tape_str = ''.join(self.tape).replace("X", "□")
        # Muestra en dónde se encuentra la cabeza
        head_str = ''.join([' ']*(self.pos+1)) + '\u2193'
        if self.pos < len(tape_str):
            prueba = tape_str[:self.pos]+"["+tape_str[self.pos]+"]" + tape_str[self.pos +1:]
        else:
            prueba = tape_str[:self.pos]+"[ ]" + tape_str[self.pos:]
        print(head_str)
        print(prueba)
        print(f"State: {self.state}")
        print()

    def run(self) -> (str, float):
        start_time = time.time()
        while self.state != "18":
            self.move()
        elapsed_time = time.time() - start_time
        print("Tiempo tomado: %s segundos" % elapsed_time)
        return ("".join(self.tape).replace("X", "") + " = " + str(self.tape.count("1")), elapsed_time)

def multiple(file_name, config_file):
    f = open(config_file)
    data = json.load(f)
    turing_table = data["transitions"]
    line_list = []
    output_list = []

    with open(file_name, 'r') as archivo:
        for line in archivo:
            line_list.append(line.strip())

    if len(line_list) == 1:
        taper = ["X"] + list(itertools.chain(*line_list[0])) + ["X"]
        result, elapsed_time = Turing(taper, turing_table).run()
        output_list.append(result + ' - Tiempo: ' + str(elapsed_time) + ' segundos\n')
    else:
        for i in line_list:
            taper = ["X"] + list(itertools.chain(*i)) + ["X"] * 50 * ((len(line_list)) * 2 - 2)
            result, elapsed_time = Turing(taper, turing_table).run()
            output_list.append(result + ' - Tiempo: ' + str(elapsed_time) + ' segundos\n')

    with open('result.txt', 'a') as file:
        file.truncate(0)
        file.writelines(output_list)

multiple(filee, config_file)
