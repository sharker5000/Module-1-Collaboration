from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#$env:FLASK_APP = "application.py"
#$env:FLASK_ENV = "devlopment"

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.name} - {self.book_name}"

@app.route('/')
def index():
    return 'this is the worst website I have ever died in'

@app.route('/books')
def get_books():
    return Books

