from PIL import Image
import matplotlib.pyplot as plt

image = Image.open('Mapa_MD_no_terrain_low_res_dark_Gray.bmp')

width, height = image.size
f = open("mapa.txt", "r")
T = []
colors = []

for line in f:
    x = line.split()
    T.insert(T.__len__(),x)

#binaryzacja
threshold = 220
for i in range(T[0].__len__()):
    for j in range(T.__len__()):
        T[j][i]= int(T[j][i])
        if T[j][i]>threshold:
            T[j][i]=255
        else:
            T[j][i]=0



T3 = [[255 for x in range(600)] for i in range(330)]

#erozja
for i in range(1, width-1):
    for j in range(1, height-1):
        if T[j-1][i-1] == 0 or T[j][i-1] == 0 or T[j+1][i-1] == 0 or T[j-1][i] == 0 or T[j][i] == 0 or T[j+1][i] == 0 or T[j-1][i+1] == 0 or T[j][i+1] == 0 or T[j+1][i+1] == 0:
            T3[j][i]=0

for x in range(width):
    for y in range(height):
        image.putpixel((x, y), T3[y][x])

image.show()

T2 = [[0 for x in range(600)] for i in range(330)]

#dylatacja
for i in range(1, width-1):
    for j in range(1, height-1):
        if T3[j-1][i-1] == 255 or T3[j][i-1] == 255 or T3[j+1][i-1] == 255 or T3[j-1][i] == 255 or T3[j][i] == 255 or T3[j+1][i] == 255 or T3[j-1][i+1] == 255 or T3[j][i+1] == 255 or T3[j+1][i+1] == 255:
            T2[j][i]=255

for x in range(width):
    for y in range(height):
        image.putpixel((x, y), T2[y][x])

image.show()

