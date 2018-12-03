import numpy as np

data = open('day3.txt',encoding='utf-8',mode='r')
fabric = np.zeros((1000,1000))
loop = 0
list = []

for line in data.readlines():
    #loop += 1
    #print('ID = ',loop)
    line = line.replace(':','')
    line = line.strip().split()
    start_i, start_j = line[2].split(',')
    num_i, num_j = line[3].split('x')
    start_i, start_j, num_i, num_j = int(start_i), int(start_j), int(num_i), int(num_j)
    list.append((start_i, start_j, num_i, num_j))

    for i in range(start_i, start_i+num_i):
        for j in range(start_j, start_j+num_j):
            #print(i, j)
            fabric[i][j] += 1

#print(list[0])
for i in range(1353):
    loop += 1
    state = 0
    print('ID = ',loop)
    start_i, start_j, num_i, num_j = list[i]
    #print(list[i])

    for i in range(start_i, start_i+num_i):
        for j in range(start_j, start_j+num_j):
            state += fabric[i][j]
            #print(state)
    if state == num_i*num_j:
        print('This is the ID',loop)
        break
    else:
        continue










