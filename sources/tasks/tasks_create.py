import random

def make_number(ind):
    if ind < 10:
        return "00" + str(ind)
    elif ind < 100:
        return "0" + str(ind)
    else:
        return str(ind)

index = []
for i in range(3):
    p = []
    for j in range(27):
        p.append([])
    index.append(p)

for i in range(20):
    a, b, c = random.randint(1000000000, 10000000000), random.randint(1, 27), random.randint(1, 3)
    name = "task_" + str(a) + ".txt"
    f = open(name, 'w', encoding='utf-8')
    f.write(str(b) + "\n")
    f.write(str(c) + "\n")
    f.write("Страшный текст очень сложной задачи\n")
    f.write("Страшный ответ\n")
    index[c - 1][b - 1].append(a)
    f.close()

print(index)