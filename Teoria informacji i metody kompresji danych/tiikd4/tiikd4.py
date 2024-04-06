import random
import string
import itertools
import sys
import math 
import os
def wczytywanie(file):
    plik = open(file, 'r', encoding='UTF-8')
    content = plik.readlines()

    return content

def srednia_dlugosc(tekst):
    text = tekst.split()
    return sum(len(word) for word in text) / len(text)



def prawdopodobienstwo_liter(plik, rzad):

    text = wczytywanie(plik)

    slownik = {}
    i = 1
    for l in range(1, len(text[0])-rzad):
        
        znak = text[0][l:l+rzad]
        if znak in slownik:
            slownik[znak] +=1
        else:
            slownik[znak] = 1
        i += 1
           




    sort_slow = {key: value for key, value in sorted(slownik.items(), key=lambda item: item[1], reverse=True)}

  
   
    prawdopod = {}
    for key in slownik:
        prawdopod[key] = slownik[key] / i

    sort_prawd = {key: value for key, value in sorted(prawdopod.items(), key=lambda item: item[1], reverse=True)}


    return sort_prawd

def prawdopodobienstwo_slow(plik, rzad):

    text = wczytywanie(plik)
    content = text[0]
    content = content.split(" ")
   
    slownik = {}
    i = 0
    for l in range(1, len(content)-rzad):
        
        znak = content[l:l+rzad]
        string = ' '.join(znak)
        if string in slownik:
            slownik[string] +=1
            
        else:
            slownik[string] = 1
        i += 1
    sort_slow = {key: value for key, value in sorted(slownik.items(), key=lambda item: item[1], reverse=True)}

 
    prawdopod = {}
    for key in slownik:
        prawdopod[key] = slownik[key] / i

    sort_prawd = {key: value for key, value in sorted(prawdopod.items(), key=lambda item: item[1], reverse=True)}


    return sort_prawd




#zad1
def entropia(prawd):
    entropy = 0
    
    for prob in prawd.values():
    
        if prob > 0.0:
        
            logarytm = math.log2(prob)
            entropy += prob*logarytm

    return -1*entropy

def entropia_warunkowa(prawd):
    entropy = 0
    
    for prob in prawd.values():
    
        if prob > 0.0:
        
            logarytm = math.log2(prob)
            entropy += prob*logarytm

    return -1*entropy


if __name__ == '__main__':

    wejscie = sys.argv[1:]
    #plik_in = str(wejscie[0])
    #wielkosc = int(wejscie[1])
    plik_out = str(wejscie[0])


  
 
    path = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\tiikd4'
    entr_liter = []
    entr_slow = []
    entr_war_liter = []
    entr_war_slow = []


    

    #entropia dla słów i liter
    print("Entropia dla słów i liter")
    for plik in os.listdir(path):
        if plik.endswith('.txt'):
            for i in range(1, 5):
                prawd_slow = prawdopodobienstwo_slow(plik, i)
                prawd_liter = prawdopodobienstwo_liter(plik, i)
                suma = sum(value for value in prawd_slow.values())
                print(suma)
                e_slow = entropia(prawd_slow)
                e_liter = entropia(prawd_liter)
                entr_liter.append(e_liter)
                entr_slow.append(e_slow)
            print(f"Dla pliku: {plik}")
            print(f"Entropia dla liter wyniosla: {entr_liter}")
            print(f"Entropia slow wyniosla: {entr_slow}")


            for x in range(1, len(entr_liter)):
                entr_war_liter.append(entr_liter[x]-entr_liter[x-1])
                entr_war_slow.append(entr_slow[x] - entr_slow[x-1])
            entr_war_liter.insert(0, entr_liter[0])
            entr_war_slow.insert(0, entr_slow[0])

            print(f"Entropia warunkowa dla liter wyniosla: {entr_war_liter}")
            print(f"Entropia warunkowa dla slow wyniosla: {entr_war_slow}")
            entr_slow = []
            entr_liter = []
            entr_war_liter = []
            entr_war_slow = []


    
