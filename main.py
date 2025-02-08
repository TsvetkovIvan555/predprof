from flask import Flask, render_template, request
from werkzeug.utils import redirect

import back, os, groups_back

app = Flask(__name__)

#==================Global_vars=====================

id_user_now = -1 # -1 = no user now
tasks_ind = [[[836419444891], [54714164571], [373307514517], [719929041113], [6537890045], [468174815235], [884560013296], [276582272401], [23510334577], [81709467158], [951412760508], [859422950635], [477024075651], [549220021089], [616817205455], [885076946889], [89800173058], [386978173985], [310643678079], [905487982537], [187955124163], [856153098920], [332960568967], [979303093507], [235415132342], [147497730087], []], [[718219017617], [409713330965], [234916589072], [993147590553], [62638306098], [224967226191], [256771631362], [62869871783], [653807849716], [685007139030], [97379047531], [28452000469], [746568985334], [392466207887], [669102236965], [955356573780], [989189727896], [969329243381], [679520903028], [149602234844], [114388616338], [572042017415], [100471967825], [509367248504], [221992969773], [477529217905], []], [[129215051547], [778966339011], [425597834938], [959757203246], [407507204833], [752818999970], [147473509524], [579985474351], [390449290110], [836933766008], [346672184285], [267122594510], [821880882838], [571482425327], [507716000088], [809253149647], [866764057232], [930452074057], [203184133729], [188990648098], [656210420441], [872464592365], [637386167696], [14941199360], [69925198830], [525614198034], []]] # Matrix 3 * 27. Every cell - matrix of tokens with difficulty i and index j
tests_cnt = back.find_cnt_of_tests()
cnt_users = back.find_cnt_of_users()

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
    user = back.users_data(id_user_now)
    return render_template('pers_cab.html', User=user, users_status = status)

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
    index = back.generate_random_token(9)
    a = back.make_new_task(data, index)
    tasks_ind[a[0]][a[1]].append(a[2])
    return render_template("your_token.html", users_status = status, res = index)

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

@app.route('/group<ind>')
def group(ind):
    status = back.get_users_status(id_user_now)
    tasks = groups_back.make_tests_for_groups(ind)
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
