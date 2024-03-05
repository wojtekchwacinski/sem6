import random
import string
import itertools
import sys
def wczytywanie(file):
    plik = open(file, 'r', encoding='UTF-8')
    content = plik.readlines()

    return content

def srednia_dlugosc(tekst):
    text = tekst.split()
    return sum(len(word) for word in text) / len(text)

def zad_1():
    alfabet = "mnbvcxzlkjhgfdsapoiuytrewq "
    belkot = []

    for i in range(0,100):
        belkot.append("")
        for j in range(0,81):
            losowy = random.choice(alfabet)
            belkot[i] = belkot[i] + losowy
        print(f"{belkot[i]} \n")

    #print(belkot)

    ile_znakow = 0
    ile_spacji = 0
    for zdania in belkot:
        for i in zdania:
            if i != " ":
                ile_znakow += 1
            else:
                ile_spacji += 1
    srednia_długosc = ile_znakow/ile_spacji
    print(f"Liczba wyrazów: {ile_znakow}, liczba spacji: {ile_spacji}")
    print(f"Średnia długość słów w bełkocie: {srednia_długosc}")


def zad_2(plik):
    plik1 = 'norm_hamlet.txt'
    plik2 = 'norm_romeo.txt'
    plik3 = 'norm_wiki_sample.txt'
    text = wczytywanie(plik)
    #print(text[0])
    slownik = {}
    i = 0
    for znak in text[0]:
        i += 1
        if znak in slownik:
            slownik[znak] +=1
        else:
            slownik[znak] = 0


    print(slownik)

    sort_slow = {key: value for key, value in sorted(slownik.items(), key=lambda item: item[1], reverse=True)}

    print(sort_slow)
    alfabet = "mnbvcxzlkjhgfdsapoiuytrewq "
    prawdopod = {}
    for item in alfabet:
        prawdopod[item] = round(slownik[item] / i, 4)

    sort_prawd = {key: value for key, value in sorted(prawdopod.items(), key=lambda item: item[1], reverse=True)}

    print(sort_prawd)
    return sort_prawd, text[0]


def zad_3(prawd, tekst):


    belkot = ""
    for j in range(1000):
        znak = random.choices(list(prawd.keys()), weights=list(prawd.values()), k=1)[0]
        belkot += znak



    ile_znakow = 0
    ile_spacji = 0
    for i in belkot:
        if i != " ":
            ile_znakow += 1
        else:
            ile_spacji += 1
    #print(ile_spacji)
    srednia_długosc = ile_znakow/ile_spacji
    print(f"Liczba wyrazów: {ile_znakow}, liczba spacji: {ile_spacji}")
    print(f"Średnia długość słów w bełkocie: {srednia_długosc}")

    ile_znakow_2 = 0
    ile_spacji_2 = 0
    for i in tekst:
        if i != " ":
            ile_znakow_2 += 1
        else:
            ile_spacji_2 += 1
    #print(ile_spacji)
    srednia_długosc_2 = ile_znakow_2/ile_spacji_2
    print(f"Liczba wyrazów: {ile_znakow_2}, liczba spacji: {ile_spacji_2}")
    print(f"Średnia długość słów w tekscie: {srednia_długosc_2}")

    print(srednia_dlugosc(belkot))
    print(srednia_dlugosc(tekst))


def zad_4(prawd, tekst):
    top_znaki = ' e'

    prawd_po = {}
    ilosci = {}
    suma = 0
    for znak in top_znaki:
        i = 0
        for znaczek in tekst:
            if tekst[i-1] == ' ' or tekst[i-1] == 'e':
                x = znak + znaczek
                if x in ilosci:
                    ilosci[x] += 1
                else:
                    ilosci[x] = 0
                suma += 1
            i += 1

    ilosci_sort = {key: value for key, value in sorted(ilosci.items(), key=lambda item: item[1], reverse=True)}
    print(ilosci_sort)

    for item in ilosci_sort:
        prawd_po[item] = float(ilosci_sort[item] / suma)
    print(prawd_po)

    prawd_2 = {}
    for itemek in ilosci_sort:
        prawd_2[itemek] = prawd_po[itemek] / prawd[itemek[0]]

    print(prawd_2)


def markov_chain(tekst, rzad):
    markov = {}
    for i in range(len(tekst) - rzad):
        x = tekst[i:i+rzad]
        next_x = tekst[i+rzad]
        markov.setdefault(x, []).append(next_x)

    #print(markov)
    return markov
def generator(markov, wielkosc, rzad, poczatek=None):



    if poczatek == None:
        poczatek = random.choice(list(markov.keys()))

    while len(poczatek) < wielkosc:
        klucz = poczatek[-rzad:]
        if klucz in markov:
            poczatek += random.choice(markov[klucz])


    return poczatek





def zad_5(tekst, plik_out, wielkosc):
    dict_1 = markov_chain(tekst, 1)
    text_1 = generator(dict_1, wielkosc, rzad=1)
    print(text_1)
    print(srednia_dlugosc(text_1))
    dict_2 = markov_chain(tekst, 3)
    text_2 = generator(dict_2, wielkosc, rzad=3)
    print(text_2)
    print(srednia_dlugosc(text_2))
    dict_3 = markov_chain(tekst, 5)
    text_3 = generator(dict_3, wielkosc, rzad=5, poczatek='probability')
    print(text_3)
    print(srednia_dlugosc(text_3))


    file = open(plik_out, 'w', encoding='Utf-8')

    file.write('I\n')
    file.write(f"Ciag pierwszy: {text_1}\n")
    file.write(f"Srednia długosc slowa: {srednia_dlugosc(text_1)}\n")

    file.write('II\n')
    file.write(f"Ciag pierwszy: {text_2}\n")
    file.write(f"Srednia długosc slowa: {srednia_dlugosc(text_2)}\n")

    file.write('III\n')
    file.write(f"Ciag pierwszy: {text_3}\n")
    file.write(f"Srednia dlugosc slowa: {srednia_dlugosc(text_3)}\n")

    file.close()




if __name__ == '__main__':

    wejscie = sys.argv[1:]
    plik_in = str(wejscie[0])
    wielkosc = int(wejscie[1])
    plik_out = str(wejscie[2])


    #zad_1()
    prawd, tekst = zad_2(plik_in)
    #zad_3(prawd, tekst)
    #zad_4(prawd, tekst)
    zad_5(tekst, plik_out, wielkosc)
