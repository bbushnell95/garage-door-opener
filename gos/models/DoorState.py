from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction():
    """ Class for performing Transcations on the DB """

    def add(self):
        db.session.add(self)
        db.session.commit()

class DoorState(db.Model, Transaction):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50), nullable=False)
    door_open = db.Column(db.String(10), nullable=False)

    def __init__(self, timestamp, door_open):
        self.timestamp = timestamp
        self.door_open = door_open
