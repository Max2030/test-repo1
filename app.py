# =============================================================================
# Items restful api
# We will be using the parser in the class
# =============================================================================
import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager


from resources.user_login_api import UserLogin
from resources.user_register import UserRegister, UserById
from resources.user_manager import UserManager, UserList
from resources.items_api import Item
from resources.items_list_api import ItemList
from resources.store_api import Store, StoreList
from resources.token_refresh import TokenRefresh
from resources.user_logout import UserLogout
from blacklist import BLACKLIST



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
#-There should be better logic than this----
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
#---------------------------------------------
app.secret_key = 'mohamed' #app.config['JWT-SECRET_KEY']
api = Api(app)

jwt = JWTManager(app) # this creates /auth end point

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: # This should be coming from the datanase
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blacklist_loader
def token_in_blacklist_callback(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST # This should be from database

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
            'message': "The token has expired",
            'error': "Token_expired"
            }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
            'message': "Signiture verification failed",
            'error': "invalid_token"
            }), 401

@jwt.unauthorized_loader
def unauthorised_token_callback():
    return jsonify({
            'message': "Rwquest doe not contain an access token",
            'error': "authorisation_required"
            }), 401

@jwt.needs_fresh_token_loader
def need_fresh_token_callback():
    return jsonify({
            'message': "The token is not fresh",
            'error': "fresh_token_required"
            }), 401

@jwt.revoked_token_loader
def revoke_token_callback():
    return jsonify({
            'message': "The token has been revoked",
            'error': "Token_revoked"
            }), 401


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

api.add_resource(UserLogout, '/logout')

#==================================================
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    # run the appication:
    app.run(port=81)
