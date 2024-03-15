from docplex.mp.model import Model
import re
file_name = "CM_n=2_m=7.txt"
numbers = re.findall(r'\d+', file_name)
print(numbers)
file = open(file_name, 'r', encoding='Utf-8')

matrix = []
n = int(numbers[0])  # liczba samolotów
m = int(numbers[1])  # liczba manewrów
print(n, m)

for i in range(n*m):
    read = file.readline()
    num = re.findall(r'\d+', read)
    dane = list(map(int, num))
    matrix.append(dane)
print(matrix)
def solve_aircraft_conflict(n, m, CM):
    # Tworzenie modelu
    model = Model()

    # Zmienne decyzyjne
    x = {(i, j): model.binary_var(name=f'x_{i}_{j}') for i in range(n*m) for j in range(n*m)}

    # Ograniczenia
    # Każdy samolot może wykonać tylko jeden manewr
    for i in range(n):
        model.add_constraint(model.sum(x[i, j] for j in range(m) ) == 1, ctname=f'sum_row_{i}')
    czik = 0
    # Unikanie konfliktów
    
    for i in range(n):
        for j in range(m):
            for k in range(n):
                for l in range(m):
                    if CM[(i-1)*m+j][(k-1)*m+l] == 1 and i != k:
                        model.add_constraint(x[i, j] + x[k, l] <= 1)
    #for i in range(n*m):
    #    for j in range(i+1, n*m):
    #        if CM[i][j] == 1:
    #            model.add_constraint(x[i+1, j+1] + x[j+1, i+1] <= 1)
    # Rozwiązanie
    model.minimize(1)  # Funkcja celu jest stała, szukamy tylko rozwiązania dopuszczalnego
    solution = model.solve()

    if solution is not None:
        # Wypisanie rozwiązania
        for i in range(n):
            for j in range(m):
                print(f'Samolot {i}, manewr {j}: {x[i, j].solution_value}')
    else:
        print('Brak rozwiązania.')

# Dane wejści

# Rozwiązanie problemu
solve_aircraft_conflict(n, m, matrix)
