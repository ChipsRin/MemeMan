from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/123456')
def abcd():
    return "Yes"


@app.route('/aaa', methods=['GET'])
def abcdefg():
    data = request.args
    return data

if __name__ == '__main__':
    app.debug = True
    app.run()

