# =============================================================================
# This where we refresh tokes
# =============================================================================
from flask_restful import Resource
from flask_jwt_extended import (
        get_jwt_identity,
        jwt_refresh_token_required,
        create_access_token
        )


class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
