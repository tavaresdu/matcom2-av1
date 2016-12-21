import scipy.integrate as integrate
from tabulate import tabulate
from math import *
import sys
import csv

name = sys.argv[0]

def main(algorithm, filename):
    with open(filename, 'r') as csvfile:
        rows = list(csv.reader(csvfile, delimiter=','))
        for row in rows:
            equation = row[0]
            row[0] = lambda x: eval(equation)
            for i in range(1, len(row)):
                row[i] = float(row[i])
            algorithm(*row)

def print_table(header, rows):
    print(tabulate(rows, headers=header, tablefmt='grid'))

def trapezio(f, a, b, quantity, *args):
    rows = list()
    total_area = int()
    h = (b - a) / quantity
    total_result = integrate.quad(f, a, b)[0]

    header = ['Trapézio', 'Área (Trapézio)', 'Valor Real', 'Erro (%)']

    for i in range(int(quantity)):
        x0 = a + (h * i)
        x1 = a + (h * (i + 1))
        result_i = integrate.quad(f, x0, x1)[0]
        area_i = (f(x0) + f(x1)) * h / 2
        error_i = (result_i - area_i) / result_i * 100
        rows.append([i+1, area_i, result_i, error_i])
        total_area += area_i

    total_error = (total_result - total_area) / total_result * 100
    rows.append(['Total', total_area, total_result, total_error])

    print_table(header, rows)

def simpson_1_3(f, a, b, *args):
    header = ['Área (Parábola)', 'Valor Real', 'Erro (%)']

    result = integrate.quad(f, a, b)[0]
    h = (b - a) / 2
    area_p = (f(a) + 4 * f(a + h) + f(b)) * h / 3
    error = (result - area_p) / result * 100
    row = [[area_p, result, error]]

    print_table(header, row)

def simpson_3_8(f, a, b, *args):
    header = ['Área (Parábola)', 'Valor Real', 'Erro (%)']

    result = integrate.quad(f, a, b)[0]
    h = (b - a) / 3
    area_p = (f(a) + 3 * f(a + h) + 3 * f(a + h * 2) + f(b)) * 3 * h / 8
    error = (result - area_p) / result * 100
    row = [[area_p, result, error]]

    print_table(header, row)

def romberg(f, a, b, q, *args):
    pass

if __name__ == '__main__':
    algs = {
        'tr': trapezio,
        's3': simpson_1_3,
        's8': simpson_3_8,
        'ro': romberg
    }

    if len(sys.argv) == 3:
        main(algs[sys.argv[1]], sys.argv[2])
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

    Arquivo de Entrada: CSV (Escrever equações e valores na sintaxe do Python)
        Coluna 1 = Função à integrar
        Coluna 2 = Valor de A (X inicial)
        Coluna 3 = Valor de B (X final)
        Coluna 4 = Quantidade de iterações (Somente utilizado nos Trapézios)

        O algorítmo suporta o cálculo de múltiplas funções
        caso o arquivo de entrada tenha mais de uma linha.
""".format(name=name))
