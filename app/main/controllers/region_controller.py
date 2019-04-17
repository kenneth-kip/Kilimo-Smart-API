""" Region Controller """
from datetime import datetime

from flask_restplus import Resource, reqparse

from ..serializers.region_serializer import RegionSerializer
from ..serializers.price_serializer import PriceSerializer
from ..models.price import Price as PriceModel
from ..models.region import Region as RegionModel
from ..util.model_helper import get_latest_date


API = RegionSerializer.api
REGION_SERIALIZER = RegionSerializer


@API.route('/<string:name>')
class Region(Resource):
    """ Region Resource """

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
        region_prices = RegionModel.query.filter_by(name=name).all()[0].prices
        date_prices_for_region = list(filter(lambda price: price.date == date,
                                             region_prices))
        return date_prices_for_region


@API.route('/')
class RegionList(Resource):
    """ Region List Resource """

    @API.doc("list_of_regions")
    @API.marshal_list_with(REGION_SERIALIZER.region,
                           envelope='regions')
    def get(self):
        """ Gets the list of regions """
        return RegionModel.query.all()
