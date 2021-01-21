import json
from flask import render_template
from flask.helpers import url_for
from app import app
from .input_parser import parse
from flask import jsonify


@app.route('/', methods=('GET', 'POST'))
@app.route('/home/', methods=('GET', 'POST'))
def home():
    return render_template('home.html')


@app.route('/ajax/<message>', methods=('GET', 'POST'))
def ajax(message):
    print(str(message))
    parsed = parse(message)
    return jsonify({
        "response": f"https://www.google.com/maps/embed/v1/place?key=AIzaSyAstsdkCuu_k4i-V4ZNVW6WTZkYEeMvV1c&q={parsed}"
    })

