from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    '''Display home page'''
    return render_template('hello.html', title="User Sign-in App")

def is_valid_username_pw(entry):
    '''Validate string and return True if it is between 3 and 20 characters long'''

    if len(entry) >= 3 and len(entry) <= 20:
        if " " in entry:
            return False
        else:
            return True
    else:
        return False

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

    if not is_valid_username_pw(name):
        username_error = 'Not a valid username'

    if not is_valid_username_pw(password):
        password_error = 'Not a valid password'
        password = ''
    else:
        if password_check != password:
            password_check_error = 'Your passwords did not match'
            password = ''
            password_check = ''
    
    if email: #Still need to check for @ and . 
        if not is_valid_username_pw(email):
            email_error = 'Not a valid email'



app.run()


#Tests
# print(is_valid_username_pw("hello there"))
# print(is_valid_username_pw("as"))
# print(is_valid_username_pw("asdfjkl;lkjasdfiqekaslsdklfj;3134"))
# print(is_valid_username_pw("password"))