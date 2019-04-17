""" Region Model """
from .. import db


class Region(db.Model):
    """ Region's Model"""
    __tablename__ = "Region"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    prices = db.relationship(
        'Price', backref=db.backref('region_prices', lazy=True))

    def __repr__(self):
        return f'<Region %r>' % self.name
