# =============================================================================
# Items restful api
# We will be using the parser in the class
# =============================================================================
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security_data import authenticate, identity

from resources.user_register import UserRegister, UserById
from resources.user_manager import UserManager, UserList
from resources.items_api import Item
from resources.items_list_api import ItemList
from resources.store_api import Store, StoreList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mohamed'
api = Api(app)

jwt = JWT(app, authenticate, identity) # this creates /auth end point

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')
api.add_resource(UserById, '/userid/<int:user_id>')

api.add_resource(UserManager, '/user/<string:name>')
api.add_resource(UserList, '/users')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

#==================================================
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    # run the appication:
    app.run(port=81)
