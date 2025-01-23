from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

from database import db

class PingpongCounter(db.Model):
    __tablename__ = 'pingpong_counters'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self):
        self.count = 0

    def __json__(self):
        return ['id', 'count']

    def __repr__(self):
        return '<id {}>'.format(self.id)
