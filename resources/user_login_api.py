# =============================================================================
# User log object
# =============================================================================
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
        create_access_token, create_refresh_token
        )
from models.users import UserModel

class UserLogin(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This field cannot be blank")
    parser.add_argument('password', type=str, required=True,
                        help="This field cannot be blank")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)

            return{
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
        else:
            return {'message':"Invalid credentials"}, 401