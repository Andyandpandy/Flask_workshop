from flask import Flask, request, render_template, redirect, url_for, abort

from connection import Firebase_conn

app = Flask(__name__)

conn = Firebase_conn()

"""
Step four involves using the firebase module (created by Ozgur Vatansever).
The Firebase application has a class known as FirebaseApplication, which needs the base url for the firebase.
The firebase module also has the possibility to add authentication for firebase to secure that its not everyone who 
can access the database.
The connection.py file contains two classes one with the connections for firebase and another with a simple exception.
The create_a_user() method is used to create a user and the get_user method is used to get the same user from the 
database.
Also when the user is found this is logged (line 33).
"""


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
