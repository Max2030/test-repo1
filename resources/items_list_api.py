# =============================================================================
# This is items list api
# =============================================================================
from flask_restful import Resource

from models.item import ItemModel

class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}

#----------------------------------------------------