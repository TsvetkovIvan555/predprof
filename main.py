from flask import Flask, render_template, request
import random

app = Flask(__name__)

user = 3

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

@app.route('/test', methods=['GET', 'POST'])
def test():
    questions = [
        {'text': 'Какой цвет небо?', 'correct_answer': 'голубой'},
        {'text': 'Какой цвет трава?', 'correct_answer': 'зеленый'},
        {'text': 'Какой цвет кровь?', 'correct_answer': 'красный'},
        {'text': 'Какой цвет солнце?', 'correct_answer': 'желтый'},
    ]

    results = []

    random_questions = random.sample(questions, 2)

    if request.method == 'POST':
        user_answers = [
            request.form.get('answer0', '').lower(),
            request.form.get('answer1', '').lower()
        ]
        correct_answers = [q['correct_answer'] for q in random_questions]

        results.clear()

        for user_answer, correct_answer in zip(user_answers, correct_answers):
            result = {
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'is_correct': user_answer == correct_answer
            }
            results.append(result)

    return render_template('test.html', questions=random_questions, results=results, enumerate=enumerate, user = user)

@app.route('/sign_out')
def sign_out():
    global user
    user = 1
    return render_template("home_page.html", user = user)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
