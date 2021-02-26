from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def Code():
    return render_template('code.html', page_title="Code")

def hello_world():
    return '<h1>Hello, Flask!</h1>'


@app.route('/Coder')
def Coder():
    return render_template('coder.html', page_title="Coder")

@app.route('/Venv')
def Venv():
    return render_template('venv.html', page_title="Venv")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
