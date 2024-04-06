import random
import sys
import string
import itertools

def wczytywanie(file):
    plik = open(file, 'r', encoding='UTF-8')
    content = plik.readlines()
    tekst = content[0] 
    tekst = tekst.split(" ")
    #print(tekst)
    return tekst


#zad 1
def zad_1(plik):
    #print(plik)
    x = len(plik)
    print(x)
    licznosci = {}
    for slowo in plik:
        if slowo in licznosci:
            licznosci[slowo] += 1

        else:
            licznosci[slowo] = 1


    licznosci = {key: value for key, value in sorted(licznosci.items(), key=lambda item: item[1], reverse=True)}
    proacent = {}
    set1 = set(plik)

    #print(licznosci)
    for i in set1:
        proacent[i] = (licznosci[i]/x) * 100


    procenty = {key: value for key, value in sorted(proacent.items(), key=lambda item: item[1], reverse=True)}
    #print(procenty) 

    counter = 0
    first_6000 = {}
    for key, value in licznosci.items():
        if counter < 6000:
            first_6000[key] = value
            counter += 1
        else:
            break
    
    counter_2 = 0
    first_30000 = {}
    for key, value in licznosci.items():
        if counter_2 < 30000:
            first_30000[key] = value
            counter_2 += 1
        else:
            break
    

    ilosc_6000 = 0
    for key, value in first_6000.items():
        ilosc_6000 += value
    
    ilosc_30000 = 0
    for key, value in first_30000.items():
        ilosc_30000 += value
    print(ilosc_30000)
    print(ilosc_6000)
    print(len(set1))
    print(f"6000 najcześciej uzywanych słów {(ilosc_6000/x) * 100}")
    print(f"30000 najcześciej uzywanych słów {(ilosc_30000/x) * 100}")
    return procenty
def zad_2(plik, prawd):
    x = 1000
    belkot = ""
    for i in range(x):
        znak = random.choices(list(prawd.keys()), weights=list(prawd.values()), k=1)[0]
        belkot += " "
        belkot += znak
    #print(belkot)

def markov_chain(tekst, rzad):
    markov = {}
    print(len(tekst))
    print(tekst[0])
    for i in range(1, len(tekst)-rzad):
        x = tekst[i:i+rzad]
        string = ' '.join(x)
        print(string)
        print(x)
        next_x = tekst[i+rzad]
        markov.setdefault(string, []).append(next_x)

    return markov
def generator(markov, wielkosc, rzad, poczatek=None):
 
    listka = []
    if poczatek == None:
        poczatek = random.choice(list(markov.keys()))
        poczatek.split(" ")
    if poczatek != None:
        keys_starting_withProb = [key for key in markov.keys() if key.startswith(poczatek)]
        poczatek = random.choice(keys_starting_withProb)



    listka.append(poczatek)
    #if poczatek is not None:
    if rzad > 1:
        z = listka[0].split(' ')
        listka.pop()
        for l in range (rzad):

            listka.append(z[l])


    while len(listka) < wielkosc:
        klucz = listka[-rzad:]
        print(klucz[0])
        klucz = ' '.join(klucz)
        if klucz in markov:
            listka.append(random.choice(markov[klucz]))
        else:
            break

    return listka

def zad_3(tekst, plik_out, wielkosc):
    dict_1 = markov_chain(tekst, 1)
    text_1 = generator(dict_1, wielkosc, rzad=1)
    print(text_1)
    
    dict_2 = markov_chain(tekst, 2)
    text_2 = generator(dict_2, wielkosc, rzad=2)
    print(text_2)
    
    dict_3 = markov_chain(tekst, 2)
    text_3 = generator(dict_3, wielkosc, rzad=2, poczatek='probability')
    print(text_3)
    
    file = open(plik_out, 'w', encoding='Utf-8')

    file.write('I\n')
    file.write(f"Ciag pierwszy: {text_1}\n")
 

    file.write('II\n')
    file.write(f"Ciag pierwszy: {text_2}\n")


    file.write('III\n')
    file.write(f"Ciag pierwszy: {text_3}\n")
  

    file.close()




if __name__ == "__main__":
    
    wejscie = sys.argv[1:]
    plik_in = str(wejscie[0])
    wielkosc = int(wejscie[1])
    plik_out = str(wejscie[2])
    tekst = wczytywanie(plik_in)
    prawd = zad_1(tekst)
    zad_2(tekst, prawd)

    zad_3(tekst, plik_out, wielkosc)