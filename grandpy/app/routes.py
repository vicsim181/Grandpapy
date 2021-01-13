from flask import render_template
from app import app
from .input_parser import parse


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/api/message/<message>', methods=['GET'])
def api(message):
    return str(parse(message))


@app.route('/map/<search>')
def map(search):
    input = parse(search)
    print("input: " + str(input))
    return render_template('maps.html', input=str(input))
