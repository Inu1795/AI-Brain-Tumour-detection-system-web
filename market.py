from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')  # this is a route, a term of Flask called as decorator
@app.route('/home')
def app_mp():
    # render template is an inbuilt function which renders file from app_mp html file
    return render_template('loginpage.html')


@app.route('/login')
def login_page():
    return render_template('loginpage.html')
