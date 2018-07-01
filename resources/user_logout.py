# =============================================================================
# This is the log out class:
#     It will be adding the user idenntity of the logging out
#     user into the blacklast data. Hence, next time the user
#     tries to use the api, s/he will need to log in
# =============================================================================
from flask_restful import Resource
from flask_jwt_extended import get_raw_jwt, jwt_required
from blacklist import BLACKLIST

class UserLogout(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti'] # jti is JWT ID
        BLACKLIST.add(jti)
        return {'message': "Successfuly logged out"}, 200