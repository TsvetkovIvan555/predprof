from flask import Flask, render_template, request
import back, os

app = Flask(__name__)

#==================Global_vars=====================

id_user_now = -1
tasks_ind = [[[], [1546087504], [], [], [], [], [], [], [2916180634, 7210576563], [], [], [], [9624466323], [], [], [], [], [], [], [6114071314], [5396808959], [], [], [], [], [7738091925], []], [[8107538073], [], [], [8065011922], [], [6900636397], [], [], [], [], [], [3865783076], [], [], [], [], [], [], [], [], [1289154757], [], [], [3227319211], [], [4010654269, 6465017951], []], [[], [], [], [], [], [], [], [4509329672], [], [], [], [], [], [], [], [9234051873], [], [2816686148], [3004432945], [], [], [], [], [2882934399], [], [], []]]
tests_cnt = 0
while os.path.isfile("sources/tests/test_" + "0"*(9-len(str(tests_cnt))) + str(tests_cnt) + ".txt"):
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
def pres_cub():
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
    random_questions = back.generate_random_questions_for_test(tasks_cnt)
    results = []
    is_found = 1
    if request.method == 'POST':
        data = request.form
        new_data = back.get_results_for_test(data, random_questions)
        results, is_found = new_data[0], new_data[1]
    return render_template('test.html', questions=random_questions, results=results, test_found=is_found, enumerate=enumerate, users_status = status)

#==============================================================================



#=========================================FUCK===================================================

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
            gen_text_file = "sources/tests/test_" + "0"*(9-len(str(tests_cnt))) + str(tests_cnt) + ".txt"
            f = open(gen_text_file, 'w')
            for key, id in a.items(multi=True):
                f.write(id + "\n")
            f.close()
            result = "0"*(9-len(str(tests_cnt))) + str(tests_cnt)
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
        tests = []
        tasks = []
        studens = []
        results = []
        overall_results = []
        overall_group_completion = 1
        tests_size = 0
        return render_template("group1.html", users_status = status, tests = tests, tasks = tasks, studens = studens, results = results, overall_results = overall_results, overall_group_completion = overall_group_completion, tests_size = tests_size)

@app.route('/group')
def group(index):
    status = back.get_users_status(id_user_now)
    tasks = [{"title" : "Title", "due_date" : "28.04.2008", "description" : "haosuvn sud hupsdf ggvudgvn sdhcvghsdghsdhpcvchmsdhmfhmefvchopucfgdsphoucfgsdcdfgscfgsohmps"}]
    lectures = []
    return render_template("group1.html", users_status = status, tasks = tasks, lectures = lectures)

#=================================================================================================

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
