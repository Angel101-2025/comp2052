from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    book_list = [
        {'title': 'Overlord', 'author': 'Kugane Maruyama', 'year': 2012},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
        {'title': 'After Ever After', 'author': 'Jordan Sonneblick', 'year': 2010},
    ]
    return render_template('books.html', books=book_list)

@app.route('/authors')
def authors():
    authors = ['Kugane Maruyama', 'Harper Lee', 'Jordan Sonneblick']
    return render_template('authors.html', authors=authors)
