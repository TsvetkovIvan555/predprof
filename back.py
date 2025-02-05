from flask import Flask
import random, os

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
    file.close()
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
    file.close()
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
        file.close()
        if login == login1:
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
    for i in diff:
        for j in index:
            for ind in tasks_ind[i][j]:
                name = "sources/tasks/task_" + str(ind) + ".txt"
                file = open(name, mode="r", encoding="UTF-8")
                task_number = int(file.readline().replace("\n", ""))
                task_diff = int(file.readline().replace("\n", ""))
                task_text = file.readline()
                task_ans = file.readline()
                task_index = ind
                file.close()

                gen_n += 1
                a = [task_number, task_index, task_text, task_ans]
                gen_tasks.append(a)
    ans = [gen_n, gen_tasks]
    return ans

def generate_random_questions_for_test(tasks_cnt):
    random_questions = []
    for i in range(0, 27):
        j = random.randint(0, 2)
        gen_text_file = "sources/tasks/"
        z = random.randint(0, tasks_cnt[i][j-1]-1)
        if i <= 9:
            gen_text_file += "task_0" + str(i)
        else:
            gen_text_file += "task_" + str(i)
        gen_text_file += str(j)
        gen_text_file += (6 - len(str(z)))*"0" + str(z) + ".txt"
        f = open(gen_text_file, 'r')
        random_questions.append({'text': str(i+1) + ". " + f.readline().rstrip(), 'correct_answer': f.readline().rstrip()})
        f.close()
    return random_questions

def get_results_for_test(data, random_questions):
    is_found = 1
    results = []
    if data.get('specific-test-id'):
        test_id = data.get('specific-test-id')
        if os.path.isfile("sources/tests/test_" + "0" * (9 - len(str(test_id))) + str(test_id) + ".txt"):
            f = open("sources/tests/test_" + "0" * (9 - len(str(test_id))) + str(test_id) + ".txt", 'r')
            i = 0
            random_questions = []
            for line in f:
                task_id = line.rstrip()
                f_task = open("sources/tasks/task_" + task_id + ".txt", 'r')
                random_questions.append({'text': str(i + 1) + ". " + f_task.readline().rstrip(),
                                         'correct_answer': f_task.readline().rstrip()})
                i += 1
                f_task.close()
            f.close()
            is_found = 1
        else:
            is_found = -1
    else:
        user_answers = []
        i = 0
        while data.get('answer' + str(i)) != None:
            user_answers.append(data.get('answer' + str(i)).lower())
            i += 1

        correct_answers = [q['correct_answer'] for q in random_questions]

        results.clear()

        for user_answer, correct_answer in zip(user_answers, correct_answers):
            result = {
                'user_answer': str(user_answer),
                'correct_answer': str(correct_answer),
                'is_correct': str(user_answer) == str(correct_answer)
            }
            results.append(result)
    return [results, is_found]

diff = {"Легко" : "1", "Средне" : "2", "Сложно" : "3"}

def make_new_task(data):
    name = "sources/tasks/task_" + str(data["index"]) + ".txt"
    file = open(name, mode="w", encoding="UTF-8")
    file.write(data["index"] + "\n")
    file.write(data["number"] + "\n")
    file.write(diff[data["difficulty"]] + "\n")
    file.write(data["text"] + "\n")
    file.write(data["answer"] + "\n")
    file.close()
    return [int(diff[data["difficulty"]]) - 1, int(data["number"]) - 1, int(data["index"])]

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

