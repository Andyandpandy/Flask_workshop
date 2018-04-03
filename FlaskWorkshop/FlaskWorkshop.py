from flask import Flask, request, render_template, redirect, url_for, abort, session
import os

from connection import Firebase_conn

app = Flask(__name__)

app.secret_key = os.urandom(24)

conn = Firebase_conn()


@app.route('/')
def hello_world():
    if session.get('username'):
        return 'Hello World!'
    return redirect(url_for('login'))


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
        try:
            username = request.form['username']
            password = request.form['password']
            app.logger.error(username)
            app.logger.error(password)

            # Attempt to find user on firebase
            attempted_username = conn.get_user(username)

            if attempted_username and attempted_username['password'] == password:
                app.logger.error("User is {} and the password matched: {}".format(attempted_username,
                                                                                  attempted_username[
                                                                                      'password'] == password))
                session['username'] = username
                return redirect(url_for('home_page'))

            app.logger.error("The users password is {}".format(conn.get_user('Andy')))
        except KeyError:
            pass
        return redirect(url_for('login'))
    else:
        abort(403)


@app.route('/home/')
def home_page():
    if session.get('username'):
        return render_template('home.html')
    return redirect(url_for('login'))


@app.route('/settings/')
def settings_page():
    if session.get('username'):
        return render_template('settings.html')
    return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
