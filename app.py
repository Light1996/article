from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/home')
def home():
    return "Hello World"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/git')
def Git():
    return render_template('git.html')


@app.route('/docker')
def Docker():
    return render_template('docker.html')


@app.route('/flask')
def Flask():
    return render_template('flask.html')


@app.route('/ci')
def cicd():
    return render_template('ci.html')


@app.route('/oop')
def oop():
    return render_template('oop.html')


@app.route('/aaa')
def aaa():
    return render_template('aaa.html')


if __name__ == '__main__':
    app.run(debug=True)
