from flask import Flask
import random, os

app = Flask(__name__)

def find_cnt_of_tests():
    tests_cnt = 1
    while os.path.isfile("sources/tests/test_" + "0" * (5 - len(str(tests_cnt))) + str(tests_cnt) + ".txt"):
        tests_cnt += 1
    return tests_cnt - 1

def find_cnt_of_users():
    users_cnt = 1
    while os.path.isfile("sources/users/main_data/user_" + "0" * (3 - len(str(users_cnt))) + str(users_cnt) + ".txt"):
        users_cnt += 1
    return users_cnt - 1

def find_cnt_of_groups():
    tests_cnt = 1
    while os.path.isfile("sources/groups/lectures/group_" + "0" * (5 - len(str(tests_cnt))) + str(tests_cnt) + ".txt"):
        tests_cnt += 1
    return tests_cnt - 1

def make_cnt(ind):
    if ind < 10:
        return "00" + str(ind)
    elif ind < 100:
        return "0" + str(ind)
    else:
        return str(ind)

def make_users_id(ind):
    name = "sources/users/main_data/user_"
    name += make_cnt(ind)
    name += ".txt"
    return name

def get_users_status(ind):
    if ind == -1:
        return 1
    name = make_users_id(ind)
    file = open(name, mode="r", encoding="UTF-8")
    status = int(file.readline())
    file.close()
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
    file.close()

    name = "sources/users/groups/user_" + make_cnt(ind) + ".txt"
    file = open(name, mode="w", encoding="UTF-8")
    file.close()

def change_users_data(data, ind):
    name = make_users_id(ind)
    file = open(name, mode="w", encoding="UTF-8")
    file.close()
    file = open(name, mode="w", encoding="UTF-8")
    file.write("2\n")
    file.write(data["name"] + "\n")
    file.write(data["login"] + "\n")
    file.write(data["email"] + "\n")
    file.write(data["password"] + "\n")
    file.write("0\n0\n")
    file.write(data["nick"] + "\n")
    file.close()

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
        file.close()
        if login == login1:
            if password == password1:
                return i
            else:
                return -1
    return -2

def make_users_groups(ind):
    name = "sources/users/groups/user_" + make_cnt(ind) + ".txt"
    ans = []
    with open(name) as file:
        for index_of_group in file:
            index_of_group = index_of_group.replace("\n", "")
            name_of_group = "sources/groups/main_information/group_" + "0" * (5 - len(str(index_of_group))) + str(index_of_group) + ".txt"
            file1 = open(name_of_group, mode='r', encoding='UTF-8')
            name1 = file1.readline()
            description = file1.readline()
            id_of_owner = file1.readline()
            file1.close()
            ans.append([name1, "/group" + str(index_of_group) + "_" + str(id_of_owner)])
    return ans

def users_data(ind):
    name1 = make_users_id(ind)
    file = open(name1, mode="r", encoding="UTF-8")
    status = file.readline().replace("\n", "")
    name = file.readline().replace("\n", "")
    login = file.readline().replace("\n", "")
    email = file.readline().replace("\n", "")
    password = file.readline().replace("\n", "")
    solved = file.readline().replace("\n", "")
    unsolved = file.readline().replace("\n", "")
    nick = file.readline().replace("\n", "")
    file.close()
    return {
        'status' : status,
        'password' : password,
        'full_name': name,
        'login': login,
        'email': email,
        'solved': solved,
        'unsolved' : unsolved,
        'nick': nick,
        'groups': make_users_groups(ind)
    }

def check(data, cnt_users):
    login = data["login"]
    for i in range(1, cnt_users + 1):
        name = make_users_id(i)
        file = open(name, mode="r", encoding="UTF-8")
        stutus = file.readline()
        name = file.readline()
        login1 = file.readline().replace("\n", "")
        file.close()
        if login == login1:
            return False
    return True

def check1(data, cnt_users, id):
    login = data["login"]
    for i in range(1, cnt_users + 1):
        name = make_users_id(i)
        file = open(name, mode="r", encoding="UTF-8")
        stutus = file.readline()
        name = file.readline()
        login1 = file.readline().replace("\n", "")
        file.close()
        if login == login1 and i != id:
            return False
    return True


def generate_task(data, tasks_ind):
    gen_tasks = []
    index = []
    for i in range(1, 28):
        if data.get("type" + str(i)):
            index.append(i - 1)
    diff = []
    for i in range(1, 4):
        if data.get("dif" + str(i)):
            diff.append(i - 1)
    gen_n = 0

    try:
        ind = int(data["token"])
        gen_n = 1
        name = "sources/tasks/task_" + str(ind) + ".txt"
        file = open(name, mode="r", encoding="UTF-8")
        task_number = int(file.readline().replace("\n", ""))
        task_diff = int(file.readline().replace("\n", ""))
        task_text = file.readline()
        task_additional = file.readline().rstrip()
        task_ans = file.readline()
        task_index = ind
        file.close()

        try:
            if task_additional[len(task_additional) - 1] == 't':
                task_type = "txt"
                task_additional = "sources/tasks/" + task_additional
            if task_additional[len(task_additional) - 1] == 'g':
                task_type = "pic"
                task_additional = "images/" + task_additional
            if task_additional[len(task_additional) - 2] == 's':
                task_type = "table"
                task_additional = "sources/tasks/" + task_additional
            if task_additional[len(task_additional) - 2] == 'c':
                task_type = "doc"
                task_additional = "sources/tasks/" + task_additional
        except:
            task_type = "none"

        a = [task_number, task_index, task_text, task_ans, task_additional, task_type]
        gen_tasks.append(a)
        ans = [gen_n, gen_tasks]
        return ans
    except:
        for i in diff:
            for j in index:
                for ind in tasks_ind[i][j]:
                    name = "sources/tasks/task_" + str(ind) + ".txt"
                    file = open(name, mode="r", encoding="UTF-8")
                    task_number = int(file.readline().replace("\n", ""))
                    task_diff = int(file.readline().replace("\n", ""))
                    task_text = file.readline()
                    task_additional = file.readline().rstrip()
                    task_ans = file.readline()
                    task_index = ind
                    file.close()

                    gen_n += 1

                    try:
                        if task_additional[len(task_additional) - 1] == 't':
                            task_type = "txt"
                            task_additional = "sources/tasks/" + task_additional
                        if task_additional[len(task_additional) - 1] == 'g':
                            task_type = "pic"
                            task_additional = "images/" + task_additional
                        if task_additional[len(task_additional) - 2] == 's':
                            task_type = "table"
                            task_additional = "sources/tasks/" + task_additional
                        if task_additional[len(task_additional) - 2] == 'c':
                            task_type = "doc"
                            task_additional = "sources/tasks/" + task_additional
                    except:
                        task_type = "none"

                    a = [task_number, task_index, task_text, task_ans, task_additional, task_type]
                    gen_tasks.append(a)
        ans = [gen_n, gen_tasks]
        return ans

def generate_random_questions_for_test(tasks_ind):
    random_questions = []
    for i in range(0, 26):
        j = random.randint(0, 2)
        if len(tasks_ind[j][i]) != 0:
            z = random.randint(0, len(tasks_ind[j][i])-1)
            d = unpack_task(tasks_ind[j][i][z])
            task_additional = d['additional']
            try:
                if task_additional[len(task_additional)-1] == 't' :
                    task_type = "txt"
                    task_additional = "sources/tasks/" + task_additional
                if task_additional[len(task_additional)-1] == 'g' :
                    task_type = "pic"
                    task_additional = "images/" + task_additional
                if task_additional[len(task_additional)-2] == 's' :
                    task_type = "table"
                    task_additional = "sources/tasks/" + task_additional
                if task_additional[len(task_additional)-2] == 'c' :
                    task_type = "doc"
                    task_additional = "sources/tasks/" + task_additional
            except:
                task_type = "none"
            random_questions.append({'text': d['problem'].rstrip(), 'correct_answer': d['answer'].rstrip(), 'additional': task_additional, 'type': task_type})
    return random_questions


def unpack_task(id):
    name = "sources/tasks/task_" + str(id) + ".txt"
    f = open(name, mode="r", encoding="UTF-8")
    result = dict()
    result['kim'] = f.readline().rstrip()
    result['dif'] = f.readline().rstrip()
    result['problem'] = f.readline().rstrip()
    result['additional'] = f.readline().rstrip()
    result['answer'] = f.readline().rstrip()
    f.close()
    return result


def generate_specific_test(test_id):
    name = "sources/tests/test_" + str(test_id) + ".txt"
    f = open(name, mode="r", encoding="UTF-8")
    task_id = f.readline().rstrip()
    questions = []
    while task_id:
        d = unpack_task(task_id)
        task_additional = d['additional']
        try:
            if task_additional[len(task_additional)-1] == 't' :
                task_type = "txt"
                task_additional = "sources/tasks/" + task_additional
            if task_additional[len(task_additional)-1] == 'g' :
                task_type = "pic"
                task_additional = "images/" + task_additional
            if task_additional[len(task_additional)-2] == 's' :
                task_type = "table"
                task_additional = "sources/tasks/" + task_additional
            if task_additional[len(task_additional)-2] == 'c' :
                task_type = "doc"
                task_additional = "sources/tasks/" + task_additional
        except:
            task_type = "none"
        questions.append({'text': d['problem'].rstrip(), 'correct_answer': d['answer'].rstrip(), 'additional': task_additional, 'type': task_type})
        task_id = f.readline().rstrip()
    f.close()
    return questions


def check_test(data):
    user_answers = []
    correct_answers = []
    i = 0

    while data.get('answer' + str(i)) != None:
        user_answers.append(data.get('answer' + str(i)))
        correct_answers.append(data.get('correct_answer' + str(i)))
        i += 1

    results = []

    for user_answer, correct_answer in zip(user_answers, correct_answers):
        result = {
            'user_answer': str(user_answer),
            'correct_answer': str(correct_answer),
            'is_correct': str(user_answer) == str(correct_answer)
        }
        results.append(result)

    return results

diff = {"Легко" : "1", "Средне" : "2", "Сложно" : "3"}

def make_new_task(data, index):
    name = "sources/tasks/task_" + str(index) + ".txt"
    file = open(name, mode="w", encoding="UTF-8")
    file.write(data["number"] + "\n")
    file.write(diff[data["difficulty"]] + "\n")
    file.write(data["text"] + "\n")
    file.write(data["answer"] + "\n")
    file.close()
    return [int(diff[data["difficulty"]]) - 1, int(data["number"]) - 1, int(index)]

def generate_random_token(length):
    token = random.randint(10 ** length, 10 ** (length + 1))
    return token


def make_tasks_id():
    task = [[[] for _ in range(27)] for _ in range(3)]
    folder_path = "sources/tasks"
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file = os.path.join(root, file_name)

            if file[file.find(".") + 1:] == "txt" and file.find("_") == file.rfind("_"):
                f = open(file, 'r', encoding='utf-8')
                a = file.find("_") + 1
                b = file.find(".")
                id = file[a:b]
                type = f.readline().replace("\n", "")
                diff = f.readline().replace("\n", "")
                f.close()
                task[int(diff) - 1][int(type) - 1].append(id)
    return task

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

