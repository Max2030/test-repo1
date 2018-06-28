
# =============================================================================
# security data:
#     This will contain the user credentials
# =============================================================================
from models.users import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)



# tets it:
#uu = authenticate('mohamed', 'asdf')
#uu.username
#uu.password





# Let us test it:
#username_mapping['bob']
#userid_mapping[1]