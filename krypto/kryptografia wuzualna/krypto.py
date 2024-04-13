from PIL import Image, ImageChops
import random 

image = Image.open('obraz.png')
width, heigth = image.size
tabela_obrazu = []

for i in range(heigth):
    tabela_obrazu.append([])
    for j in range(width):

        pixel_value = image.getpixel((i, j))
        tabela_obrazu[-1].append(pixel_value)
        print(pixel_value)
    print("\n")


# udzał 1 
def create_udzial(pixele_wejsciowe):
    image1 = Image.new("RGB", (200, 100), (255, 255, 255))
    image2 = Image.new("RGB", (200, 100), (255, 255, 255))
    prawd = [True, False]

    for i in range(len(pixele_wejsciowe)):
        for j in range(len(pixele_wejsciowe)):
            if pixele_wejsciowe[i][j] == (255, 255, 255, 255):
               
                random_element = random.choice(prawd)
                if random_element:
                    image1.putpixel((i*2, j),  (255, 255, 255, 127))
                    image1.putpixel((i*2 + 1, j), (0, 0, 0, 127))

                    image2.putpixel((i*2, j), (0, 0, 0, 127))
                    image2.putpixel((i*2 + 1, j), (255, 255, 255, 127))

                else:
                    image1.putpixel((i*2, j), (0, 0, 0, 127))
                    image1.putpixel((i*2 + 1, j), (255, 255, 255, 127))
                
                    image2.putpixel((i*2, j), (255, 255, 255, 127))
                    image2.putpixel((i*2 + 1, j), (0, 0, 0, 127))
                
                    
            else:
                random_element = random.choice(prawd)
                if random_element:
                    image1.putpixel((i*2, j),  (255, 255, 255, 127))
                    image1.putpixel((i*2 + 1, j), (0, 0, 0, 127))

                    image2.putpixel((i*2, j), (255, 255, 255, 127))
                    image2.putpixel((i*2 + 1, j), (0, 0, 0, 127))

                else:
                    image1.putpixel((i*2, j), (0, 0, 0, 127))
                    image1.putpixel((i*2 + 1, j),  (255, 255, 255, 127))

                    image2.putpixel((i*2, j), (0, 0, 0, 127))
                    image2.putpixel((i*2 + 1, j), (255, 255, 255, 127))
        
    return image1, image2




pic1, pic2 = create_udzial(tabela_obrazu)

pic1.save('udzial1.png')
pic2.save('udzial2.png')


pic1 = pic1.convert("1")
pic2 = pic2.convert("1")

#nalozenie na sb obraków

pic3 = ImageChops.logical_xor(pic1, pic2)

pic3.save('odkodowany_obraz.png')