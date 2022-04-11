import random
from PIL import Image
size_x = 10
size_y = 10
next_step = 'y'

image = Image.new('1', (size_x, size_y))

row = []
automat = []

glider = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,0,0,0,0],
          [0,0,0,0,0,1,1,0,0,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

oscillator = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]

constans = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,1,0,0,0,0,0],
          [0,0,1,0,0,1,0,0,0,0],
          [0,0,0,1,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]
#Enter your patter
own_pattern = [[1,0,0,0,0,0,0,0,0,1],
               [0,1,0,0,0,0,0,0,1,0],
               [0,0,1,0,0,0,0,1,0,0],
               [0,0,0,1,0,0,1,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,0,0],
               [0,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,0,0,1,0,0],
               [0,1,0,0,0,0,0,0,1,0],
               [1,0,0,0,0,0,0,0,0,1]]

#random pattern
for i in range(size_y):
    row = []
    for j in range(size_x):
        row.append(random.randint(0, 1))
    automat.append(row)

#automat=own_pattern

def checkNeighbours(x, y):
    neighbours = 0
    ax = x - 1
    bx = x + 1
    ay = y - 1
    by = y + 1
    if x == 0:
        ax = size_x - 1
    if x == size_x - 1:
        bx = 0
    if y == 0:
        ay = size_y - 1
    if y == size_y - 1:
        by = 0
    neighbours += automat[ax][ay]
    neighbours += automat[x][ay]
    neighbours += automat[bx][ay]
    neighbours += automat[ax][y]
    neighbours += automat[bx][y]
    neighbours += automat[ax][by]
    neighbours += automat[x][by]
    neighbours += automat[bx][by]
    if automat[x][y] == 0 and neighbours == 3:
        return 1
    if automat[x][y] == 1 and (neighbours > 3 or neighbours < 2):
        return 0
    else:
        return automat[x][y]


while 1 == 1:
    next_step = input("Czy wygenerować kolejny krok? y/n")
    if next_step == 'y':
        automat_temp = []
        for i in range(size_y):
            row = []
            for j in range(size_x):
                row.append(checkNeighbours(i, j))
                #image.putpixel((i,j),checkNeighbours(i, j))
            automat_temp.append(row)
            for item in row:
                print(item, end="")
            print()
        automat=automat_temp
        #image.show()
    else:
        exit(0)
