import random

def make_number(ind):
    if ind < 10:
        return "00" + str(ind)
    elif ind < 100:
        return "0" + str(ind)
    else:
        return str(ind)

for i in range(1000):
    name = "task_" + make_number(i) + ".txt"
    f = open(name, 'w', encoding='utf-8')
    a, b, c = random.randint(100000000000, 1000000000000), random.randint(1, 28), random.randint(1, 4)
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(c) + "\n")
    f.write("Страшный текст очень сложной задачи\n")
    f.write("Страшный ответ\n")
    f.close()