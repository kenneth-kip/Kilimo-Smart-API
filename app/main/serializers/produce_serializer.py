""" Produce Serializer """
from flask_restplus import fields, Namespace
from .price_serializer import PriceSerializer


class ProduceSerializer:
    """ Produce Seializer"""

    api = Namespace('Produce', description="Produce Data Object")
    produce = api.model('produce', {
        'name': fields.String(required=True, description="Produce's name"),
        'type': fields.String(required=True, description="Produce type")
    })
