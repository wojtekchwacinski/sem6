from PIL import Image
import random
def osadzanie(plik, seed, licz_nat, d):

    obrazek = Image.open(plik)
    obrazek = obrazek.copy()
    random.seed(seed)
    obrazek = obrazek.convert('RGB')
    new_pixels = []
    pixele = obrazek.load()

    suma = 0
    ss = 0
    for i in range(1, licz_nat):
        x_1 = random.randint(0, obrazek.width-1)
        y_1 = random.randint(0, obrazek.height-1)
        #print(x_1, y_1)

        x_2 = random.randint(0, obrazek.width-1)
        y_2 = random.randint(0, obrazek.height-1)

        r_1, g_1, b_1 = pixele[x_1, y_1]
        s1_1 = (r_1 + g_1 + b_1)/3

        r_1 = min(255, int(r_1 + d))
        g_1 = min(255, int(g_1 + d))
        b_1 = min(255, int(b_1 + d))
        pixele[x_1, y_1] = (r_1, g_1, b_1)
        s1 = (r_1 + g_1 + b_1)/3


        r_2, g_2, b_2 = pixele[x_2, y_2]
        s2_2 = (r_2 + g_2 + b_2)/3 

        r_2 = max(int(r_2 - d), 0)
        g_2 = max(int(g_2 - d), 0)
        b_2 = max(int(b_2 - d), 0)
        pixele[x_2, y_2] = (r_2, g_2, b_2)
        s2 = (r_2 + g_2 + b_2)/3 

        suma += (s1-s2)
        ss += (s1_1-s2_2)

    s_n =  suma

    return obrazek, s_n, ss

def detekcja_znaku(obraz, seed, licz_nat, d):
    obrazek = obraz
    obrazek = obrazek.copy()
    random.seed(seed)
    
    new_pixels = []
    pixele = obrazek.load()
    suma = 0
    ss = 0
    for i in range(1, licz_nat):
        x_1 = random.randint(0, obrazek.width-1)
        y_1 = random.randint(0, obrazek.height-1)
        #print(x_1, y_1)
        x_2 = random.randint(0, obrazek.width-1)
        y_2 = random.randint(0, obrazek.height-1)

        r_1, g_1, b_1 = pixele[x_1, y_1]
        s1_1 = (r_1 + g_1 + b_1)/3

        r_1 = max(int(r_1 - d), 0)
        g_1 = max(int(g_1 - d), 0)
        b_1 = max(int(b_1 - d), 0)
        pixele[x_1, y_1] = (r_1, g_1, b_1)
        s1 = (r_1 + g_1 + b_1)/3


        r_2, g_2, b_2 = pixele[x_2, y_2]
        s2_2 = (r_2 + g_2 + b_2)/3 

        r_2 = min(255, int(r_2 + d))
        g_2 = min(255, int(g_2 + d))
        b_2 = min(255, int(b_2 + d))
        pixele[x_2, y_2] = (r_2, g_2, b_2)
        s2 = (r_2 + g_2 + b_2)/3 
        suma += (s1-s2)
        ss += (s1_1-s2_2)
    s_n =  suma

    return obrazek, s_n, ss



if __name__ == "__main__":
    seed_generatora = 444
    
    licz_nat = 5000
    d = 44


    nowy_obrazek, s_n, sn = osadzanie("jhin_four.jpg", seed_generatora, licz_nat, d)
    print(f"Sn: {sn}, a sprimn: {s_n}")
    nowy_obrazek.save("fouuuur.jpg")

    dekodowany, s_n2, ss = detekcja_znaku(nowy_obrazek, seed_generatora, licz_nat, d)

    dekodowany.save("zdekodowany.jpg")
    print(f"sprimn: {s_n2}, {ss}")