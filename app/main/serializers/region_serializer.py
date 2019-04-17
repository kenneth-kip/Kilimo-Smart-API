""" Region Serializer """
from flask_restplus import fields, Namespace
from .price_serializer import PriceSerializer


class RegionSerializer:
    """ Region's Seializer """

    api = Namespace('Region', description="Region Data Object")
    region = api.model('region', {
        'name': fields.String(required=True, description="region's name")
    })
