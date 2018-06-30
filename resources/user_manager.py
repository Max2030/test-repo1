# =============================================================================
# User manager, returns users
# =============================================================================
from flask_restful import Resource
from models.users import UserModel
from flask_jwt_extended import jwt_required

from resources.user_register import UserRegister

class UserManager(Resource):

    @jwt_required
    def get(self, name):
        user = UserModel.find_by_username(name)

        if user:
            return user.json()

        return {'message': "User '{}' does not exist".format(name)}, 400


    @jwt_required
    def put(self, name):
        data = UserRegister.parser.parse_args()

        user = UserModel.find_by_username(name)

        if user:
            user.username = data['username']
        else:
            user = UserModel(**data)
        user.save_to_db()
        return user.json()


    @jwt_required
    def delete(self, name):
        try:
            user = UserModel.find_by_username(name)

            if user:
                user.delete_from_db()
                return {'message': "User '{}' has been deleted!".format(name)}, 200
            else:
                return {'message': "User '{}' does not exist".format(name)}, 404
        except:
            return {"message": "Ann error occurred while deleting user '{}'".format(name)}
#====================================================

class UserList(Resource):

    @jwt_required
    def get(self):
        return {'users': [user.json() for user in UserModel.find_all()]}

#========================================================================

