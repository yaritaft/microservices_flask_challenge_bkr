from flask import request
from flask_restplus import Resource

from .dtos import UserDto, UserDtoDetail
from .services import (
    delete_user,
    get_all_users,
    get_a_user,
    save_new_user,
    update_user,
)

api = UserDto.api
_user = UserDto.user
_user_detail = UserDtoDetail.user


@api.route("/")
class UserList(Resource):
    @api.doc("list_of_registered_users")
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """List all registered users"""

        return get_all_users()

    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route("/<user_id>")
@api.param("user_id", "The User identifier")
@api.response(404, "User not found.")
class UserDetail(Resource):
    @api.doc("get a user")
    def get(self, user_id):
        """get a user given its identifier"""
        user = get_a_user(user_id)
        if not user:
            api.abort(404)
        return user

    @api.doc("Patch a user")
    @api.expect(_user_detail, validate=True)
    @api.response(204, "User successfully updated.")
    def patch(self, user_id, envelope="data"):
        """get a user given its identifier"""
        user = get_a_user(user_id)
        data = request.json
        if not user:
            api.abort(404)
        update_user(user, data)
        response_object = {
            "status": "success",
            "message": "Successfully updated.",
        }
        return response_object, 204

    @api.response(204, "User successfully deleted.")
    @api.doc("Delete a user")
    def delete(self, user_id):
        """get a user given its identifier"""
        user = get_a_user(user_id)
        if not user:
            api.abort(404)
        delete_user(user)
        response_object = {
            "status": "success",
            "message": "Successfully deleted.",
        }
        return response_object, 204
