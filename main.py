from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    '''Display home page'''
    return render_template('hello.html', title="User Sign-in App")

@app.route('/', methods=['POST'])
def validate_user():
    '''Validate username, password and email address entered'''

    name = request.form['name']
    password = request.form['password']
    password_check = request.form['password_check']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_check_error = ''
    email_error = ''

    




app.run()