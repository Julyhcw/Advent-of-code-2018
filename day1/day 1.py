data = open('day1_0.txt',encoding='utf-8')
state = 0
list = []
fn = data
while True:
    for line in fn.readlines():
        line = int(line)
        state += line
        if state in list:
            print('twice = ', state)
            exit()
        list.append(state)
    fn = open('day1_0.txt', encoding='utf-8')
