from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

from database import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    done = db.Column(db.Boolean)

    def __init__(self, title, done):
        self.title = title
        self.done = done

    def __repr__(self):
        return '<id {}>'.format(self.id)
