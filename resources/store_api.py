# =============================================================================
# This is the store api
# =============================================================================
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
           return store.json()
        return {'message': "Store '{}' not found".format(name)}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' exists".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occured while creating the store"}, 500

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {"message": "Store '{}' has been deleted"}

#================================================
class StoreList(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}
#==============================================