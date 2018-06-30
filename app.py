# =============================================================================
# Items restful api
# We will be using the parser in the class
# =============================================================================
import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
#from security_data import authenticate, identity

from resources.user_login_api import UserLogin
from resources.user_register import UserRegister, UserById
from resources.user_manager import UserManager, UserList
from resources.items_api import Item
from resources.items_list_api import ItemList
from resources.store_api import Store, StoreList
from resources.token_refresh import TokenRefresh



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mohamed' #app.config['JWT-SECRET_KEY']
api = Api(app)

jwt = JWTManager(app) # this creates /auth end point

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: # This should be coming from the datanase
        return {'is_admin': True}
    return {'is_admin': False}

api.add_resource(UserLogin, '/login')

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')
api.add_resource(UserById, '/userid/<int:user_id>')

api.add_resource(UserManager, '/user/<string:name>')
api.add_resource(UserList, '/users')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(TokenRefresh, '/refresh')

#==================================================
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    # run the appication:
    app.run(port=81)
