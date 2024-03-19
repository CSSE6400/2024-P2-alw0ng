import datetime 
from . import db 

class Todo(db.Model):
    __tablename__= 'todos'

    #This is how we define a column, this is also the primary key
    id = db.Column(db.Integer, primary_key=True)
    #This isa manadatory column of80characters
    title = db.Column(db.String(80), nullable=False) 
    #This isan optional column of120characters 
    description = db.Column(db.String(120), nullable=True) 
    #This columnhasa default valueofFalse 
    completed = db.Column(db.Boolean,nullable=False, default=False) 
    deadline_at = db.Column(db.DateTime,nullable=True) 
    #This columnhasa default valuewhichis afunctioncall 
    created_at = db.Column(db.DateTime,nullable=False, default=datetime.datetime. utcnow) 
    #This columnhasa default valuewhichis afunctioncalland alsoupdateson update 
    updated_at = db.Column(db.DateTime,nullable=False, default=datetime.datetime. utcnow, onupdate=datetime.datetime.utcnow)

    #This is a helper method to convert the model to a dictionary
    def to_dict(self): 
        return {
            'id': self.id, 
            'title': self.title, 
            'description': self.description, 
            'completed': self.completed, 
            'deadline_at': self.deadline_at.isoformat() if self.deadline_at else None, 
            'created_at': self.created_at.isoformat() if self.created_at else None, 
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    def __repr__(self):
        return f'<Todo {self.id} {self.title}>'
