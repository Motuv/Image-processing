from PIL import Image
import matplotlib.pyplot as plt

f = open("mapa.txt", "r")
T = []
colors = []

for line in f:
    x = line.split()
    T.insert(T.__len__(),x)

#    for i in T[T.__len__()-1]:
#        colors.append(int(i))

for i in range(T[0].__len__()):
    for j in range(T.__len__()):
        T[j][i] = int(T[j][i])
#threshold = 216
#for i in range(T[0].__len__()):
#    for j in range(T.__len__()):
#        T[j][i]= int(T[j][i])
#        if T[j][i]>threshold:
#            T[j][i]=255
#        else:
#            T[j][i]=0

image = Image.open('Mapa_MD_no_terrain_low_res_dark_Gray.bmp')
width, height = image.size

Lowpass=[[1,1,1],[1,1,1],[1,1,1]]
Highpass = [[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]
Gauss = [[1,4,1],[4,32,4],[1,4,1]]
imgGauss= [[0 for x in range(600)] for i in range(330)]
imgHighpass = [[0 for x in range(600)] for i in range(330)]
imgLowpass = [[0 for x in range(600)] for i in range(330)]
for i in range(1, 329):
    for j in range(1, 599):
        imgLowpass[i][j] = int((Lowpass[0][0]*T[i-1][j-1]+Lowpass[0][1]*T[i-1][j]+Lowpass[0][2]*T[i-1][j+1]+Lowpass[1][0]*T[i][j-1]+Lowpass[1][1]*T[i][j]+Lowpass[1][2]*T[i][j+1]+Lowpass[2][0]*T[i+1][j-1]+Lowpass[2][1]*T[i+1][j]+Lowpass[2][2]*T[i+1][j+1])/9)
        imgHighpass[i][j] = int((Highpass[0][0] * T[i - 1][j - 1] + Highpass[0][1] * T[i - 1][j] + Highpass[0][2] *T[i - 1][j + 1] + Highpass[1][0] * T[i][j - 1] + Highpass[1][1] * T[i][j] + Highpass[1][2] * T[i][j + 1] + Highpass[2][0] * T[i + 1][j - 1] + Highpass[2][1] * T[i + 1][j] + Highpass[2][2] * T[i + 1][j + 1]))
        imgGauss[i][j]= int((Gauss[0][0]*T[i-1][j-1]+Gauss[0][1]*T[i-1][j]+Gauss[0][2]*T[i-1][j+1]+Gauss[1][0]*T[i][j-1]+Gauss[1][1]*T[i][j]+Gauss[1][2]*T[i][j+1]+Gauss[2][0]*T[i+1][j-1]+Gauss[2][1]*T[i+1][j]+Gauss[2][2]*T[i+1][j+1])/52)
        if imgHighpass[i][j] > 255:
            imgHighpass[i][j] = 255
        if imgHighpass[i][j] < 0:
            imgHighpass[i][j] = 0
                
for x in range(width):
    for y in range(height):
        image.putpixel((x, y), imgGauss[y][x])

image.show()
#plt.hist(colors, bins = [215,216,217,218,219,220], edgecolor='black')
#plt.show()