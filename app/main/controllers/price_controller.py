""" Price Controller """
from datetime import datetime

from flask_restplus import Resource, reqparse

from ..serializers.price_serializer import PriceSerializer
from ..models.price import Price as PriceModel
from ..services.price_scraper import PriceScraper
from ..util.model_helper import get_latest_date

API = PriceSerializer.api
PRICE_SERIALIZER = PriceSerializer.price


@API.route('/')
class Price(Resource):
    """ Region Resource """

    @API.doc("Price List", params={'date': 'Price info. date'})
    @API.marshal_list_with(PRICE_SERIALIZER, envelope='prices')
    def get(self):
        """ Gets all the prices """

        parser = reqparse.RequestParser()
        parser.add_argument('date', location="args", type=str,
                            default=get_latest_date(), required=False)
        # Get params date and convert to date object
        args = parser.parse_args()
        date = datetime.strptime(args['date'], '%Y-%m-%d').date()

        return PriceModel.query.filter_by(date=date).all()

    @API.doc("updates_price_list")
    def post(self):
        """ Updates the price list """
        parser = reqparse.RequestParser()
        parser.add_argument('prices', type=list,
                            help="body has no price list",
                            required=True, location='json')
        args = parser.parse_args()
        
        prices = PriceScraper(args['prices'])
        prices.update_new_prices()
        return ('', 204)
