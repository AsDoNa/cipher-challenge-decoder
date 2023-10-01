from flask import Flask,render_template

from ciphers import *

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

app.run()