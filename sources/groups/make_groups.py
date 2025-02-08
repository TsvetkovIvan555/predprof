for i in range(1, 10):
    name = "lectures/group_0000" + str(i) + ".txt"
    file = open(name, 'w', encoding='utf-8')
    file.close()
    name = "main_information/group_0000" + str(i) + ".txt"
    file = open(name, 'w', encoding='utf-8')
    file.close()
    name = "test/group_0000" + str(i) + ".txt"
    file = open(name, 'w', encoding='utf-8')
    file.close()
    name = "users/group_0000" + str(i) + ".txt"
    file = open(name, 'w', encoding='utf-8')
    file.close()

