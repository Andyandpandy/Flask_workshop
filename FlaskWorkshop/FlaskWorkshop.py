from flask import Flask, request, render_template, redirect, url_for, abort

from connection import Firebase_conn

app = Flask(__name__)

conn = Firebase_conn()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/simple_login/', methods=['GET', 'POST'])
def simple_login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # Find user Andy
        app.logger.error("The users password is {}".format(conn.get_user('Andy')))
        return redirect(url_for('home_page'))
    else:
        abort(403)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        app.logger.error(username)
        app.logger.error(password)

        #Attempt to find user on firebase
        attempted_username = conn.get_user(username)

        if attempted_username and attempted_username['password'] == password:
            app.logger.error("User is {} and the password matched: {}".format(attempted_username, attempted_username['password'] == password))
            return redirect(url_for('home_page'))

        app.logger.error("The users password is {}".format(conn.get_user('Andy')))
        return redirect(url_for('login'))
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
