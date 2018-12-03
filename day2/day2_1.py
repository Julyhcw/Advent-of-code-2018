import difflib
list = []
list_fina = []
state = 0
num_i = 0
num_j = 0
data = open('day2_0.txt',encoding='utf-8',mode='r')
for line in data.readlines():
    line = line.strip()
    list.append(line)
    #print(list)
n = len(list)
print(n)
for i in range(n-1):
    for j in range(i+1,n):
        seq = difflib.SequenceMatcher(None,list[i],list[j])
        ratio = seq.ratio()
        if ratio > state:
            state = ratio
            num_i = i
            num_j = j
        else:
            continue
print('num_i = {}, num_j = {}'.format(num_i, num_j))
list_i = list[num_i]
list_j = list[num_j]
print(list_i)
print(list_j)
for n in range(len(list[num_i])):
    if list_i[n] == list_j[n]:
        list_fina.append(list_i[n])
    else:
        continue
print(list_fina)
















