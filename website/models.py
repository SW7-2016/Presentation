from website import db

db.Model.metadata.reflect(db.engine)

class cpu(db.Model):
    __table__ = db.Model.metadata.tables['cpu']

    def __repr__(self):
		return '<CPU %r, with %i cores>' % self.name, self.cores
'''
class motherboard(db.Model):
    __tablename__ = db.Model.metadata.tables['motherboard']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    cores = db.Column(db.Integer)
'''
