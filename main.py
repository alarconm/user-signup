from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    '''Display home page'''
    return render_template('hello.html', title="User Sign-in App")


app.run()