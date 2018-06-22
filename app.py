from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html',name1=" ")

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    surname = request.form['surname']
    name1=name+' '+surname
    return render_template("main.html",name1=name1)


if __name__ == '__main__':
    app.run(debug=True)
