from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(50), unique = True, nullable = False)
    author_name = db.Column(db.String(20))
    publisher = db.Column(db.String(30))

    def __repr__(self):
        return f"{self.book_name} - {self.author_name} - {self.publisher}"


#define routes, routes are URLS that are tied to funcitons
@app.route('/')
def index():
    return 'Hello world!'

#Route will grab all the books
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'book name': book.book_name, 'author name': book.author_name, 'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

#Route that will get a specific id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'book name': book.book_name, 'author name': book.author_name, 'publisher': book.publisher}