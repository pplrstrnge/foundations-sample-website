from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('menu_template.html')

if __name__ == "__main__":
   