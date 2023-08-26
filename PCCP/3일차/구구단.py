from pprint import pprint
gugudan = []
for i in range(2, 10):
    temp = []
    for j in range(1, 10):
        temp.append(j*i)
    gugudan.append(temp)

pprint(gugudan)

gugudan2 = [[i*j for i in range(1, 10)] for j in range(2, 10)]

pprint(gugudan2)
