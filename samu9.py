'''9.Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.'''


# Code
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Create a model for your resources (e.g., books or movies)
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

@app.route('/')
def index():
    resources = Resource.query.all()
    return render_template('index4.html', resources=resources)

@app.route('/add', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_resource = Resource(name=name, description=description)
        db.session.add(new_resource)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add1.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_resource(id):
    resource = Resource.query.get(id)
    if request.method == 'POST':
        resource.name = request.form['name']
        resource.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', resource=resource)

@app.route('/delete/<int:id>')
def delete_resource(id):
    resource = Resource.query.get(id)
    db.session.delete(resource)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")

