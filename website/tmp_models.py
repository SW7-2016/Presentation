from website import db

class cpu(db.Model):
	__tablename__ = 'cpu'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique=True)
	cores = db.Column(db.Integer)

	def __init__(self, name, cores):
		self.name = name
		self.cores = cores

	def __repr__(self):
		return '<CPU %r, with %i cores>' % self.name, self.cores

class motherboard(db.Model):
	__tablename__ = 'motherboard'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique=True)
	cores = db.Column(db.Integer)

	def __init__(self, name, cores):
		self.name = name
		self.cores = cores

	def __repr__(self):
		return '<MB %r, with %i cores>' % self.name, self.cores