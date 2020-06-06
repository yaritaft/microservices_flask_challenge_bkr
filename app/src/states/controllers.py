from flask import request
from flask_restplus import Resource

from .dtos import StateDto, StateDtoDetail
from .services import (
    delete_state,
    get_a_state,
    get_all_states,
    save_new_state,
    update_state,
)

api = StateDto.api
_state = StateDto.state
_state_detail = StateDtoDetail.state


@api.route("/")
class StateList(Resource):
    """Endpoint to handle new model state instances and get list of states."""

    @api.doc("list_of_registered_states")
    @api.marshal_list_with(_state, envelope="data")
    def get(self):
        """Get saved states in db.

        Returns
        -------
        Tuple (dict, int)
            Response object and status code. (dict, int)
        """
        return get_all_states()

    @api.response(201, "State successfully created.")
    @api.doc("create a new state")
    @api.expect(_state, validate=True)
    def post(self):
        """Create and saved news states in db.

        Returns
        -------
        Tuple (dict, int)
            Response object and status code. (dict, int)
        """
        data = request.json
        return save_new_state(data=data)


@api.route("/<state_id>")
@api.param("state_id", "The State identifier")
@api.response(404, "State not found.")
class StateDetail(Resource):
    """Endpoint to handle single model state instances."""

    @api.doc("get a state")
    @api.marshal_list_with(_state_detail, envelope="data")
    def get(self, state_id):
        """Get saved state in db.

        Parameters
        ----------
        state_id : int
            state identifier.

        Returns
        -------
        Tuple (dict, int)
            Response object and status code. (dict, int)
        """
        state = get_a_state(state_id)
        print(state)
        if not state:
            api.abort(404)
        return state

    @api.doc("Patch a state")
    @api.expect(_state_detail, validate=True)
    @api.response(200, "State successfully updated.")
    def patch(self, state_id, envelope="data"):
        """Update saved state in db.

        Parameters
        ----------
        state_id : int
            state identifier.

        Returns
        -------
        Tuple (dict, int)
            Response object and status code. (dict, int)
            400 Bad request ID cannot be changed
            404 state not found
            200 state updated
        """
        state = get_a_state(state_id)
        data = request.json
        if not state:
            api.abort(404)
        if update_state(state, data) is not None:
            api.abort(400)
        response_object = {
            "status": "success",
            "message": "Successfully updated.",
        }
        return response_object, 200

    @api.response(200, "State successfully deleted.")
    @api.doc("Delete a state")
    def delete(self, state_id):
        """Delete state from db.

        Parameters
        ----------
        state_id : int
            state identifier.

        Returns
        -------
        Tuple (dict, int)
            Response object and status code. (dict, int)
        """
        state = get_a_state(state_id)
        if not state:
            api.abort(404)
        delete_state(state)
        response_object = {
            "status": "success",
            "message": "Successfully deleted.",
        }
        return response_object, 200
