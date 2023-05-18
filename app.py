from flask import (render_template, 
                   url_for, request) # 'url_for' will connect the links to the html files
from models import db, Pet, app



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-pet', methods=["GET", "POST"])
def add_pet():
    print(request.form)
    print(request.form['name'])
    return render_template('addpet.html')


@app.route('/pet')
def pet():
    return render_template('pet.html')


if __name__ == '__main__':
    db.create_all()     # this replaces the base.metadata.create_all call in SQLAlchemy without Flask
    app.run(debug=True, port=8001, host='127.0.0.1')