from appmain import db
from flask_sqlalchemy import SQLAlchemy

libraries = db.Table('libraries',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True)
	)

class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	

	def __repr__(self):
		return self.username

class Song(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), unique=False, nullable=False)
	users = db.relationship('User', secondary=libraries, lazy='subquery',
							backref = db.backref('songs', lazy=True))

	def __repr__(self):
		return self.title