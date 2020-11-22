# AUHack Flask workshop
The Flask workshop presents an opportunity for creating a fast webserver on heroku.com, connecting to a Firebase database and creating endpoints for any device that can connect to the webserver.

In this workshop we will go through seven steps where we will walkthrough what the microframework flask has to offer with very little code. We will be create a simple website with a login. The login will connect to the Firebase check if the user exists and whether or not the password is correct. Besides being able to use Firebase we will connect a device (D1mini as example) to our webserver with and without authentication. 

# What will you learn?
* How to get a Flask webserver running in no time.
* How to use some of the core functionality of Flask.
* How to connect to Firebase from the Flask application.
* How to have a device connect to the Flask application.

# Table of contents
* Step one: Setup https://github.com/AUHack/ws18_flask/tree/Step_one
* Step two: Create a simplelogin https://github.com/AUHack/ws18_flask/tree/Step_two
* Step three: Home & Settings page https://github.com/AUHack/ws18_flask/tree/Step_three
* Step four: Connect firebase https://github.com/AUHack/ws18_flask/tree/Step_four
* Step five: Create a more extensive login https://github.com/AUHack/ws18_flask/tree/Step_five
* Step six: Use session for authentication https://github.com/AUHack/ws18_flask/tree/Step_six
* Step seven: Create endpoints for D1mini https://github.com/AUHack/ws18_flask/tree/Step_seven

# Requirements
* Understanding of simple programming concepts.
* A gmail account for Firebase.
* A free heroku account (https://heroku.com)
* The heroku CLI (https://devcenter.heroku.com/articles/heroku-cli)
* PyCharm is the IDE that will be demonstrated in so preferably PyCharm installed (Jetbrains has student kits).
* Flask is a python microframework, therefore a basic knowledge of python would be useful (not required).

# Installation
1. Download the step you want to use.
2. Create a new directory and paste the FlaskWorkshop folder and virtual folder into this new directory.
3. Open your terminal and change directory (cd) to the FlaskWorkshop folder.
4. Create a heroku app.
5. Use the heroku deploy guide to initialize and upload to the heroku app you have created (Go to your heroku app on heroku.com and click the deploy tab to see more information). 
  * Use the following commands:
  
  * heroku login
  * git init
  * heroku git:remote -a your_heroku_app_name
  * git add .
  * git commit -am "some message"
  * git push heroku master
  
6. Once uploaded you will be able to continue uploading to the heroku server. 
7. Open pycharm with the directory created earlier and continue to develop on your webserver on heroku.  


# Project structure
* Step one: (Flask, files for heroku server & virtualenv)
* Step two: (GET, POST, redirect, url_for, render_template() & request.method) 
* Step three: (Templating, Static, url_for (html) & Jinja2 basics) 
* Step four: (Setup a firebase database and use Ozgur Vatansever firebase module)
* Step five: (Use request.form to get data from html form)
* Step six: (Use a secret_key and the session object to secure authentication)
* Step seven: (Use the request object for getting data, checking headers and finally we will make a response if the auth header is not found)

# About Flask
Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. http://flask.pocoo.org/

Flask is simple and elegant framework that we can use to create nice and easy webservices in no time. This can be extremely helpful for all about to participate in AUHack, since you will be able to set up at webserver that connects to firebase and lets other devices connect to itself in approximately an hour. 
