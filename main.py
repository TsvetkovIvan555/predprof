from flask import Flask, render_template, request
import back, os

app = Flask(__name__)

#==================Global_vars=====================

id_user_now = -1
tasks_ind = [[[], [442701234045], [], [213356906846], [688796500706], [], [134566501740], [750281280620], [], [307299927110], [], [], [], [], [], [200541182144], [], [], [], [], [], [595142304923], [], [], [], [765399153600], []], [[], [], [], [], [], [], [], [], [], [], [512047613482], [935100716544], [], [982167014755], [397009063134], [], [662206776207], [], [264580247379], [], [370643766438], [], [629389421547], [538606974067], [387565347971], [], [969406941960]], [[905868882709], [373549955085], [376812223976], [], [], [909260051248], [], [], [819684926242], [], [], [], [323037701306], [], [], [], [], [585142304922], [], [467221859587], [], [], [], [], [], [], []]]
tests_cnt = 0
while os.path.isfile("sources/tests/test_" + "0"*(5-len(str(tests_cnt))) + str(tests_cnt) + ".txt"):
    tests_cnt += 1
cnt_users = 2

#====================================================






#===============I know how does it work, and it works correctly =============================

@app.route('/')
def main_page():
    status = back.get_users_status(id_user_now)
    return render_template("home_page.html", users_status = status)

@app.route('/signup', methods=['POST', 'GET'])
def sign_up(): #regestation
    global id_user_now, cnt_users
    if request.method == 'GET':
        status = back.get_users_status(id_user_now)
        return render_template("signup.html", users_status = status)
    elif request.method == "POST":
        data = request.form
        if back.check(data, cnt_users):
            cnt_users += 1
            id_user_now = cnt_users
            back.push_new_user(data, cnt_users)
            status = back.get_users_status(id_user_now)
            return render_template("home_page.html", users_status=status)
        else:
            status = back.get_users_status(id_user_now)
            return render_template("signup_bad.html", users_status=status)

@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    global id_user_now
    if request.method == 'GET':
        status = back.get_users_status(id_user_now)
        return render_template("login.html", users_status = status)
    elif request.method == "POST":
        data = request.form
        ind = back.find_user(data, cnt_users)
        if ind > 0:
            id_user_now = ind
            status = back.get_users_status(id_user_now)
            return render_template("home_page.html", users_status=status)
        elif ind == -1:
            status = back.get_users_status(id_user_now)
            return render_template("password_bad.html", users_status = status)
        else:
            status = back.get_users_status(id_user_now)
            return render_template("login_bad.html", users_status=status)

@app.route('/pers_cab')
def pers_cab():
    status = back.get_users_status(id_user_now)
    User = back.users_data(id_user_now)
    return render_template('pers_cab.html', User=User, users_status = status)

@app.route('/sign_out')
def sign_out():
    global id_user_now
    id_user_now = -1
    status = back.get_users_status(id_user_now)
    return render_template("home_page.html", users_status = status)

@app.route('/task', methods=['GET', 'POST'])
def task():
    status = back.get_users_status(id_user_now)
    gen_n = 0
    gen_tasks = []
    if request.method == 'POST':
        data = request.form
        a = back.generate_task(data, tasks_ind)
        gen_n, gen_tasks = a[0], a[1]
    return render_template("task.html", n = gen_n, tasks = gen_tasks, users_status = status)
#===============================================================================================






#=================I don't know how does it work, but it works correctly================

@app.route('/test', methods=['GET', 'POST'])
def test():
    status = back.get_users_status(id_user_now)
    test_questions = back.generate_random_questions_for_test(tasks_ind)
    results = []
    is_found = 1
    if request.method == 'POST':
        if request.form.get('specific-test-id'):
            test_id = request.form.get('specific-test-id')
            if os.path.isfile("sources/tests/test_" + str(test_id) + ".txt"):
                test_questions = back.generate_specific_test(test_id)
            else:
                is_found = -1
        else:
            data = request.form
            results = back.check_test(data)
    return render_template('test.html', questions=test_questions, results=results, test_found=is_found, enumerate=enumerate, users_status = status)

#==============================================================================



#=========================================FUGG===================================================

@app.route('/add_task', methods=['POST', 'GET'])
def add_task():
    status = back.get_users_status(id_user_now)
    if request.method == 'GET':
        return render_template("add_task.html", users_status = status)
    data = request.form
    a = back.make_new_task(data)
    tasks_ind[a[0]][a[1]].append(a[2])
    return render_template("home_page.html", users_status = status)

@app.route('/lec1')
def lec1():
    status = back.get_users_status(id_user_now)
    return render_template('lection_1.html', users_status = status)

@app.route('/lec2')
def lec2():
    status = back.get_users_status(id_user_now)
    return render_template('lection_2.html', users_status = status)

@app.route('/lec3')
def lec3():
    status = back.get_users_status(id_user_now)
    return render_template('lection_3.html', users_status = status)

@app.route('/add_test', methods=['GET', 'POST'])
def add_test():
    global tests_cnt
    result = -1
    if request.method == 'POST':
        a = request.form
        for key, id in a.items(multi=True):
            if not os.path.isfile("sources/tasks/task_" + str(id) + ".txt"):
                result = -2
        if result != -2:
            gen_text_file = "sources/tests/test_" + "0"*(5-len(str(tests_cnt))) + str(tests_cnt) + ".txt"
            f = open(gen_text_file, 'w')
            for key, id in a.items(multi=True):
                f.write(id + "\n")
            f.close()
            result = "0"*(5-len(str(tests_cnt))) + str(tests_cnt)
            tests_cnt += 1
    status = back.get_users_status(id_user_now)
    return render_template("add_test.html", res = result, users_status = status)


@app.route('/add_course', methods=['POST', 'GET'])
def add_course():
    status = back.get_users_status(id_user_now)
    if request.method == 'GET':
        return render_template("add_course.html", users_status = status)
    elif request.method == "POST":
        return render_template("home_page.html", users_status = status)

@app.route('/add_group', methods=['GET', 'POST'])
def add_group():
    status = back.get_users_status(id_user_now)
    if request.method == 'GET':
        return render_template("add_group.html", users_status = status)
    else:
        status = back.get_users_status(id_user_now)
        tasks = []
        lectures = []
        return render_template("group1.html", users_status=status, tasks=tasks, lectures=lectures)

@app.route('/group1')
def group():
    status = back.get_users_status(id_user_now)
    tasks = [{"title" : "Первый тест", "due_date" : "28.04.2008", "description" : "Пройдите первый тест и получите 2", "test_link" : "/test", "results_link" : "/statistic"},
             {"title" : "Второй тест", "due_date" : "28.04.2008", "description" : "Пройдите второй тест и получите 2", "test_link" : "/test", "results_link" : "/statistic"}]
    lectures = [{"title" : "Первая лекция", "description" : "Пройдите лекцию и узнайте про таблицы истинности", "link" : "/lec1"},
                {"title" : "Вторая лекция", "description" : "Пройдите лекцию и узнайте про графы", "link" : "/lec2"},
                {"title" : "Третья лекция", "description" : "Пройдите лекцию и узнайте про Д.П", "link" : "/lec3"}]
    return render_template("group1.html", users_status = status, tasks = tasks, lectures = lectures)


@app.route('/statistic')
def statistics():
    status = back.get_users_status(id_user_now)
    number_of_tasks = 4
    students = [{"name": "Lev", "results": [1, 100, 4, 5], "final_score": 75},
                {"name": "Misha", "results": [-1, 10, 40, 5], "final_score": 50},
                {"name": "Albert", "results": [1, 100, 40, 5], "final_score": 100}]
    overall_results = [33, 66, 33, 100]
    correct_results = [1, 100, 40, 5]
    overall_group_completion = 44

    return render_template("statistic.html", users_status=status, number_of_tasks=number_of_tasks, students=students,
                           overall_results=overall_results, correct_results=correct_results,
                           overall_group_completion=overall_group_completion)


#=================================================================================================

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
