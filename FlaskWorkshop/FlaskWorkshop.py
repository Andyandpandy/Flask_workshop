from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/simple_login/', methods=['GET', 'POST'])
def simple_login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        print("post")
        return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run()
