from PIL import Image
import random

image = Image.open('Mapa_MD_no_terrain_low_res_dark_Gray.bmp')
width, height = image.size
T = []
frames = []

for i in range(width):
    row = []
    for j in range(height):
        row.append(image.getpixel((i, j)))
    T.append(row)

threshold = 90
for i in range(width):
    for j in range(height):
        if T[i][j] > threshold:
            T[i][j] = 1
        else:
            T[i][j] = 0

for x in range(width):
    for y in range(height):
        image.putpixel((x, y), T[x][y] * 255)
frames.append(image)


# mam stan poczatkowy w T
# 0 - rzeka
# 1 - brak drzewa
# 2 - drzewo
# 3 - drzewo płonące

def checkNeighbours(x, y):
    # okreslenie sasiadow
    ax = x - 1
    bx = x + 1
    ay = y - 1
    by = y + 1
    if x == 0:
        ax = width - 1
    if x == width - 1:
        bx = 0
    if y == 0:
        ay = height - 1
    if y == height - 1:
        by = 0
    neighbour_states = [0, 0, 0, 0]

    if T[x][y] == 3:
        return 1

    # sprawdzenie stanu sasiadow
    neighbour_states[T[ax][ay]] += 1
    neighbour_states[T[x][ay]] += 1
    neighbour_states[T[bx][ay]] += 1

    neighbour_states[T[ax][y]] += 1
    neighbour_states[T[x][y]] += 1
    neighbour_states[T[bx][y]] += 1

    neighbour_states[T[ax][by]] += 1
    neighbour_states[T[x][by]] += 1
    neighbour_states[T[bx][by]] += 1

    # reguly przejscia

    if T[x][y] == 1:
        if neighbour_states[0] + neighbour_states[2] - neighbour_states[3] > 0:
            if random.randint(0, neighbour_states[0] + neighbour_states[2] - neighbour_states[3]) >= 2:
                return 2
        else:
            if random.randint(0, 1000) > 999:
                return 2
    if T[x][y] == 2:
        if neighbour_states[3] > neighbour_states[0]:
            if random.randint(0, neighbour_states[3] - neighbour_states[0]) >= 1:
                return 3
        else:
            if random.randint(0, 10000) > 9999:
                return 3
    return T[x][y]

# stany w kolejnych krokach
for k in range(500):
    automat_temp = []
    image_temp = Image.new('RGB', (600, 330), (0, 0, 0))
    for i in range(width):
        row = []
        for j in range(height):
            x = checkNeighbours(i, j)
            row.append(x)
            if x == 0:
                image_temp.putpixel((i, j), (0, 0, 0))
            elif x == 2:
                image_temp.putpixel((i, j), (0, 255, 0))
            elif x == 3:
                image_temp.putpixel((i, j), (255, 0, 0))
            elif x == 1:
                image_temp.putpixel((i, j), (255, 255, 255))
        automat_temp.append(row)
    T = automat_temp
    frames.append(image_temp)
    print(k)
frames[0].save('forest_fire.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)