from math import *
import sys
import csv

name = sys.argv[0]

def main(algorithm, filename):
    with open(filename, 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=';')
        function = lambda x: eval(rows[0])
        algorithm(function, float(rows[1]), float(rows[2]), float(rows[3]))

def print_table(header, rows):
    print(tabulate(rows, headers=header, tablefmt='grid'))

def trapezio(f, a, b, q):
    rows = list()
    h = (b - a) / i

    for i in range(q):
        x = a + (h)


def simpson_1_3(f, a, b, q):
    pass

def simpson_3_8(f, a, b, q):
    pass

def romberg(f, a, b, q):
    pass

if __name__ == '__main__':
    algs = {
        'tr': trapezio,
        's3': simpson_1_3,
        's8': simpson_3_8,
        'ro': romberg
    }

    if sys.argv == 3:
        main(algs[sys.argv[1]],
            sys.argv[2],
            )
    else:
        print("""\
Como usar:
    python {name} [sigla do método] [arquivo de entrada]
    Exemplo: python {name} tr input.csv

    Métodos disponíveis (e siglas):
        Método dos Trapézios  (tr)
        Regra de Simpson 1/3  (s3)
        Regra de Simpson 3/8  (s8)
        Integração de Romberg (ro)

    Arquivo de Entrada: CSV
        Coluna 1 = Função à integrar (na sintaxe do Python)
        Coluna 2 = Valor de A (X inicial)
        Coluna 3 = Valor de B (X final)
        Coluna 4 = Quantidade de iterações

        O algorítmo suporta o cálculo de múltiplas funções
        caso o arquivo de entrada tenha mais de uma linha.
""".format(name=name))
