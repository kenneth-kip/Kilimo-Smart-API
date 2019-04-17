""" Price Serializer """
from flask_restplus import fields, Namespace


class PriceSerializer:
    """ Price Serializer """

    api = Namespace('Price', description="Price Data Object")
    price = api.model('price', {
        'produce': fields.String(attribute="produce.name",
                                 required=True, description="Price's produce"),
        'quantity': fields.String(required=True, description="Quantity"),
        'low_price': fields.String(required=True, description="Low Price"),
        'high_price': fields.String(required=True, description="High Price"),
        'region': fields.String(attribute="region.name",
                                required=True, description="Price's region"),
        'date': fields.Date(dt_format='rfc822')
    })
