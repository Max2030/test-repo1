# =============================================================================
# This is the  user object that we will be using
# =============================================================================
from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def json(self):
        return {'username': self.username, 'password': self.password}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
#==================================================
if __name__ == '__name__':

    user = UserModel.find_by_username('mohamed')
    print('{} {} {}'.format(user.id, user.username, user.password))

    for i in range(1, 7):
        user = UserModel.find_by_id(i)
        print('{} {} {}'.format(user.id, user.username, user.password))
