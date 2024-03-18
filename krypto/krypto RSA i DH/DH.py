import sympy
import random
from collections import defaultdict
licznosc_gupy = int(input())

def DH(licznosc):
    liczba_pierwsza = 9743
    pier_pierwotny = sympy.primitive_root(liczba_pierwsza)
    klucz_prywatny = {}
    obliczone = {}
    obliczone_k = defaultdict(list)

    for i in range(licznosc):
        big_int = random.randint(4000, 10000)
        klucz_prywatny[i] = big_int
        X = pow(pier_pierwotny, big_int, liczba_pierwsza)
        obliczone[i] = X
    
    for i in range(licznosc):
        
        for j in obliczone.keys():
            if j == i:
                continue
            else:
                 k = pow(obliczone[j], klucz_prywatny[i], liczba_pierwsza)
                 obliczone_k[i].append(k)
    
    

    for k, l in obliczone_k.items():
        for k2, l2 in obliczone_k.items():
            if k != k2:
                set1 = set(l)
                set2 = set(l2)
                if set1.intersection(set2):
                    continue
                else:
                    return False, obliczone_k
    return True, obliczone_k


odp, wynik = DH(licznosc_gupy)
if odp == False:
    print("Ktos ma bledne klucze")
    print(wynik)
else:
    print("Kazdy ma klucze wszystkich pozostalych w grupie")
    print(wynik)