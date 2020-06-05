from flask import request
from flask_restplus import Resource

from .dtos import StateDto, StateDtoDetail
from .services import (
    delete_state,
    get_all_states,
    get_a_state,
    save_new_state,
    update_state,
)

api = StateDto.api
_state = StateDto.state
_state_detail = StateDtoDetail.state


@api.route("/")
class StateList(Resource):
    @api.doc("list_of_registered_states")
    @api.marshal_list_with(_state, envelope="data")
    def get(self):
        """List all registered states"""

        return get_all_states()

    @api.response(201, "State successfully created.")
    @api.doc("create a new state")
    @api.expect(_state, validate=True)
    def post(self):
        """Creates a new State """
        data = request.json
        return save_new_state(data=data)


@api.route("/<state_id>")
@api.param("state_id", "The State identifier")
@api.response(404, "State not found.")
class StateDetail(Resource):
    @api.doc("get a state")
    def get(self, state_id):
        """get a state given its identifier"""
        state = get_a_state(state_id)
        print(state)
        if not state:
            api.abort(404)
        return state

    @api.doc("Patch a state")
    @api.expect(_state_detail, validate=True)
    @api.response(200, "State successfully updated.")
    def patch(self, state_id, envelope="data"):
        """get a state given its identifier"""
        state = get_a_state(state_id)
        data = request.json
        if not state:
            api.abort(404)
        update_state(state, data)
        response_object = {
            "status": "success",
            "message": "Successfully updated.",
        }
        return response_object, 200

    @api.response(200, "State successfully deleted.")
    @api.doc("Delete a state")
    def delete(self, state_id):
        """get a state given its identifier"""
        state = get_a_state(state_id)
        if not state:
            api.abort(404)
        delete_state(state)
        response_object = {
            "status": "success",
            "message": "Successfully deleted.",
        }
        return response_object, 200
