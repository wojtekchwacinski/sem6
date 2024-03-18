import random
import math
#liczby pierwsze p i q

p = 7451
q = 9767

n = p * q

phi = (p - 1) * (q - 1)

def wyznacz_e(phi):
    while True:
        r = random.randint(2, phi)
        if math.gcd(r, phi) == 1:
            return r
e = wyznacz_e(phi)

d = pow(e, -1, phi)

print((e*d-1)/phi)

print(f"p: {p}, q: {q}, n: {n}, phi: {phi}, e: {e}, d: {d}")

wiadomosc = "Jutro slonce wschodzi o piatej rano, pamietaj!"
print(f"Wiadomosc: {wiadomosc}")
#szyfrowanie
#klucz_publiczny - e i n 
#szyfrogrm - c
c = []

for znak in wiadomosc:
    c.append(pow(ord(znak), e, n))

print(f"Wiadomosc zaszyfrowana: {c}")

#deszyfrowanie
#klucz_prywatny - d i n
m = ""
for kod in c:
    m += chr(pow(kod, d, n))

print(f"Wiadomosc po odszyfrowaniu: {m}")
