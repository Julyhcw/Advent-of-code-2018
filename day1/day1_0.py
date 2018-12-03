state = 0
list = []
with open('day1_0.txt',encoding='utf-8') as fn:
    for line in fn.readlines():
        line = int(line)
        state += line
    print('result = ', state)

