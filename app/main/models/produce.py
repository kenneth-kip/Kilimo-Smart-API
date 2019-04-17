""" Produce Model """
from enum import Enum
from .. import db


class ProduceType(Enum):
    """ Produce Enum """
    VEGETABLE = 0
    FRUIT = 1


class Produce(db.Model):
    """ Produce's Model"""
    __tablename__ = "Produce"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.Enum(ProduceType))
    prices = db.relationship(
        'Price', backref=db.backref('produce_prices', lazy=True))

    def __repr__(self):
        return f'<Produce {self.name}>'
