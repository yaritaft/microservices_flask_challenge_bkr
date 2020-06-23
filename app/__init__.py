from flask import Blueprint
from flask_restx import Api

from .src.states.controllers import api as states_endpoint
from .src.users.controllers import api as users_endpoint

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK restx API BOILER-PLATE WITH JWT",
    version="1.0",
    description="a boilerplate for flask_restx web service",
)

api.add_namespace(users_endpoint, path="/users")
api.add_namespace(states_endpoint, path="/states")
