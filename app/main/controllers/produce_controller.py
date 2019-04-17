""" Produce Controller """
from datetime import datetime

from flask_restplus import Resource, reqparse

from ..serializers.produce_serializer import ProduceSerializer
from ..serializers.price_serializer import PriceSerializer
from ..models.produce import Produce as ProduceModel
from ..util.model_helper import get_latest_date

API = ProduceSerializer.api
PRODUCE_SERIALIZER = ProduceSerializer


@API.route('/')
class ProduceList(Resource):
    """ Produce esource """
    @API.doc("list_of_regions/locations")
    @API.marshal_list_with(PRODUCE_SERIALIZER.produce, envelope='produce')
    def get(self):
        """ Gets all the produce """
        return ProduceModel.query.all()


@API.route('/<string:name>')
class Produce(Resource):
    """ Produce Resource """

    @API.doc("instance_of_region", params={'date': 'Price info. date'})
    @API.marshal_list_with(PriceSerializer.price, envelope='prices')
    def get(self, name):
        """ Gets a single regions """

        parser = reqparse.RequestParser()
        latest_date = get_latest_date()
        parser.add_argument('date', location="args", type=str,
                            default=latest_date, required=False)
        # Get params date and convert to date object
        args = parser.parse_args()
        date = datetime.strptime(args['date'], '%Y-%m-%d').date()
   
        # Get region prices and filter by date passed
        produce = ProduceModel.query.filter_by(name=name).all()
        if produce:
            produce_prices = produce[0].prices
        else:
            return {'error': 'Produce does not exists'}, 404

        date_prices_for_produce = list(filter(lambda price: price.date == date,
                                              produce_prices))
        return date_prices_for_produce
