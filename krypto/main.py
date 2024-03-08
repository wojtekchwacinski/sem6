import math
import sympy
# liczby pierwsze 
p = 7451
q = 1291

N = p * q

#print(3%4)
#print(p%4)
#print(q%4)

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
for i in range(20000):
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
#dla 1 
seria1_1 = 0
seria1_2 = 0
seria1_3 = 0
seria1_4 = 0
seria1_5 = 0
seria1_6 = 0
def test_serii(bity):
    for i in range(len(bity)):
        if 

    
