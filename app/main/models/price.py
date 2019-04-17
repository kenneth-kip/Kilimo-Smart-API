""" Price Model """
from datetime import date

from .. import db


class Price(db.Model):
    """ Price's Model"""
    __tablename__ = "Price"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    low_price = db.Column(db.Numeric(scale=2), nullable=False)
    high_price = db.Column(db.Numeric(scale=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    date = db.Column(db.Date, nullable=False, default=date.today)
    region_id = db.Column(db.Integer, db.ForeignKey('Region.id'), nullable=False)
    region = db.relationship('Region', backref=db.backref('Region', lazy=True))
    produce_id = db.Column(db.Integer, db.ForeignKey('Produce.id'), nullable=False)
    produce = db.relationship('Produce', backref=db.backref('Produce', lazy=True))

    def __repr__(self):
        return f'<Price {self.produce.name}-{self.region.name}-{self.date} >'
