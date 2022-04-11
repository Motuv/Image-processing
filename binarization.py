#binaryzacja
threshold = 254
for i in range(T[0].__len__()):
    for j in range(T.__len__()):
        T[j][i]= int(T[j][i])
        if T[j][i]>threshold:
            T[j][i]=255
        else:
            T[j][i]=0

for x in range(width):
    for y in range(height):
        image.putpixel((x, y), T[y][x])

image.show()


#sciemnianie

lighten = 50

for i in range(T[0].__len__()):
    for j in range(T.__len__()):
        T[j][i]= int(T[j][i])
        if T[j][i]>=(255-lighten):
            T[j][i]=255
        elif T[j][i]<=-lighten:
            T[j][i] = 0
        else:
            T[j][i]+=lighten

image = Image.open('Mapa_MD_no_terrain_low_res_dark_Gray.bmp')

width, height = image.size

for x in range(width):
    for y in range(height):
        image.putpixel((x, y), T[y][x])

image.show()