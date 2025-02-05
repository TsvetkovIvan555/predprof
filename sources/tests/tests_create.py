import random

def make_number(ind):
    if ind < 10:
        return "0000" + str(ind)
    elif ind < 100:
        return "000" + str(ind)
    else:
        return "00" + str(ind)

for i in range(20):
    name = "test_" + make_number(i) + ".txt"
    f = open(name, 'w', encoding='utf-8')
    f.write(str(random.randint(1, 1000)))
    f.close()