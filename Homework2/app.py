from flask import Flask, request, flash, url_for, redirect, render_template
from werkzeug.utils import html
from flask_sqlalchemy import SQLAlchemy
from models import db,books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret-key"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
   titlehead = 'Books'
   
   return render_template('index.html', titlehead = titlehead, books = books.query.all() )


@app.route('/home')
def home():
   titlehead = 'Data'
   
   return render_template('home.html', titlehead = titlehead, books = books.query.all() )

@app.route('/home/insert_item', methods = ['GET', 'POST'])
def insert():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['author'] or not request.form['genre'] or not request.form['height'] or not request.form['publisher']:
         flash('Please enter all the fields', 'error')
      else:
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        height = request.form['height']
        publisher = request.form['publisher']
          
        book = books(title=title, author=author, genre = genre, height=height, publisher=publisher)
         
        db.session.add(book)
        db.session.commit()
        flash('successfully')
        return redirect(url_for('home'))
    return render_template('insert.html')

@app.route('/home/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    book = books.query.filter_by(book_id=id).first()
    if request.method == 'POST':
        
        if book:
            db.session.delete(book)
            db.session.commit()
            
            return redirect('/')
        abort(404)
        title = request.form['title']
        book = books(title=title)
 
    return render_template('delete.html',title=book)


@app.route('/home/<int:id>/update',methods = ['GET','POST'])
def update(id):
    book = books.query.filter_by(book_id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            book_id = request.form['book_id']
            title = request.form['title']
            author = request.form['author']
            genre = request.form['genre']
            height = request.form['height']
            publisher = request.form['publisher']
            book = books(book_id=book_id, title=title, author=author, genre=genre, height=height, publisher=publisher)
 
            db.session.add(book)
            db.session.commit()
            return redirect('/home')
        return "book with id = {0} Does not exist".format(id)
 
    return render_template('update.html', books=book)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)