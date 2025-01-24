from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == "POST":
        return render_template("home_page.html")


@app.route('/')
def main_page():
    return render_template("home_page.html")


@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == "POST":
        return render_template("home_page.html")



@app.route('/test', methods=['GET', 'POST'])
def test():
    results = None
    if request.method == 'POST':
        answer1 = request.form.get('answer1', '').lower()
        answer2 = request.form.get('answer2', '').lower()
        correct_answers = ['голубой', 'зеленый']
        user_answers = [answer1, answer2]
        results = []

        for user_answer, correct_answer in zip(user_answers, correct_answers):
            result = {
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'is_correct': user_answer == correct_answer
            }
            results.append(result)

    return render_template('test.html', results=results)



if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
