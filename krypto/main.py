import math
import sympy
# liczby pierwsze 
p = 7451
q = 9767

N = p * q

#print(3%4)
#print(p%4)
print(q%4)

x_0 = sympy.randprime(1000,9000)
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a
    
print(nwd(x_0, N))


print(x_0)

out = []
out_bit = []
x_1 = pow(x_0, 2, N)
out.append(x_1)
out_bit.append(out[-1] & 1)


for i in range(19999):
    x = pow(out[-1], 2, N)
    out.append(x)
    out_bit.append(out[-1] & 1)

#print(out)
#print(out_bit)
    
#test pojedyńczych bitów
suma_0 = 0
suma_1 = 0

for bit in out_bit:
    if bit == 1:
        suma_1 += 1
    else:
        suma_0 += 1

if suma_0 < 10275 and suma_0 > 9725:

    print(f"Ilość 0 w ciągu bitów o długości 20000: {suma_0}")
    print(f"Ilość 1 w ciągu bitów o długości 20000: {suma_1}")
elif suma_0 > 10275:
    print("Ilość 0 jest za duża")
    print("Ilość 1 jest za mała")
else: 
    print("Ilość 0 jest za mała")
    print("Ilość 1 jest za duża")




#test serii 
#dla 1 i 0
serie_1 = {}
serie_0 = {}
for i in range(0, 7):
    serie_1[i] = 0
    serie_0[i] = 0

curr_series_1 = 0
curr_series_0 = 0
for b in out_bit:
    if b == 1:
        curr_series_1 += 1
        if curr_series_0 > 6:
            curr_series_0 = 6
        serie_0[curr_series_0] += 1
        curr_series_0 = 0
    elif b == 0:
        if curr_series_1 > 6:
            curr_series_1 = 6
        serie_1[curr_series_1] += 1
        curr_series_1 = 0
        curr_series_0 += 1
    
print(f"Długości serii 1 ")
for key in list(serie_1.keys())[1:]:
    print(key, ":", serie_1[key])
print(f"Długości serii 0 ")
for key in list(serie_0.keys())[1:]:
    print(key, ":", serie_0[key])

#test długiej seerii
long_series_1 = 0
long_series_0 = 0
test_pass = 0
max_1 = 0
max_0 = 0
for bi in out_bit:
    if bi == 1:
        long_series_1 += 1
        if long_series_1 > max_1:
            max_1 = long_series_1
        long_series_0 = 0
        if long_series_1 >= 26:
            test_pass = 1
            break
    elif bi == 0:
        long_series_1 = 0
        long_series_0 += 1
        if long_series_0 > max_0:
            max_0 = long_series_0
        if long_series_0 >= 26:
            test_pass = 1
            break
print(f"Najdłuższe ciągi 1 i 0: {max_1}, {max_0}")
if test_pass == 0:
    print("Obecny ciąg bitów przeszedł test długiej serii")
else:
    print("Obecny ciąg nie przeszedł próby długej serii")



#test pokerowy

sublists = [out_bit[i:i+4] for i in range(0, len(out_bit), 4)]
licznosci = {}
for i in range(0, 16):
    licznosci[i] = 0

for list in sublists:
    wynik = 8 * list[0] + 4 * list[1] + 2 * list[2] + 1 * list[3]
    #print(wynik)
    licznosci[wynik] += 1

print(licznosci)
#oblcizenie sumy
suma = 0
for i in range(0, 16):
    suma += licznosci[i] * licznosci[i]

x = (16/5000) * suma - 5000

if x > 2.16 and x < 46.17:
    print(f"Test pokerowy zkończył się powodzeniem z wynikiem x: {x}")
else:
    print(f"Test pokerowy zkończył się niepowodzeniem z wynikiem x: {x}")


