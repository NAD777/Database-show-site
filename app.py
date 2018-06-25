from flask import Flask
from flask import render_template
from flask import request
from main import db

app = Flask(__name__)
app.debug=True



@app.route('/')
def hello_world():
    return render_template('main.html',name1=" ")

@app.route('/', methods=['POST'])
def my_form_post():
    database = db()
    name = request.form['name']
    surname = request.form['surname']
    name1=name+' '+surname
    database.commit(name,surname)
    database.close()
    return render_template("main.html",name1=name1)


if __name__ == '__main__':
    app.run()
