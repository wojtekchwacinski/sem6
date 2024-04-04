import hashlib
import time
import string
import random
#zad1
def hash(wiadomosc, alogorytm):
    if alogorytm == "MD5":
        hs = hashlib.md5()

    elif alogorytm == "SHA-1":
        hs = hashlib.sha1()
    elif alogorytm == "SHA-224":
        hs = hashlib.sha224()
    elif alogorytm == "SHA-384":
        hs = hashlib.sha384()
    elif alogorytm == "SHA-256":
        hs = hashlib.sha256()
    elif alogorytm == "SHA-512":
        hs = hashlib.sha512()

    elif alogorytm == "SHA-3-224":
        hs = hashlib.sha3_224()
    elif alogorytm == "SHA-3-256":
        hs = hashlib.sha3_256()
    elif alogorytm == "SHA-3-384":
        hs = hashlib.sha3_384()
    elif alogorytm == "SHA-3-512":
        hs = hashlib.sha3_512()
    
    else:
        print("Nie ma takiego algorytmu jak: ", alogorytm)
        return 0

    hs.update(wiadomosc.encode('utf-8'))

    return hs.hexdigest()

def zad2(lista_nazw, dane_wejsciowe):
    for i in range(len(lista_nazw)):

        for j in range(len(dane_wejsciowe)):
            start = time.time()
            hashyk = hash(dane_wejsciowe[j], lista_nazw[i])
            stop = time.time() - start

            print(f"Algorytm hash'ujacy: {lista_nazw[i]}\n", 
            f"Ciag wejsciowy i jego dlugosc: {dane_wejsciowe[j]}, {len(dane_wejsciowe[j])}\n",
            f"Czas dzialania: {stop}\n",
            f"Dlugosc na wyjsciu: {len(hashyk)}")
            print(hashyk)
            print(len(bin(int(hashyk, 16))[2:]))

            print("\n")   



if __name__ == "__main__":
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
    lista_nazw = ["MD5", "SHA-1", "SHA-224" , "SHA-256", "SHA-384", "SHA-512", "SHA-3-224", "SHA-3-256", "SHA-3-384", "SHA-3-512"]
    dane_wejsciowe = ["Kou", "klasa dzis mamy dzien", "fajowo miec 123", "bdo>?()&23", random_string]

    #zad2
    #zad2(lista_nazw, dane_wejsciowe)

    #zad3
    stryng = "Ala "
    print(f"Wartosc wejsciowa: {stryng}")
    haszon = hash(stryng, "MD5")
    print(len(bin(int(haszon, 16))[2:]))
    print(bin(int(haszon, 16)))
    print(f"Wartosc wyjsciowa: {haszon}")

    stryng = "Kot"
    print(f"Wartosc wejsciowa: {stryng}")
    haszon = hash(stryng, "SHA-1")
    print(f"Wartosc wyjsciowa: {haszon}")

    stryng = "Kot"
    print(f"Wartosc wejsciowa: {stryng}")
    haszon = hash(stryng, "SHA-256")

    print(f"Wartosc wyjsciowa: {haszon}")

    #zad5 
    stryng = "Kot"
    stryn2 = "czlek"
    
    haszon = hash(stryng, "SHA-256")
    haszon2 = hash(stryn2, "SHA-256")

    bity_1 = bin(int(haszon, 16))[2:13]
    bity_2 = bin(int(haszon2, 16))[2:13] 

    kolizje = 0

    for i in range(len(bity_1)):
        if bity_1[i] == bity_2[i]:
            kolizje += 1
    print(f"Liczba kolizji w pierwszych 12 bitachdla Kot i czlek: {kolizje}")

    #zad6 

    string_1 = "kotek"
    string_2 = "kouek"

    haszon = hash(string_1, "SHA-256")
    haszon2 = hash(string_2, "SHA-256")
    bity_1 = bin(int(haszon, 16))[2:]
    bity_2 = bin(int(haszon2, 16))[2:] 

    zmiany = 0

    for x in range(len(bity_1)):
        if bity_1[x] != bity_2[x]:
            zmiany += 1
    procent = (zmiany/len(bity_1)) * 100
    print(f"Procentowa liczba bitow ktore ulegly zmianie: {procent}")