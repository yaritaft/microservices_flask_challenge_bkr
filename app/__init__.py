from flask_restplus import Api
from flask import Blueprint

from .src.states.controllers import api as states_endpoint
from .src.users.controllers import api as users_endpoint

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK RESTPLUS API BOILER-PLATE WITH JWT",
    version="1.0",
    description="a boilerplate for flask restplus web service",
)

api.add_namespace(users_endpoint, path="/users")
api.add_namespace(states_endpoint, path="/states")
