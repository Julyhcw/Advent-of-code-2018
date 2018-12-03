data = open('day2.txt',encoding='utf-8',mode='r')

double = 0
tribe = 0


for line in data.readlines():
    length = len(line)
    line = line.strip()
    list = []
    list_new = []
    for i in line:

        list.append(i)
        if i not in list:
            list_new.append(i)
    d = {}

    for i in list:
        d[i] = list.count(i)
    c = d.values()
    if 2 in c:
        double += 1
    if 3 in c:
        tribe += 1


    '''
    for i in c:
        if i == 2:
            double += 1
            
        elif i == 3:
            tribe += 1
        else:
            continue
    '''
print(double, tribe, double*tribe)