from flask import Flask

app = Flask(__name__)

def make_cnt(ind):
    if ind < 10:
        return "00" + str(ind)
    elif ind < 100:
        return "0" + str(ind)
    else:
        return str(ind)

def make_users_id(ind):
    name = "sources/users/user_"
    name += make_cnt(ind)
    name += ".txt"
    return name

def get_users_status(ind):
    if ind == -1:
        return 1
    name = make_users_id(ind)
    file = open(name, mode="r", encoding="UTF-8")
    status = int(file.readline())
    return status

def push_new_user(data, ind):
    name = make_users_id(ind)
    file = open(name, mode="w", encoding="UTF-8")
    file.write("2\n")
    file.write(data["name"] + "\n")
    file.write(data["login"] + "\n")
    file.write(data["email"] + "\n")
    file.write(data["password"] + "\n")
    file.write("0\n0\n")
    file.write(data["nick"] + "\n")

def find_user(data, cnt_users):
    login = data["login"]
    password = data["password"]
    for i in range(1, cnt_users + 1):
        name = make_users_id(i)
        file = open(name, mode="r", encoding="UTF-8")
        stutus = file.readline()
        name = file.readline()
        login1 = file.readline().replace("\n", "")
        email = file.readline()
        password1 = file.readline().replace("\n", "")

        if login == login1:
            if password == password1:
                return i
            else:
                return -1
    return -2

def users_data(ind):
    name = make_users_id(ind)
    file = open(name, mode="r", encoding="UTF-8")
    status = file.readline().replace("\n", "")
    name = file.readline().replace("\n", "")
    login = file.readline().replace("\n", "")
    email = file.readline().replace("\n", "")
    password = file.readline().replace("\n", "")
    solved = file.readline().replace("\n", "")
    unsolved = file.readline().replace("\n", "")
    nick = file.readline().replace("\n", "")
    return {
        'full_name': name,
        'login': login,
        'email': email,
        'solved_tasks': solved,
        'nick': nick,
        'groups': ['Группа 1', 'Группа 2', 'Группа 3']
    }

def users_data(ind):
    name = make_users_id(ind)
    file = open(name, mode="r", encoding="UTF-8")
    status = file.readline().replace("\n", "")
    name = file.readline().replace("\n", "")
    login = file.readline().replace("\n", "")
    email = file.readline().replace("\n", "")
    password = file.readline().replace("\n", "")
    solved = file.readline().replace("\n", "")
    unsolved = file.readline().replace("\n", "")
    nick = file.readline().replace("\n", "")
    return {
        'full_name': name,
        'login': login,
        'email': email,
        'solved': solved,
        'unsolved' : unsolved,
        'nick': nick,
        'groups': ['Группа 1', 'Группа 2', 'Группа 3']
    }

def check(data, cnt_users):
    login = data["login"]
    for i in range(1, cnt_users + 1):
        name = make_users_id(i)
        file = open(name, mode="r", encoding="UTF-8")
        stutus = file.readline()
        name = file.readline()
        login1 = file.readline().replace("\n", "")
        if login == login1:
            return False
    return True

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

