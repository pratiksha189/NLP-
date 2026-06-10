from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_BLANK():
    return 'Hello BLANK'

@app.route('/admin')
def hello_admin():
    return 'Hello Administrator'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Welcome %s as guest!' %guest

