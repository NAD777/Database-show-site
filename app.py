from flask import Flask
from flask import render_template
from flask import request
from main import db

app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    database = db()
    results = database.get_list()
    database.close()
    return render_template("index.html", results=results)

@app.route('/', methods=['POST'])
def my_form_post():
    database = db()
    if(request.form['btn']=='Add'):
        name = request.form['name']
        surname = request.form['surname']
        database.commit(name,surname)
        results = database.get_list()
    elif(request.form['btn']=='Search'):
        search = request.form['search']
        results = database.get_list(search)
        #dopisat poisk po db
    else:
        print('nothing happened')

    database.close()
    return render_template("index.html",results=results)


if __name__ == '__main__':
    app.run(debug=True)
