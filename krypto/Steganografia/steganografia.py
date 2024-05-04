from PIL import Image
import math 

def pobranie_px(obraz):
    obrazek = Image.open(obraz)
    w,h = obrazek.size

    pix = obrazek.load()
    pixele = []
    for y in range(h):
        for x in range(w):
            r, g, b = pix[x, y]
            r, g, b = bin(r),bin(g),bin(b)
            r, g, b = r[2:], g[2:], b[2:]
            pixele.append([r, g, b])
    #print(pixele)
    return pixele

def umieszczanie(wiadomosc, pixele):
    tab_bitow = []
    for i in wiadomosc:
        znak = i
        #print(znak)
        wartosc_bitowa = format(ord(znak), '08b')
        #print(wartosc_bitowa)
        tab_bitow.append(wartosc_bitowa)
    s = ""
    s = ''.join(tab_bitow)
    dlugosc_wiadomosci = len(s)
    ilosc_potrzebnych_pix = math.ceil(len(s) / 3)
    #print(dlugosc_wiadomosci)
    #print(ilosc_potrzebnych_pix)
    #print(tab_bitow)

    for i in range(ilosc_potrzebnych_pix):
        for j in range(len(pixele[i])):
            #print(pixele[i][j][-1])
            #print("s[0]", s[0])
            if s:
                if pixele[i][j][-1] == s[0]:
                    s = s[1:]
                    continue
                else:
                    pixele[i][j] = pixele[i][j][:-1] + s[0]
                    s = s[1:]

    return pixele, dlugosc_wiadomosci

def odczytywanie_danych_zobrazka(pixele, wiadomosc_len):

    last_bits = []
    for i in range(len(pixele)):
        for j in range(len(pixele[i])):
            last_bits.append(pixele[i][j][-1])

    zakodowana_wiadomosc = last_bits[:wiadomosc_len]
    podzieloe = []
    for i in range(0, len(zakodowana_wiadomosc), 8):
        podzieloe.append(zakodowana_wiadomosc[i:i+8])
    #print(podzieloe)
    odkodowane_znaki = []
    for i in podzieloe:
        bity = ''.join(i)
        #print(bity)
        x = int(bity,2)
        #print(x)
        odkodowane_znaki.append(x)
    return odkodowane_znaki









if __name__ == "__main__":
    wiadomosc = "ZTo jest moja tajna wiadomosc"
    print(wiadomosc)

    
    pixele = pobranie_px("images.jpg")

    new_pixele, dl = umieszczanie(wiadomosc, pixele)

    #print(f"Nowe pixele do obrazka", new_pixele)

    odkodowana_wiad = odczytywanie_danych_zobrazka(new_pixele, dl)
    

    print(odkodowana_wiad)

    for i in odkodowana_wiad:
        print(chr(i))

    