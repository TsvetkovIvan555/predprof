from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/page_0')
@app.route('/navigation')
def navigation():
    return render_template("page_0.html")


@app.route('/page_1')
def page_1():
    return render_template("page_1.html")


@app.route('/page_2')
def page_2():
    return render_template("page_2.html")


@app.route('/page_3')
def page_3():
    return render_template("page_3.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")