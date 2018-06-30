# =============================================================================
# This is items list api
# =============================================================================
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_optional

from models.item import ItemModel

class ItemList(Resource):

    @jwt_optional
    def get(self):

        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]

        if user_id:
            return {'items': items }, 200
        return {
                'items': [item['name'] for item in items],
                'message': "More data available, if you log in!"
            }, 200

#----------------------------------------------------