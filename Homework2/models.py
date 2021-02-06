from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class books(db.Model):
    __tablename__ = "books"

    book_id = db.Column('book_id', db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(80))
    height = db.Column(db.Integer())
    publisher = db.Column(db.String(80))