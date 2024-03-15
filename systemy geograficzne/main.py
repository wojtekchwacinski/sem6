
from docplex.mp.model import Model

# Dane wejściowe
n = 2  # Liczba samolotów
m = 7  # Liczba manewrów dla każdego samolotu

# Macierz konfliktów (tu przykładowa macierz z wcześniejszego wpisu)
CM = [
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Tworzenie modelu
model = Model()

# Zmienne decyzyjne
x = {(i, j): model.binary_var(name=f'x_{i}_{j}') for i in range(1, n + 1) for j in range(1, m + 1)}

# Ograniczenia sumujące się do 1 dla każdego samolotu
#for i in range(1, n + 1):
#    model.add_constraint(model.sum(x[i, j] for j in range(1, m + 1)) == 1)
model.add_constraint(x[1, 1] + x[1, 2] + x[1, 3] + x[1, 4] + x[1, 5] + x[1, 6] + x[1, 7] == 1)
model.add_constraint(x[2, 1] + x[2, 2] + x[2, 3] + x[2, 4] + x[2, 5] + x[2, 6] + x[2, 7] == 1)

# Dodawanie ograniczeń wynikających z macierzy konfliktów
model.add_constraint(x[1, 1] + x[2, 5] <= 1)
model.add_constraint(x[1, 1] + x[2, 5] <= 1)
model.add_constraint(x[1, 7] + x[2, 4] <= 1)
model.add_constraint(x[1, 7] + x[2, 6] <= 1)

# Dodawanie ograniczeń wynikających z macierzy konfliktów
#for i in range(1, n + 1):
#    for j in range(1, m + 1):
#        for k in range(1, n + 1):
#            for l in range(1, m + 1):
#                if CM[(i - 1) * m + j - 1][(k - 1) * m + l - 1] == 1:
#                    model.add_constraint(x[i, j] + x[k, l] <= 1)

# Minimalizacja (stała funkcja celu)
model.minimize(1)

# Rozwiązanie modelu
solution = model.solve()

# Wypisanie rozwiązania
if solution:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i, j].solution_value == 1:
                print(f'Samolot {i}, Manewr {j}')
else:
    print("Nie znaleziono rozwiąz")