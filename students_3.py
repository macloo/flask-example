# using python 3
from flask import Flask, render_template
from data import STUDENTS
app = Flask(__name__)

# define two functions to be used by the routes

# retrieve all the ids from the dataset and put them into a list
def get_ids(source):
    ids = []
    for row in source:
        id = row["id"]
        ids.append(id)
    return sorted(ids)

# find the row that matches the id in the URL, retrieve name and photo
def get_student(source, id):
    for row in source:
        if id == str( row["id"] ):
            name = row["name"]
            photo = row["photo"]
            # change number to string
            id = str(id)
            # return these if id is valid
            return id, name, photo
    # return these if id is not valid - not a great solution, but simple
    return "Unknown", "Unknown", ""

# two decorators using the same function
@app.route('/')
@app.route('/index.html')
def index():
    ids = get_ids(STUDENTS)
    return render_template('index.html', ids=ids)

# your code here
@app.route('/student/<id>')
def student(id):
    # run function to get student data based on the id in the path
    id, name, photo = get_student(STUDENTS, id)
    # pass all the data for the selected student to the template
    return render_template('student.html', id=id, name=name, photo=photo)

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
