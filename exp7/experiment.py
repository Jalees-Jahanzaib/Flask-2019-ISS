from exp7 import db

class Corpus(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	option = db.Column(db.String(20), unique=True, nullable=False)

class Algorithm(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	option = db.Column(db.String(20), unique=True, nullable=False)

class Training(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	option = db.Column(db.String(20), unique=True, nullable=False)
