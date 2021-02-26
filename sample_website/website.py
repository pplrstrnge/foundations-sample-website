from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route('/')
def Code():
    return render_template('code.html', page_title="Code")

def hello_world():
    return '<h1>Hello, Flask!</h1>'


@app.route('/coder')
def coder():
    return render_template('coder.html', page_title="Coder")

@app.route('/venv')
def venv():
    return render_template('venv.html', page_title="Venv")

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        what = request.form.get('what')
        return '<h1>It is {}.' .format(what)

    return '''<form method="POST">
    What? <input type="text" name="what">
    <input type="submit">
    </form>'''


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
