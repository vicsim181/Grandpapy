from flask import render_template
from app import app
from .input_parser import parse


@app.route('/')
@app.route('/home/')
def index():
    return render_template('home.html')


@app.route('/api/message/<message>', methods=['GET'])
def api(message):
    return str(parse(message))
