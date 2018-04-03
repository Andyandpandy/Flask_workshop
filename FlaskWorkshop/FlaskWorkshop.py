from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/simple_login/', methods=['GET', 'POST'])
def simple_login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        return redirect(url_for('home_page'))
    else:
        abort(403)


@app.route('/home/')
def home_page():
    return render_template('home.html')


@app.route('/settings/')
def settings_page():
    return render_template('settings.html')


@app.route('/logout/')
def logout():
    return redirect(url_for('simple_login'))


if __name__ == '__main__':
    app.run()
