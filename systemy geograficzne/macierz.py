import re
from docplex.mp.model import Model
import time
file_name = "CM_n=20_m=7.txt"
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


model = Model()
model.populate_solution_pool = True

x = {(i, j): model.binary_var(name=f'x_{i}_{j}') for i in range(n) for j in range(m)}

#for i in range(n):
#    model.add_constraint(model.sum(x[i, j] for j in range(m) ) == 1, ctname=f'sum_row_{i}')
for i in range(n):
    model.add_constraint(x[i, 0]+x[i, 1]+x[i, 2]+x[i, 3]+x[i, 4]+x[i, 5]+x[i,6] == 1)

flaga = 0 
for i in range(len(matrix)):
    if i%m == 0:
        flaga += 1
    for j in range(flaga*m, len(matrix[i])):
        if matrix[i][j] == 1 and i != j:
            print(i,j,"\n")
            nr_pierwszego_samolotu = int(i/m)

            nr_pierwszego_manewru = j
            while nr_pierwszego_manewru > (m-1):
                nr_pierwszego_manewru = nr_pierwszego_manewru - m


            nr_drugiego_samolotu = int(j/m)

            nr_drugiego_manewru = i
            while nr_drugiego_manewru > (m-1):
                nr_drugiego_manewru = nr_drugiego_manewru - m

            print(f"pierwsza zmienna: samolot nr: {nr_pierwszego_samolotu} manewr nr: {nr_pierwszego_manewru}")
            print(f"druga zmienna: samolot nr: {nr_drugiego_samolotu} manewr nr: {nr_drugiego_manewru}")
            model.add_constraint(x[nr_pierwszego_samolotu, nr_pierwszego_manewru] + x[nr_drugiego_samolotu, nr_drugiego_manewru] <= 1)
model.minimize(1) 


start = time.time()
solution = model.solve()
end = time.time()
print(f"Czas potrzebny na obliczenia: {end-start}[s]")
#print(solution)
#print(x)

print(f"Liczba znalezionych rozwiązań dopuszczalnych: {model.populate().size}")


if solution is not None:
    print("Przykłądowe rozwiązanie\n")    
    for i in range(n):
        for j in range(m):
            if x[i,j].solution_value == 1:
                print(f'Samolot {i}, manewr {j}: {x[i, j].solution_value}')
else:
    print('Brak rozwiązania.')