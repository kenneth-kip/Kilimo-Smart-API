from flask_restplus import Api
from flask import Blueprint

from .main.controllers.region_controller import API as region_namespace
from .main.controllers.produce_controller import API as produce_namespace
from .main.controllers.price_controller import API as price_namespace

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(region_namespace, path='/regions')
api.add_namespace(produce_namespace, path='/produces')
api.add_namespace(price_namespace, path='/prices')
