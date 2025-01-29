from flask import Flask, render_template, request
import random

app = Flask(__name__)

user = 3
tasks_cnt = [[1, 1, 1] for i in range(28)]

@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template("signup.html", user = user)
    elif request.method == "POST":
        return render_template("home_page.html", user = user)


@app.route('/')
def main_page():
    return render_template("home_page.html", user = user)


@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    global user
    if request.method == 'GET':
        return render_template("login.html", user = user)
    elif request.method == "POST":
        user = 2
        return render_template("home_page.html", user = user)


@app.route('/add_course', methods=['POST', 'GET'])
def add_course():
    if request.method == 'GET':
        return render_template("add_course.html", user = user)
    elif request.method == "POST":
        return render_template("home_page.html", user = user)

@app.route('/add_task', methods=['POST', 'GET'])
def add_task():
    if request.method == 'GET':
        return render_template("add_task.html", user = user)
    elif request.method == "POST":
        return render_template("home_page.html", user = user)

@app.route('/pers_cab')
def index():
    User = {
        'full_name': 'Иванов Иван Иванович',
        'username': 'ivanov',
        'email': 'ivanov@example.com',
        'rank': 'Студент',
        'solved_tasks': 52,
        'groups': ['Группа 1', 'Группа 2', 'Группа 3']  # Пример данных о группах
    }
    stats = {
        'math': 35,
        'phys': 15,
        'cs': 50
    }
    return render_template('pers_cab.html', User=User, user=user, stats=stats)

@app.route('/lec1')
def lec1():
    return render_template('lection_1.html', user = user)

@app.route('/lec2')
def lec2():
    return render_template('lection_2.html', user = user)

@app.route('/lec3')
def lec3():
    return render_template('lection_3.html', user = user)

@app.route('/test', methods=['GET', 'POST', 'UPDATE'])
def test():
    random_questions = []
    for i in range(0, 27):
        j = random.randint(0, 2)
        gen_text_file = "sources\\tasks\\"
        z = random.randint(0, tasks_cnt[i][j-1]-1)
        if(i <= 9):
            gen_text_file += "task_0" + str(i) + "_"
        else:
            gen_text_file += "task_" + str(i) + "_"
        gen_text_file += str(j) + "_"
        gen_text_file += (6 - len(str(z)))*"0" + str(z) + ".txt"
        f = open(gen_text_file, 'r')
        random_questions.append({'text': str(i+1) + ". " + f.readline().rstrip(), 'correct_answer': f.readline().rstrip()})
        f.close()    
    results = []
    
    if request.method == 'POST':
        user_answers = []
        for i in range(0, 27):
            user_answers.append(request.form.get('answer' + str(i), '').lower())
            
        correct_answers = [q['correct_answer'] for q in random_questions]

        results.clear()

        for user_answer, correct_answer in zip(user_answers, correct_answers):
            result = {
                'user_answer': str(user_answer),
                'correct_answer': str(correct_answer),
                'is_correct': str(user_answer) == str(correct_answer)
            }
            results.append(result)
    if request.method == 'UPDATE':
        random_questions = []
        for i in range(0, 27):
            j = random.randint(0, 2)
            gen_text_file = "sources\\tasks\\"
            z = random.randint(0, tasks_cnt[i][j-1]-1)
            if(i <= 9):
                gen_text_file += "task_0" + str(i) + "_"
            else:
                gen_text_file += "task_" + str(i) + "_"
            gen_text_file += str(j) + "_"
            gen_text_file += (6 - len(str(z)))*"0" + str(z) + ".txt"
            f = open(gen_text_file, 'r')
            random_questions.append({'text': str(i+1) + ". " + f.readline().rstrip(), 'correct_answer': f.readline().rstrip()})
            f.close()    
        results = []        
    return render_template('test.html', questions=random_questions, results=results, enumerate=enumerate, user = user)

@app.route('/task', methods=['GET', 'POST'])
def task():
    gen_n = 0
    gen_tasks = []
    if(request.method == 'POST'):
        gen_n = 0
        gen_tasks = []
        for i in range(0, 27):
            if request.form.get("type" + str(i + 1)) != None:
                for j in range(0, 3):
                    if(request.form.get("dif" + str(j + 1)) != None):
                        gen_n += tasks_cnt[i][j]
                        gen_text_file = "sources/tasks/"
                        for z in range(tasks_cnt[i][j]):
                            if(i < 9):
                                gen_text_file += "task_0" + str(i) + "_"
                            else:
                                gen_text_file += "task_" + str(i) + "_"
                            gen_text_file += str(j) + "_"
                            gen_text_file += (6 - len(str(z)))*"0" + str(z) + ".txt"
                            f = open(gen_text_file, 'r')
                            gen_tasks.append([])
                            for line in f:
                                gen_tasks[-1].append(line.rstrip())
                            f.close()
    return render_template("task.html", n = gen_n, tasks = gen_tasks, user = user)

@app.route('/sign_out')
def sign_out():
    global user
    user = 1
    return render_template("home_page.html", user = user)

@app.route('/add_group', methods=['GET', 'POST'])
def add_group():
    if request.method == 'GET':
        return render_template("add_group.html", user = user)
    else:
        tests = []
        tasks = []
        studens = []
        results = []
        overall_results = []
        overall_group_completion = 1
        tests_size = 0
        return render_template("group1.html", user = user, tests = tests, tasks = tasks, studens = studens, results = results, overall_results = overall_results, overall_group_completion = overall_group_completion, tests_size = tests_size)

@app.route('/group1')
def group1():
    tests = []
    tasks = []
    studens = []
    results = []
    overall_results = []
    overall_group_completion = 1
    tests_size = 0
    return render_template("group1.html", user = user, tests = tests, tasks = tasks, studens = studens, results = results, overall_results = overall_results, overall_group_completion = overall_group_completion, tests_size = tests_size)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
