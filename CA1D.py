import random
#poniższe zmienne można ustawiać osobno dla każdej symulacji
rule = 225
bin_rule = []
boundary = 2 #1. jedynki na brzegach, 2. periodyczne warunki
size = 10
steps = 10

for i in range(8):
    bin_rule.append(rule % 2)
    rule = int(rule / 2)

table = []
temp = []

for i in range(size):
    temp.append(random.randint(0, 1))
table.append(temp)

def transition(left, center, right):
    bin = "0b" + str(left) + str(center) + str(right)
    dec = int(bin, 2)
    return bin_rule[dec]


for i in range(steps):
    temp = []
    for j in range(size):
        if j == 0:
            if boundary == 2:
                temp.append(transition(table[i][size-1], table[i][j], table[i][j + 1]))
            else:
                temp.append(transition(1, table[i][j], table[i][j + 1]))
        elif j == size-1:
            if boundary == 2:
                temp.append(transition(table[i][j - 1], table[i][j], table[i][0]))
            else:
                temp.append(transition(table[i][j - 1], table[i][j], 1))
        else:
            if boundary == 2:
                temp.append(transition(table[i][j - 1], table[i][j], table[i][j + 1]))
            else:
                temp.append(transition(table[i][j - 1], table[i][j], table[i][j + 1]))
    table.append(temp)
    print(table[i])